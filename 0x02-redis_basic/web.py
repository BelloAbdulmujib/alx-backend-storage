#!/usr/bin/env python3
'''module to obtain the HTML content of a particular URL and returns it
'''

import redis
import requests
from typing import Callable
from functools import wraps


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def get(self, key: str) -> str:
        return self._redis.get(key)

    def set(self, key: str, value: str, ex: int):
        self._redis.set(key, value, ex=ex)

    def incr(self, key: str):
        self._redis.incr(key)

cache = Cache()

def count_requests(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(url: str) -> str:
        cache.incr(f"count:{url}")
        cached_page = cache.get(f"cache:{url}")
        if cached_page:
            return cached_page.decode('utf-8')

        page_content = func(url)
        cache.set(f"cache:{url}", page_content, ex=10)
        return page_content
    return wrapper

@count_requests
def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response'''
    response = requests.get(url)
    return response.text
