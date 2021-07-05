"""Test cases for LRU Cache Library.
"""

import unittest
from problem_1_lib import DoubleNode, UniqueQueue


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

        # Verify: The left node of the right node is the current node itself
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

        # Verify: Values are returned in the order it was pushed in
        self.assertEqual(q.pop(), 10)
        self.assertEqual(q.pop(), 20)
        self.assertIsNone(q.pop())

    def test_push_element_twice(self):
        # Setup
        q = UniqueQueue()
        q.push(10)
        q.push(20)
        q.push(10)

        # Verify: 20 is popped first and then 10
        # Since 10 is pushed twice, it is the newer one
        # hence 20 should be popped out first
        # Also we should have only one copy of 10
        self.assertEqual(q.pop(), 20)
        self.assertEqual(q.pop(), 10)
        self.assertIsNone(q.pop())
