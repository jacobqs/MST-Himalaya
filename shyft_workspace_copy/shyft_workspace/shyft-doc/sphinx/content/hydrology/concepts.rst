********
Concepts
********

This section contains explanations of the concepts underlying the architectural decisions
and inner workings of this package.

``shyft`` is meant to provide facilities for conducting hydrologic simulations and
accessing uncertainty resulting from the forcing data and decisions regarding
model structure.

Hydrological region model
=========================

The hydrological region-model consists of cells, where each cell have a "personality"
that models the geo-physical properties that best fits that part of the model. Each
cell must have a catchment-identifier, that allows the cells to be summed together in
order to provide catchment scale computations.

At region-level, users can set the method-stack-parameter for each catchment-id.
Technically, this can be done on each cell as well. Each cell can optionally be connected
to a river-model, where the response from the cell to the first river can be shaped by a
convolution mask (u-hydrogram). Rivers get their input from the connected cells, as well
as upstream river-segments, allowing routing to take place, of the sum-flow that is shaped
and delayed using a convolution mask.

The region-model object provides methods to interpolate/project external forcing data, like
temperature, precipitation etc. on to the cells taking the cell-distance/height etc. into account.
Furthermore, it provides means of parameter-optimization where the user provides a goal-function
and ranges for selected parameters, allowing optimization routines to find the parameters
minimizing the value of the goal-function. The specification of a goal function is very flexible,
allowing multiple criteria and period-selective calibration strategies.


Orchestration
=============

In order to perform the simulations Shyft needs to ingest data coming
from observations (meteorological stations, catchment discharges...)
and possible previous calibration runs prior to fill its internal data
structures and proceed with a simulation run. The specification of
this data ingestion process is called 'orchestration' in Shyft.

Although the core of the Shyft simulation code is written in C++, all
the orchestration code is written in Python and uses the Python-API
exposed by Shyft in order to populate the C++ data structures. In
addition, the orchestration code adds another abstraction layer that
allows the end user to write their own repositories classes with a
minimal (or no) knowledge of Shyft core internals.

The orchestration code uses YAML configuration files in order to
define a calibration or simulation run and provides basic
infrastructure in order to read them, but still allowing the user to
add its own code to tailor the calibration/simulation.  This chapter
explains how the user can customize the orchestration process so that
she can better adapt it to read her own data in any format she want.

    ..WARNING::
        The repository and orchestration are undergoing a refactorization
        and some of the following may not be completely relevant or updated.



Repositories
------------

Before to start, we need to introduce the concept of repository in
Shyft.  A repository is just a collection of data in some arbitrary
format, but in Shyft, it has the particular meaning of the **Python code**
that can read this data and feed it to the Shyft core.

The `Shyft.repository` package offers interfaces (via Python ABC
classes) so that the user can provide concrete implementations of his
own repositories. In this approach users can provide their own
repositories customized to their own configuration files (typically
slight variations of the YAML config files that come with Shyft) and a
diversity of data formats (maybe a whole collection of files,
databases, etc.). In addition, some concrete repositories are being
distributed so that they can be used right away. These concrete
repositories can also be taken as an example of implementation for
other user-defined repositories too.

The `generic` repository
^^^^^^^^^^^^^^^^^^^^^^^^

One of the repositories that comes with Shyft, and is named 'generic'
because it is very simple and not meant to read from complicated
datasets. It is more meant as an example on how you can create your
own repositories in case `generic` is not enough for your needs.

For example, in order to choose this repository you have to indicate
this in you 'configuration.yaml' file::

  repository:
    class: Shyft.repository.generic.Config
    params:         # add your own params here to initialize repository

As you can see, you can specify *any* class that is accessible in your
Python installation by using the dotted naming convention
(e.g. Shyft.orchestration2.generic.Config above).

In general, the user is advised to use the generic repository by
default and configure the ingestion of data from different
repositories via a explicit specification.  For example, let's suppose
that you want to access the geo-located time series that Shyft needs
for its simulations via NetCDF4 files, but this is not supported by
the 'generic' repository.  In this case we are going to specify
another repository in the 'datasets.yaml' config file.  Keep reading.


The 'repository' entries in 'datasets.yaml'
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This entry makes possible to declare repository classes for dealing
with different sources and destinations for geo-located time-series.
Let's see an example extracted from the 'datasets.yaml' for the
`netcdf` sub-package (included in Shyft)::

  sources:
    - repository: source_repo1
      class: Shyft.repository.netcdf.SourceDataset
      params:
        stations_met: stations_met.nc
        types:
          - type: precipitation
            stations:
              - values: /station1/precipitation
                time: /station1/time
                location: /station1.x, /station1.y, /station1.z

In this case we want to specify the datasets for the geo-located
time-series sources, and for one of these sources ('source_repo1') we
have specified that we want to use an instance of the
`Shyft.orchestration2.netcdf.SourceDataset` class.  This class can be
user defined, but must always inherit from
`Shyft.orchestration2.BaseSourceDataset`.  Here we have the abstract
interface for it::

  class BaseSourceDataset(BaseConfigFiles):
      """Interface for SourceDataset objects."""
      __metaclass__ = ABCMeta

      @abstractmethod
      def fetch_sources(self, input_source_types, data, params):
          """`data` is a container for geo-located time-series that should be filled (appended)."""
          pass

