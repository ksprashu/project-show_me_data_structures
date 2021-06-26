import unittest
from problem_1 import DoubleNode, UniqueQueue, LRU_Cache


class DoubleNodeTest(unittest.TestCase):

    def test_single_node(self):
        node = DoubleNode(10)
        self.assertEqual(node.get_value(), 10)
        self.assertIsNone(node.get_left_node())
        self.assertIsNone(node.get_right_node())

    def test_add_left_node(self):
        node = DoubleNode(10)
        node.set_left_node(DoubleNode(5))
        self.assertIsNotNone(node.get_left_node())
        self.assertEqual(node.get_left_node().get_value(), 5)

    def test_add_right_node(self):
        node = DoubleNode(10)
        node.set_right_node(DoubleNode(20))
        self.assertIsNotNone(node.get_right_node())
        self.assertEqual(node.get_right_node().get_value(), 20)

    def test_left_of_right_node_is_self(self):
        node = DoubleNode(10)
        node.set_right_node(DoubleNode(20))
        self.assertIsNotNone(node.get_right_node().get_left_node())
        self.assertEqual(node.get_right_node().get_left_node().get_value(), 10)


class UniqueQueueTest(unittest.TestCase):

    def test_empty_new_queue(self):
        q = UniqueQueue()
        self.assertIsNone(q.pop())

    def test_queue_has_two_elements(self):
        # Setup
        q = UniqueQueue()
        q.push(10)
        q.push(20)

        # Verify
        self.assertEqual(q.pop(), 10)
        self.assertEqual(q.pop(), 20)
        self.assertIsNone(q.pop())

    def test_push_element_twice(self):
        # Setup
        q = UniqueQueue()
        q.push(10)
        q.push(20)
        q.push(10)

        # Verify
        self.assertEqual(q.pop(), 20)
        self.assertEqual(q.pop(), 10)
        self.assertIsNone(q.pop())


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
        cache.get(1)
        cache.get(2)
        cache.set(5, 5)
        cache.set(6, 6)

        # Verify
        self.assertEqual(cache.get(3), -1)
        self.assertEqual(cache.get(6), 6)


if __name__ == '__main__':
    unittest.main()
