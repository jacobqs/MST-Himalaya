DTSS - Distributed Time Series System
=====================================

The DTSS provides services and components, that can be used and orchestrated from python, as well as directly
in c++ applications and libraries.

The DtsServer provides a python customizable server, that provides two high performance network interfaces:

  1. Raw socket exchanging messages produced by boost.serialization, binary
  2. Web-api socket interface, exchanging json messages. We use boost.beast,
     and boost.spirit to provide a high performance in all phases of the communication and handling.
     The web-api also provides subscription mechanisms, so that changes to expressions/time-series are
     pushed to the client when changes are detected.

Python users can enjoy the DtsClient interface, providing a typesafe, robust,
high performance easy to use synchronous interface.

Web front-end developers and users, and integrators might benefit from the web-api interface.

Most important part of the DTSS concept, is that the core itself can be embedded into **model based** services,
where the time-series (expressions) are attached to a model.

Similar as for the DTSS, these services also provide dual interface as explained above,
and they are also orchestrated, configured, extended by python.

The DtsServer can be customized adding python hooks, so that you can integrate your own/existing
time-series databases, services or even custom computation models.

In addition, the DtsServer, and its component can serve in master/slave configuration,
so that computations can be distributed(with local caching), yet at the same time
have a centralized storage for incoming/stored time-series.
