#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
import ssl

from logging_gelf.handlers import GELFTCPSocketHandler


class LDPGELFTCPSocketHandler(GELFTCPSocketHandler):
    def __init__(self, hostname):
        GELFTCPSocketHandler.__init__(
            self, host=hostname, port=12202, use_tls=True,
            cert_reqs=ssl.CERT_NONE, ca_certs=None
        )
