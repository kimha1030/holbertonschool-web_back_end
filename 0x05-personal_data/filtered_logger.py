#!/usr/bin/env python3
"""
filter_logger.py
"""
import typing
import re
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        """ Constructor """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Method to filter values in incoming log records
            using filter_datum"""
        return filter_datum(
            self.fields,
            self.REDACTION,
            super(
                RedactingFormatter,
                self).format(record),
            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ Method that returns a logging.Logger object """
    logger = logging.getLogger("user_data")
    logger.propagate = False
    s_handler = logging.StreamHandler()
    s_handler.setLevel(logging.INFO)
    formatter = RedactingFormatter(PII_FIELDS)
    s_handler.setFormatter(formatter)
    logger.addHandler(s_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Method that returns  a connector to the database object"""
    info_user = "PERSONAL_DATA_DB_USERNAME"
    info_pwd = "PERSONAL_DATA_DB_PASSWORD"
    info_host = "PERSONAL_DATA_DB_HOST"
    info_db = "PERSONAL_DATA_DB_NAME"
    cnx = mysql.connector.connection.MySQLConnection(
        user=os.getenv(
            info_user, "root"), password=os.getenv(
            info_pwd, ""), host=os.getenv(
                info_host, "localhost"), database=os.getenv(info_db))
    return cnx


def main():
    """Main function"""
    database = get_db()
    cursor = database.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    logg = get_logger()
    for row in cursor:
        str_text = ''
        for k in row:
            str_text = str_text + f'{k}={row[k]}; '
        print(str_text)
    cursor.close()
    database.close()


if __name__ == "__main__":
    main()
