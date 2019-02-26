#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
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

    def format(self, record):
        """Format the specified record into json using the schema which MUST
        inherit from :class:`logging_ldp.schemas.LDPSchema`.

        :param logging.LogRecord record: Contains all the information pertinent
        to the event being logged.
        :return: A JSON dump of the record.
        :rtype: str
        """
        data = self.filter_keys(self.schema().dump(record))
        data['_X-OVH-TOKEN'] = self.token
        out = json.dumps(data, cls=self._encoder_cls)
        if self.null_character is True:
            out += '\0'
        return out
