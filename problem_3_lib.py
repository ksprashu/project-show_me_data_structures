"""Library class for problem_3.

    Defines the following classes
    - TreeNode
    - Huffmann Tree

    Defines the following functions
    - _get_char_frequency()

"""

from __future__ import annotations


class TreeNode():
    """"Class to represent a node of a Huffmann tree.
    """

    def __init__(self, char, freq):
        self._char = char
        self._freq = freq
        self._left_child = None
        self._right_child = None

    def get_left_child(self):
        return self._left_child

    def set_left_child(self, node):
        self._left_child = node

    def has_left_child(self):
        return self._left_child is not None

    def get_right_child(self):
        return self._right_child

    def set_right_child(self, node):
        self._right_child = node

    def has_right_child(self):
        return self._right_child is not None

    def get_freq(self):
        return self._freq

    def get_char(self):
        return self._char

    def __gt__(self, node):
        if self.get_freq() > node.get_freq():
            return True
        else:
            return False


class MinTreeNodeHeap():
    """Min Heap of nodes of a Huffman Tree

    This uses HuffmannTree as a element and the heap is sorted by the frequency
    of the characters. The implementation uses a list to store the nodes.
    """

    def __init__(self, initial_size):
        self._nodes = [None for i in range(initial_size + 1)]
        self._size = 0
        self._bottom = 1  # we are not using index 0

    def get_size(self):
        return self._size

    def _get_left_index(self, index):
        return 2 * index

    def _get_left_child(self, index):
        return self._nodes[self._get_left_index(index)]

    def _get_right_index(self, index):
        return 2 * index + 1

    def _get_right_child(self, index):
        return self._nodes[self._get_right_index(index)]

    def _get_parent_index(self, index):
        return index // 2

    def _get_parent_node(self, index):
        return self._nodes[self._get_parent_index(index)]

    def insert(self, tree):
        """Inserts a new element into the heap.
        """
        # currently we are not adding the capability to grow the heap
        assert self._size < len(self._nodes)

        self._nodes[self._bottom] = tree
        self._size += 1
        self._bottom += 1

        if self._size > 1:
            self._heapify_up(self._bottom - 1)

    def peek(self):
        """Reads the topmost element without popping it.
        """
        return self._nodes[1]

    def pop(self):
        """Pops the smallest element from the heap.

        Swap the top element with the bottom-most and then remove the bottom
        and then rebalance the heap.
        """
        if self._bottom == 1:
            return None

        top = self._nodes[1]
        self._size -= 1
        self._bottom -= 1
        self._nodes[1] = self._nodes[self._bottom]
        self._nodes[self._bottom] = None
        self._heapify_down(1)

        return top

    def _heapify_down(self, index):
        """Recursively swaps current node with its smaller child,
        if current node is smaller than the smaller child.

        This rebalances the tree from the root down to the leaves.
        """
        # 1. get the index of the smallest child of the root node
        # 2. compare the root node with the smallest child
        # 3a. if root is larger, then swap with the smaller child
        # 4. now repeat for index = index of smaller child
        # 3b. if root is smaller, terminate

        smallest_index = self._get_left_index(index)

        # base condition, if at the bottom then end
        if index >= self._bottom or smallest_index >= self._bottom:
            return

        if self._get_right_child(index) and \
           self._get_left_child(index) > self._get_right_child(index):
            smallest_index = self._get_right_index(index)
        if self._swap_nodes_if_larger(index, smallest_index):
            self._heapify_down(smallest_index)

    def _heapify_up(self, index):
        """Recursively swaps current node with its parent,
        if parent is larger than child (current node).

        This is used to rebalance tree from leaf node up to root.
        """
        # 1.get the index of the parent
        # 2a. if child is smaller than parent, swap with the parent
        # 3. repeat for index = index of parent
        # 2b. if child is larger, terminate

        # base condition, if at the top then end
        if index <= 1:
            return

        parent_index = self._get_parent_index(index)
        if self._swap_nodes_if_larger(parent_index, index):
            self._heapify_up(parent_index)

    def _swap_nodes_if_larger(self, parent, child):
        """Swaps the two nodes if node1 > node 2.
        """
        if self._nodes[parent] > self._nodes[child]:
            self._nodes[parent], self._nodes[child] = \
                self._nodes[child], self._nodes[parent]
            return True

        return False


class HuffmannTree():
    """Tree to represent the data for Huffmann Tree.

    The tree will do some basic validations to maintain the properties of a
    Huffmann tree.

    Eg: It will allow addition of both left and right nodes together
    and the sum of frequency of the children should equal frequency of the root
    """

    def __init__(self, char, freq):
        self._root = TreeNode(char, freq)

    def get_root(self) -> TreeNode:
        return self._root

    @staticmethod
    def merge(tree1: HuffmannTree, tree2: HuffmannTree) -> HuffmannTree:
        """Merges the two trees and returns the merged tree.

        The sum of frequency of left and right nodes should equal the
        frequency of the root of the tree. The left and right nodes may be
        the root nodes to deep trees.
        """
        assert tree1 is not None and tree2 is not None, 'Cant merge null nodes'
        freq_sum = tree1.get_root().get_freq() + \
            tree2.get_root().get_freq()

        left_node = tree1
        right_node = tree2
        if tree1 > tree2:
            left_node = tree2
            right_node = tree1

        new_tree = HuffmannTree(None, freq_sum)
        new_tree.get_root().set_left_child(left_node.get_root())
        new_tree.get_root().set_right_child(right_node.get_root())

        return new_tree

    def __gt__(self, tree):
        if self.get_root() > tree.get_root():
            return True
        else:
            return False
