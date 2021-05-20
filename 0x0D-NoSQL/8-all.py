#!/usr/bin/env python3
"""
Task 8. List all documents in Python
"""


def list_all(mongo_collection):
    """Function that lists all documents in a collection"""
    list_doc = mongo_collection.find()
    if list_doc.count() == 0:
        return []
    else:
        return list_doc
