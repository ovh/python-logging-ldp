#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
# Copyright 2019 The logging-gelf Authors. All rights reserved.

import json

from logging_gelf.formatters import GELFFormatter
from logging_ldp.schemas import LDPSchema


class LDPGELFFormatter(GELFFormatter):
    def __init__(self, token, schema=LDPSchema, null_character=True,
                 JSONEncoder=json.JSONEncoder, exclude_patterns=None):
        GELFFormatter.__init__(
            self, schema, null_character, JSONEncoder, exclude_patterns
        )
        self.token = token

    def serialize_record(self, record):
        """Serialize logging record into a dict

        :param record:
        :param logging.LogRecord record: Contains all the information pertinent
        to the event being logged.
        :return: A dict dump of the record.
        :rtype: dict
        """
        data = GELFFormatter.serialize_record(self, record)
        data['_X-OVH-TOKEN'] = self.token
        return data
