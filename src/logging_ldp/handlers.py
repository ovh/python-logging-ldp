#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
# Copyright 2019 The logging-gelf Authors. All rights reserved.

import ssl

from logging_gelf.handlers import GELFTCPSocketHandler


class LDPGELFTCPSocketHandler(GELFTCPSocketHandler):
    def __init__(self, hostname):
        GELFTCPSocketHandler.__init__(
            self, host=hostname, port=12202, use_tls=True,
            cert_reqs=ssl.CERT_NONE, ca_certs=None
        )
