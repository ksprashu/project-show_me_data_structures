"""Generate the Huffman encoding and decoding for the provided data.
"""

import sys
from typing import Dict
from problem_3_lib import HuffmannTree, MinTreeNodeHeap


def _get_char_frequency(data) -> Dict:
    """Returns a dictionary with the frequency of each character in the input.
    """

    freq_map = {}
    for c in data:
        if c in freq_map:
            freq_map[c] += 1
        else:
            freq_map[c] = 1

    return freq_map


def _get_frequency_heap(freq_map: Dict) -> MinTreeNodeHeap:
    """Returns a min heap with each character as a Huffmann Tree.
    """

    heap = MinTreeNodeHeap(len(freq_map))
    for c, f in freq_map.items():
        heap.insert(HuffmannTree(c, f))

    return heap


def _get_huffmann_tree(freq_heap: MinTreeNodeHeap) -> HuffmannTree:
    """Returns a tree representing the huffmann tree for the string.

    Recursively pop the first two nodes, merging and inserting it back,
    until there is only one node left.
    """
    while freq_heap.get_size() > 1:
        node1 = freq_heap.pop()
        node2 = freq_heap.pop()
        new_node = HuffmannTree.merge(node1, node2)
        freq_heap.insert(new_node)

    return freq_heap.pop()


def _get_huffmann_codes(tree: HuffmannTree) -> Dict:
    """Returns a dictionary of char to code mapping.
    """
    # pre-order traverse the tree, setting the bit as we traverse
    code_map = {}
    stack = list()
    stack.append((tree.get_root(), ''))  # starting code is empty
    while len(stack) > 0:
        node, code = stack.pop()
        if node.has_left_child():
            stack.append((node.get_left_child(), code + '0'))
        if node.has_right_child():
            stack.append((node.get_right_child(), code + '1'))

        # in case we have reached the leaf, then get the code
        if not node.has_left_child() and not node.has_right_child():
            # handle the case when there is only one character
            if not code and node.get_char():
                code = '1'
            code_map[node.get_char()] = code

    return code_map


def huffman_encoding(data):
    """Encodes the provided data using Huffman coding.

    Will return the encoded data as well as the Huffmann Tree for the data.
    """

    if not data:
        raise AttributeError('Cannot encode empty text')

    freq_map = _get_char_frequency(data)
    freq_heap = _get_frequency_heap(freq_map)
    huff_tree = _get_huffmann_tree(freq_heap)

    # Assign bits to each character by traversing the tree
    code_map = _get_huffmann_codes(huff_tree)
    code = ''
    for d in data:
        assert d in code_map, 'something went wrong building huffmann tree'
        code += code_map[d]

    return code, huff_tree


def huffman_decoding(data, tree):
    """Decodes the provided data using Huffman coding.

    Will return the decoded data based on the provided Huffmann tree.
    """

    index = 0
    text = ''
    node = tree.get_root()
    data = data
    while index < len(data):
        if data[index] == '0':  # traverse left
            assert node.has_left_child(), 'left child was expected for bit 0'
            node = node.get_left_child()
        else:  # traverse right
            # handle the case where code is 1, and only 1 char in data
            if not node.get_char():
                assert node.has_right_child(), \
                    'right child was expected for bit 1'
                node = node.get_right_child()

        if not node.has_left_child() and not node.has_right_child():
            text += str(node.get_char())
            node = tree.get_root()  # reset tree for next iteration

        index += 1  # move to next bit

    return text


if __name__ == "__main__":

    long_text = '''In general, a data compression algorithm reduces the amount
    of memory (bits) required to represent a message (data). The compressed
    data, in turn, helps to reduce the transmission time from a sender to
    receiver. The sender encodes the data, and the receiver decodes the encoded
    data. As part of this problem, you have to implement the logic for both
    encoding and decoding. A data compression algorithm could be either lossy
    or lossless, meaning that when compressing the data, there is a loss
    (lossy) or no loss (lossless) of information. The Huffman Coding is a
    lossless data compression algorithm. Let us understand the two phases -
    encoding and decoding with the help of an example.'''

    sentences = ["The bird is the word", long_text]

    for sentence in sentences:
        print("\nThe size of the data is: {}".format(
            sys.getsizeof(sentence)))
        print("The content of the data is: {}".format(sentence))

        encoded_data, tree = huffman_encoding(sentence)

        print("\nThe size of the encoded data is: {}".format(
            sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("\nThe size of the decoded data is: {}".format(
            sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}".format(decoded_data))
