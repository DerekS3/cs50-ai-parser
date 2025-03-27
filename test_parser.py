import unittest
from parser import *


class TestPreprocess(unittest.TestCase):
    def setUp(self):
        None
        
    def test_preprocess_two_words(self):
        sentence = "Holmes sat."
        expected_result = ["holmes", "sat"]
        self.assertEqual(preprocess(sentence), expected_result)

    def test_preprocess_many_words(self):
        sentence = "The 3 MR. cats $ sat on the... MAT!"
        expected_result = ["the", "mr.", "cats", "sat", "on", "the", "mat"]
        self.assertEqual(preprocess(sentence), expected_result)


class TestNpChunk(unittest.TestCase):
    def setUp(self):
        None
        
    def test_np_chunk(self):
        s = preprocess("Holmes sat down and lit his pipe.")
        trees = list(parser.parse(s))
        chunks = []
        for tree in trees:
            for np in np_chunk(tree):
                chunks.append(" ".join(np.flatten()))
        expected_result = ['holmes', 'his pipe']
        self.assertEqual(chunks, expected_result)


if __name__ == '__main__':
    unittest.main()