***************
Getting started
***************

.. include:: ../_shared/help.rst

The best way to get started with Shyft is to work on some of the notebooks that we have developed.
The following notebooks are available in the `shyft-doc <https://gitlab.com/shyft-os/shyft-doc>`_ repository.
You can download and run these on your local computer, or browse through them here.

General examples
----------------
It is recommended to go through these simple notebooks first, just to get a sense of what Shyft can do.

.. toctree::
    :maxdepth: 1

    ../../notebooks/api/api-intro.ipynb
    ../../notebooks/api/api-essentials.ipynb
    ../../notebooks/repository/repositories-intro.ipynb
    ../../notebooks/shyft-intro-course-master/run_api_model.ipynb

Configured simulation
---------------------
Once you've completed that, take a look at the configured examples. These use `yaml` files to keep model
configuration data, and are a good starting point for understanding how to set up a Shyft simulation with your
own data.

.. toctree::
    :maxdepth: 1

    ../../notebooks/nea-example/calibration-configured.ipynb
    ../../notebooks/nea-example/simulation-configured.ipynb
    ../../notebooks/nea-example/run_nea_nidelva.ipynb
    ../../notebooks/nea-example/advanced_simulation.ipynb

Advanced tools
--------------
Shyft contains a lot of functionality. A few pieces are shown in the following notebooks.

.. toctree::
    :maxdepth: 1

    ../../notebooks/grid-pp/gridpp_geopoints.ipynb
    ../../notebooks/grid-pp/kalman_updating.ipynb
    ../../notebooks/grid-pp/ordinary_kriging_precipitation.ipynb
    ../../notebooks/penman-monteith/penman-monteith-verification-single-method.ipynb
    ../../notebooks/penman-monteith/penman-monteith-sensitivity.ipynb
    ../../notebooks/radiation/polar_region_radiaiton.ipynb
    ../../notebooks/radiation/radiation-sensitivity-analysis.ipynb
    ../../notebooks/radiation/radiation_camelsdata.ipynb