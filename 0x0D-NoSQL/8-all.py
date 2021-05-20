#!/usr/bin/python3
"""
Task 8. List all documents in Python
"""

import pymongo


def list_all(mongo_collection):
    """Function that lists all documents in a collection"""
    list_doc = mongo_collection.find()
    if list_doc == []:
        return []
    else:
        return list_doc
