import unittest

from coder.hamming_coder import HammingCoder


class TestHammingCoder(unittest.TestCase):
    def setUp(self):
        self.coder = HammingCoder()

    def test_encode(self):
        data_bits = "1011"
        expected_coded_bits = "0110011"
        self.assertEqual(self.coder.encode(data_bits), expected_coded_bits)

    def test_decode_with_error(self):
        coded_bits = "0110011"
        expected_data_bits = "1011"
        self.assertEqual(self.coder.decode(coded_bits), expected_data_bits)

    def test_encode_decode(self):
        data_bits = "11010011"
        encoded_bits = self.coder.encode(data_bits)
        decoded_bits = self.coder.decode(encoded_bits)
        self.assertEqual(decoded_bits, data_bits)


if __name__ == "__main__":
    unittest.main()
