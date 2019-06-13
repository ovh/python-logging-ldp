#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
# Copyright 2019 The logging-gelf Authors. All rights reserved.

"""
Schema allow to specify a mapping for :class:`logging.LogRecord`. It based on
:class:`marshmallow.Schema`. All schema MUST inherit from
:class:`logging_ldp.schemas.LDPSchema`.
"""
from datetime import datetime, time

from logging_gelf.schemas import GelfSchema


class LDPSchema(GelfSchema):
    @classmethod
    def _forge_key(cls, key, value):
        suffix = ""
        if isinstance(value, float):
            suffix = "_num"
        elif isinstance(value, int):
            suffix = "_int"
        elif isinstance(value, bool):
            suffix = "_bool"
        elif isinstance(value, (datetime, time)):
            suffix = "_date"
        return "{}{}".format(key, suffix)
