.. _Project:

**************
What is Shyft?
**************

The project name was originally an acronym standing for (S)tatkraft (Hy)drology (F)orecasting (T)oolbox when
the package was developed internally by the Norwegian Power company `Statkraft <http://www.statkraft.com>`_.

Essential for the development of the toolbox was the cooperation with the scientists at the
`University of Oslo's Department of Geosciences <http://geo.uio.no>`_ and in 2015 Statkraft
decided to publish the code as `Open Source <https://en.wikipedia.org/wiki/Open_source>`_
project under the `LGPL V.3 <https://www.gnu.org/licenses/lgpl-3.0.en.html>`_.

Both entities actively develop the toolbox. Shyft software components are used in active 24x7 operation at Statkraft.
This allows model experts in the business domain, scientists at institutes/universities together with professional
programmers cooperating efficiently to provide a high-performance toolbox for hydrology in the energy market domain.

The overall goal for the toolbox is to provide **python-enabled high performance components with operational quality**.
This includes (but is not limited to) the features listed below:

  * completely transparent and open available source-code
  * use of C++ as primary core language and Python as orchestration and interaction layer
  * well designed components and algorithms aiming at speed, robustness and scalability
  * use of well known high performance open-source 3rd party libraries
  * unit-tests and integration tests with high code coverage
  * continuous build-test-deploy on many platforms (Linux, Windows, even Raspberry Pi/ARM is possible)
  * creation of individual packages supporting private in-house build-systems
  * concise documentation with many examples facilitating ease-of-use
  * integrated issue tracking, merge-requests, allowing everyone to contribute

Some of our tools and libraries will work nice for other domains as well, like the :ref:`PackageTimeSeries`.
