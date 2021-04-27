#!/usr/bin/env python3
"""
Task 0. Writing strings to Redis
"""
import redis
import typing
from uuid import uuid4


class Cache:
    """ Cache class """
    def __init__(self):
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """ Method that should generate a random key, store the input data
            in Redis using the random key and return the key """
        r_key = str(uuid4())
        self._redis.set(r_key, data)
        return r_key
