"""This modules contains a class that can be used for a LRU Cache.
"""

from problem_1_lib import UniqueQueue


class LRU_Cache(object):
    """Least Recenty Used Cache implementation.

    This is built using a Dictionary for O(1) retrieval and a
    Unique Queue for maintaining least used element.
    """

    def __init__(self, capacity):
        self._capacity = capacity
        self._contents = dict()
        self._lru_queue = UniqueQueue()

    def get(self, key):
        """Retrieves item from provided key. Return -1 if nonexistent.
        """

        if key in self._contents:
            self._lru_queue.push(key)  # update usage
            return self._contents[key]
        else:
            return -1

    def set(self, key, value):
        """Sets the value if the key is not present in the cache.
        If the cache is at capacity remove the oldest item.
        """

        assert key is not None, 'Key cannot be empty'

        if self._is_full():
            self._flush_lru_key()

        self._contents[key] = value
        self._lru_queue.push(key)  # update usage

    def _is_full(self):
        """Returns True if the cache is up to capacity.
        """

        if len(self._contents) >= self._capacity:
            return True
        else:
            return False

    def _flush_lru_key(self):
        """Removes a single entry which was the least recenty used.
        """

        oldest = self._lru_queue.pop()
        assert oldest in self._contents, \
            f'LRU Queue has {oldest} but not the contents'
        del self._contents[oldest]


# Sample test cases are there in the associated Unit Test file
# problem_1_test.py
