:mod:`logging_ldp.formatters` --- Formatters
============================================

.. module:: logging_ldp.formatters
    :synopsis: Formatters specify the layout of log records into GELF.

.. moduleauthor:: Cedric Dumay <cedric.dumay@gmail.com>
.. sectionauthor:: Cedric Dumay <cedric.dumay@gmail.com>


.. class:: LDPGELFFormatter 

    A subclass of :class:`logging_ldp.GELFFormatter` to format LogRecord into GELF.

    .. method:: __init__(token, schema=<logging_ldp.schemas.LDPSchema>, null_character=True, JSONEncoder=json.JSONEncoder, exclude_patterns=None)

        A GELF formatter to format a :class:`logging.LogRecord` into GELF.

        :param str token: The LDP token (aka. `X-OVH-TOKEN`).
        :param logging_ldp.schemas.LDPSchema schema: The marshmallow schema to use to format data.
        :param bool null_character: Append a '\0' at the end of the string. It depends on the input used.
        :param json.JSONEncoder JSONEncoder: A custom json encoder to use.
        :param list|None exclude_patterns: List of regexp used to exclude keys

    .. method:: format(record)

        Format the specified record into json using the schema which MUST
        inherit from :class:`logging_ldp.schemas.LDPSchema` to support LDP
        casting type (see: `The field naming convention <https://docs.ovh.com/gb/en/mobile-hosting/logs-data-platform/field-naming-conventions/#id2>`_).

        :param logging.LogRecord record: Contains all the information pertinent to the event being logged.
        :return: A JSON dump of the record.
        :rtype: str

:mod:`logging_ldp.handlers` --- Handlers
========================================

.. module:: logging_ldp.handlers
    :synopsis: Handlers send the log records (created by loggers) to the appropriate GELF inputs.

.. moduleauthor:: Cedric Dumay <cedric.dumay@gmail.com>
.. sectionauthor:: Cedric Dumay <cedric.dumay@gmail.com>

.. class:: LDPGELFTCPSocketHandler

    The :class:`LDPGELFTCPSocketHandler`, which inherit from :class:`logging_gelf.GELFTCPSocketHandler`, sends logging output to a TCP/TLS network socket.

    .. method:: __init__(hostname)

        Initialize a TCP/TLS connection to the given `hostname`.

        :param str hostname: Hostname/FQDN to connect to.

:mod:`logging_ldp.schemas` --- Schemas
======================================

.. module:: logging_ldp.schemas
    :synopsis: Marshmallow schemas used to serialize log record data

.. moduleauthor:: Cedric Dumay <cedric.dumay@gmail.com>
.. sectionauthor:: Cedric Dumay <cedric.dumay@gmail.com>

.. class:: LDPSchema

    Schema which allow to specify a mapping for :class:`logging.LogRecord`. It based on :class:`logging_gelf.schemas.GelfSchema`. All schema MUST inherit from this.

    .. py:staticmethod:: _forge_key(key, value)

        Allow to rename keys to cast types (see: `The field naming convention <https://docs.ovh.com/gb/en/mobile-hosting/logs-data-platform/field-naming-conventions/#id2>`_).

        :param str key: The attribute key
        :param Any value: The attribute value
        :return: The key suffixed
        :rtype: str