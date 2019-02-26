**********************************
Logging for OVH Logs Data Platform
**********************************

.. image:: https://img.shields.io/pypi/v/logging-ldp.svg
   :target: https://pypi.python.org/pypi/logging-ldp/
   :alt: Latest Version

.. image:: https://travis-ci.org/cdumay/logging-ldp.svg?branch=master
   :target: https://travis-ci.org/cdumay/logging-ldp
   :alt: Latest version


.. image:: https://readthedocs.org/projects/logging-ldp/badge/?version=latest
   :target: http://logging-ldp.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


A python logging bundle to send logs using GELF on the OVH Logs Data Platform.

Quickstart
==========

First, install logging-ldp using `pip <https://pip.pypa.io/en/stable/>`_::

    pip install -U logging-ldp

The following example shows how to send log in Graylog TCP input

.. code-block:: python

    import logging
    from logging_ldp.formatters import LDPGELFFormatter
    from logging_ldp.handlers import LDPGELFTCPSocketHandler

    logger = logging.getLogger("ldp")
    logger.setLevel(logging.DEBUG)

    handler = LDPGELFTCPSocketHandler(hostname="gra1.logs.ovh.com")
    handler.setFormatter(LDPGELFFormatter(token="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"))
    logger.addHandler(handler)
    logger.debug("hello !")


Requirements
============

- Python >= 3.3

Project Links
=============

- Docs: http://logging-ldp.readthedocs.io/
- PyPI: https://pypi.python.org/pypi/logging-ldp
- Issues: https://github.com/cdumay/logging-ldp/issues
- OVH Logs Data Platform
    - Homepage (FR): https://logs.ovh.com
    - Documentation: https://docs.ovh.com/fr/logs-data-platform/
- Graylog & GELF
    - Documentation: http://docs.graylog.org/en/latest/pages/gelf.html
    - Python logging-gelf: http://logging-gelf.readthedocs.io/

License
=======

Apache License 2.0