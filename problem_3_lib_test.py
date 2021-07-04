"""Test cases for Huffman Coding Libaries
"""

import unittest
from problem_3_lib import TreeNode, HuffmannTree, MinTreeNodeHeap


class TreeNodeTest(unittest.TestCase):

    def test_only_freq(self):
        node = TreeNode(None, 10)
        self.assertEqual(node.get_freq(), 10)

    def test_freq_char(self):
        node = TreeNode('A', 10)
        self.assertEqual(node.get_freq(), 10)
        self.assertEqual(node.get_char(), 'A')
        self.assertIsNone(node.get_right_child())

    def test_left_right_nodes(self):
        node = TreeNode(None, 10)
        node.set_left_child(TreeNode('A', 2))
        node.set_right_child(TreeNode('B', 5))
        self.assertIsNotNone(node.get_left_child())
        self.assertIsNotNone(node.get_right_child())
        self.assertEqual(node.get_left_child().get_freq(), 2)
        self.assertEqual(node.get_right_child().get_char(), 'B')

    def test_node1_gt_node2(self):
        node10 = TreeNode(None, 10)
        node20 = TreeNode('R', 20)
        self.assertGreater(node20, node10)


class HuffmannTreeTest(unittest.TestCase):

    def test_only_freq(self):
        tree = HuffmannTree(None, 10)
        self.assertIsNotNone(tree.get_root())
        self.assertEqual(tree.get_root().get_freq(), 10)
        self.assertIsNone(tree.get_root().get_char())

    def test_add_children_first_smaller(self):
        left_child = HuffmannTree('A', 3)
        right_child = HuffmannTree('B', 7)
        tree = HuffmannTree.merge(left_child, right_child)
        # sum of left and right counts matches root node
        self.assertEqual(tree.get_root().get_freq(), 10)
        self.assertEqual(tree.get_root().get_left_child(),
                         left_child.get_root())
        self.assertEqual(tree.get_root().get_right_child(),
                         right_child.get_root())

    def test_add_children_first_larger(self):
        left_child = HuffmannTree('A', 3)
        right_child = HuffmannTree('B', 1)
        tree = HuffmannTree.merge(left_child, right_child)
        self.assertEqual(tree.get_root().get_freq(), 4)
        self.assertEqual(tree.get_root().get_left_child(),
                         right_child.get_root())
        self.assertEqual(tree.get_root().get_right_child(),
                         left_child.get_root())

    def test_tree1_gt_tree2(self):
        tree1 = HuffmannTree('K', 20)
        left_child = HuffmannTree('A', 3)
        right_child = HuffmannTree('B', 7)
        tree2 = HuffmannTree.merge(left_child, right_child)
        self.assertGreater(tree1, tree2)

    def test_merge_contains_treenode(self):
        left_child = HuffmannTree('A', 3)
        right_child = HuffmannTree('B', 1)
        tree = HuffmannTree.merge(left_child, right_child)
        self.assertIsInstance(tree.get_root(), TreeNode)
        self.assertIsInstance(tree.get_root().get_left_child(), TreeNode)
        self.assertIsInstance(tree.get_root().get_right_child(), TreeNode)


class MinHeapTest(unittest.TestCase):

    def test_insert_single_node(self):
        # Prepare
        node = HuffmannTree(None, 2)

        heap = MinTreeNodeHeap(5)
        heap.insert(node)
        self.assertEqual(heap.pop(), node)

    def test_pop_order_with_three_nodes(self):
        # Prepare
        node5 = HuffmannTree(None, 5)
        node2 = HuffmannTree(None, 2)
        node7 = HuffmannTree(None, 7)

        heap = MinTreeNodeHeap(5)
        heap.insert(node5)
        self.assertEqual(heap.peek().get_root().get_freq(), 5)
        heap.insert(node2)  # should get pushed to front
        self.assertEqual(heap.peek().get_root().get_freq(), 2)
        heap.insert(node7)  # should not change the top
        self.assertEqual(heap.peek().get_root().get_freq(), 2)

        # Verify
        self.assertEqual(heap.get_size(), 3)
        self.assertEqual(heap.pop(), node2)
        self.assertEqual(heap.pop(), node5)
        self.assertEqual(heap.pop(), node7)
        self.assertEqual(heap.get_size(), 0)


if __name__ == "__main__":
    unittest.main()
