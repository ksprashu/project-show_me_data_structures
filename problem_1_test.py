"""Test cases for LRU Cache.
"""

import unittest
from problem_1 import LRU_Cache


class LRUCacheTest(unittest.TestCase):

    def test_empty_cache(self):
        cache = LRU_Cache(2)
        self.assertEqual(cache.get(3), -1)

    def test_single_value(self):
        cache = LRU_Cache(2)
        cache.set(3, 'test')
        self.assertEqual(cache.get(3), 'test')

    def test_missing_value(self):
        # Setup
        cache = LRU_Cache(5)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)

        # Verify
        # 9 was not pushed in and hence it will be a cache miss
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(9), -1)

    def test_cache_flush(self):
        # Setup
        cache = LRU_Cache(5)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)

        # Act
        # we are pushing a total of 6 elements,
        # whereas the cache size is only 5
        # Hence the least recently used element will get flushed
        # which is 3
        cache.get(1)
        cache.get(2)
        cache.set(5, 5)
        cache.set(6, 6)

        # Verify
        # 3 should not be found, but 6 should be
        self.assertEqual(cache.get(3), -1)
        self.assertEqual(cache.get(6), 6)

    def test_high_volume_data_available(self):
        cache = LRU_Cache(2)
        cache.set(1, 1)
        cache.set(2, 2)
        for _ in range(10000):
            self.assertEqual(cache.get(1), 1)

    def test_high_volume_turns_old(self):
        cache = LRU_Cache(2)
        cache.set(1, 1)
        cache.set(2, 2)
        for _ in range(100):
            self.assertEqual(cache.get(1), 1)

        # 2 is now the newest, even though 1 was fetched 100 times.
        self.assertEqual(cache.get(2), 2)

        cache.set(3, 3)  # this should flush key 1
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(2), 2)

    def test_key_not_available(self):
        cache = LRU_Cache(5)
        cache.set(100, 10)
        cache.set(200, 20)
        cache.set(300, 30)
        cache.set(400, 40)

        for i in range(100):
            self.assertEqual(cache.get(i), -1)

    def test_bad_key_set(self):
        cache = LRU_Cache(4)
        with self.assertRaises(AssertionError):
            cache.set(None, None)

    def test_negative_key(self):
        cache = LRU_Cache(5)
        cache.set(-1211, 10)
        self.assertEqual(cache.get(-1211), 10)

    def test_large_value(self):
        cache = LRU_Cache(5)
        cache.set('test', 8817298371872038910723981728903718923710928731908273189207391082371027319827301273981273)
        self.assertRegex(str(cache.get('test')), r'^88172.+81273$')


if __name__ == '__main__':
    unittest.main()