so, basically you have to build a new class that provides the
`fetch_sources()` method returning the geo-located time-series via the
`data` dictionary of Shyft structures and based on the `params`
parameter that is basically passing the location for the data.  For an
implementation example just have a look at the sources of the
`Shyft.orchestration2.netcdf.SourceDataset` class.

The flexibility just described allows to declare different
repositories for the dataset sources (hybrid sources).

Of course, the same applies to the 'destinations' section of the
'dataset.yaml' file::

  destinations:
    - repository:  dest_repo1
      class: Shyft.repository.netcdf.DestinationDataset
      params:
        simulated_Q: netcdf://simulation.nc/Q
        simulated_SWE: netcdf://simulation.nc/SWE

If you are interested in having your own repositories in a more
general way than just specifying sources and destinations for
geo-located time series, keep reading.


The 'repository' entry in 'configuration.yaml'
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This entry allows the user to replace the regular classes in Shyft that
parse the configuration files by others.  It is important to note that
this entry in 'configuration.yaml' is **optional**, so if you don't
provide a 'repository' the default parser classes will be used.

Here we have an example of the main *bootstrap* way for specifying a
repository in the main 'configuration.yaml' file::

  repository:
    class: Shyft.repository.netcdf.Config
    params:         # add your own params here to initialize repository

Please note that we have replaced the standard `generic` repository
by another one, in this case `netcdf`.

Here there is a 'repository' section where you can specify a Python
class ('class') and some additional 'params' for the class
constructor (`__init__()` method).  In this case, we see that the
'class' entry is specifying the full path to the desired class.  The
orchestration code is then responsible to import the class
appropriately, and in this case it does that as::

  from Shyft.repository.netcdf import Config

so that means that literally any class installed in your computer can
be imported and used inside the `generic` orchestration
infrastructure.  The only limitation is that your class must inherit
from `BaseConfig` ABC class which defines the interface to implement.
Here it is an example of the implementation for the `netcdf`
repository::

    from Shyft.orchestration2.base_config import BaseConfig
    from .model import Model
    from .region import Region
    from .datasets import Datasets

    class Config(BaseConfig):
        """
        Main class hosting a complete configuration section for an Shyft run.
        """

        @property
        def region_config(self):
            if '_region_config' not in self.__dict__:
                self._region_config = Region(self.abspath(self.region_config_file))
            return self._region_config

        @property
        def model_config(self):
            if '_model_config' not in self.__dict__:
                self._model_config = Model(self.abspath(self.model_config_file))
            return self._model_config

        @property
        def datasets_config(self):
            if '_datasets_config' not in self.__dict__:
                self._datasets_config = Datasets(self.abspath(self.datasets_config_file))
            return self._datasets_config

        def process_params(self, params):
            # No additional params yet for the reference
            pass

So, basically, one must define some properties returning instances
that deal with the different configuration files.  Each of these
instances must inherit from ABC classes (interfaces).  For example,
`region_config` returns a sub-instance of
`Shyft.orchestration2.BaseRegion`, `model_config` returns a sub-instance
of `Shyft.orchestration2.BaseModel` and `datasets` returns an instance
of `Shyft.orchestration2.BaseDatasets`.  Note that you don't need to
come up with your own tailored implementation for parsing every config
files, and you may choose to stay with the generic one.

Also, one needs to define the `process_params` method for handling the
different values in the 'params' section of the 'repository' entry.
As the `netcdf` repo does not need any additional parameter, it is
declared as empty above.

This is an easy way to produce your own repositories while you are
still enforced to implement the interfaces that Shyft requires.

**Advice:** If you need to produce your own repository start by
 cloning an existing one (e.g. `netcdf`) and adapting the code to your
 needs.


Summary
========

Shyft let's you specify two different level of customization for
configuring and passing time-series to Shyft:

* Customize the read (sources) and write (destinations) of geo-located
  time series.

* Customize the treatment of configuration files (more complex, but
  doable).


What is a repository?
=====================
A repository in Shyft context provides a minimal interface to a service, that can be used to compose and
orchestrate functionality as required by the business. It typically hides a way non-essential details for
the user, e.g. how information/things are stored/retrieved from backing services and storage layers.

Parameters and responses of a repository interfaces are either basic types like int,string, or domain-objects
that can directly be used by the calling code.


Configuring Shyft
=================

Shyft is configured via `YAML files <http://yaml.org/>`_.  Here it is an example::

    ---
    Himalayas:
      config_dir: .     # where to find other config files
      region_config: region.yaml
      model_config: model.yaml
      # model_config: calibrated_model.yaml
      datasets_config: datasets.yaml
      start_datetime: 1990-07-01T00:00:00
      run_time_step: 86400
      number_of_steps: 730
      max_cells: 4  # consider only a maximum of cells (optional, mainly for testing purposes)
      output:
        params:
          - total_discharge
          - discharge
          - snow_storage
          - temperature
          - precipitation
        format: netcdf
        nc_dir: .   # dir where the output file will be stored
        file: output.nc

    ...

