.. logging-ldp documentation master file, created by
   sphinx-quickstart on Wed Jan 18 17:11:49 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

logging-ldp
============

A python 3 logging bundle to send logs using GELF on the `OVH Logs Data Platform <https://logs.ovh.com>`_.
The following example shows how to send log over TCP/TLS input.

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

Get It Now
----------

First, install logging-ldp using `pip <https://pip.pypa.io/en/stable/>`_::

    pip install -U logging-ldp

API focus
---------

The api is many only an implementation of `logging-gelf <https://logging-gelf.readthedocs.io/en/latest/index.html>`_

.. toctree::
   :maxdepth: 1

   api_focus.rst