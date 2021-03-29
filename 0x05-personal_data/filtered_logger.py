#!/usr/bin/env python3
"""
filter_logger.py
"""
import typing
import re


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Function that returns the log message obfuscated"""
    for i in fields:
        message = re.sub(
            i +
            "=[^=]*" + separator,
            i +
            "=" +
            redaction +
            separator,
            message)
    return message
