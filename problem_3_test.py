"""Test cases for Huffman Coding.
"""

import unittest
from problem_3 import _get_char_frequency, _get_frequency_heap
from problem_3 import _get_huffmann_tree, _get_huffmann_codes
from problem_3 import huffman_decoding, huffman_encoding


class GetCharFrequencyTest(unittest.TestCase):

    def test_frequency_empty(self):
        self.assertEqual(_get_char_frequency(''), {})

    def test_frequency_a(self):
        self.assertEqual(_get_char_frequency('a'), {'a': 1})

    def test_frequency_aa(self):
        self.assertEqual(_get_char_frequency('aa'), {'a': 2})

    def test_frequency_aabbb(self):
        self.assertEqual(_get_char_frequency('aabbb'), {'a': 2, 'b': 3})

    def test_frequency_banana(self):
        self.assertEqual(
            _get_char_frequency('banana'), {'b': 1, 'a': 3, 'n': 2})


class GetHuffmannTreeTest(unittest.TestCase):

    def test_single_node(self):
        tree = _get_huffmann_tree(
            _get_frequency_heap({'A': 1}))
        self.assertIsNotNone(tree)
        self.assertEqual(tree.get_root().get_freq(), 1)
        self.assertEqual(tree.get_root().get_char(), 'A')

    def test_two_nodes(self):
        tree = _get_huffmann_tree(
            _get_frequency_heap({'A': 3, 'B': 1}))
        self.assertIsNotNone(tree)
        self.assertEqual(tree.get_root().get_freq(), 4)
        self.assertIsNone(tree.get_root().get_char())
        self.assertEqual(tree.get_root().get_left_child().get_char(), 'B')
        self.assertEqual(tree.get_root().get_right_child().get_char(), 'A')


class GetHuffmannCodestest(unittest.TestCase):

    def test_long_string(self):
        text = 'AAAAAAABBBCCCCCCCCDDEEEEEE'
        code_map = _get_huffmann_codes(
                    _get_huffmann_tree(
                        _get_frequency_heap(
                            _get_char_frequency(text))))
        self.assertEqual(code_map['A'], '10')
        self.assertEqual(code_map['B'], '001')

    def test_aab(self):
        text = 'AAB'
        code_map = _get_huffmann_codes(
                    _get_huffmann_tree(
                        _get_frequency_heap(
                            _get_char_frequency(text))))
        self.assertEqual(code_map['A'], '1')
        self.assertEqual(code_map['B'], '0')


class HuffmannCodingTest(unittest.TestCase):

    def test_encode_aab(self):
        code, tree = huffman_encoding('aab')
        self.assertEqual(code, '110')
        self.assertEqual(huffman_decoding(code, tree), 'aab')

    def test_encode_abb(self):
        code, tree = huffman_encoding('abb')
        self.assertEqual(code, '011')
        self.assertEqual(huffman_decoding(code, tree), 'abb')

    def test_encode_long_string(self):
        text = 'AAAAAAABBBCCCCCCCCDDEEEEEE'
        expected = '101010101010100010010011111111111111111000000010101010101'
        code, tree = huffman_encoding(text)
        self.assertEqual(code, expected)
        self.assertEqual(huffman_decoding(code, tree), text)

    # throw error if encoding empty string
    def test_encode_empty_string(self):
        with self.assertRaisesRegex(AttributeError, 'empty text'):
            huffman_encoding('')

    def test_single_char(self):
        code, tree = huffman_encoding('a')
        self.assertEqual(huffman_decoding(code, tree), 'a')

    def test_single_char_string(self):
        code, tree = huffman_encoding('AAAAA')
        self.assertEqual(huffman_decoding(code, tree), 'AAAAA')        


if __name__ == "__main__":
    unittest.main()
