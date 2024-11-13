import unittest

from coder.repetition_coder import RepetitionCoder


class TestRepetitionCoder(unittest.TestCase):
    def setUp(self):
        self.coder = RepetitionCoder()

    def test_encode(self):
        data_bits = "101"
        expected_coded_bits = "111000111"
        self.assertEqual(self.coder.encode(data_bits), expected_coded_bits)

    def test_decode_with_error(self):
        coded_bits = "110000100"  # 노이즈가 낀 비트도 정상 복원 확인
        expected_data_bits = "100"
        self.assertEqual(self.coder.decode(coded_bits), expected_data_bits)

    def test_encode_decode(self):
        data_bits = "1101"
        encoded_bits = self.coder.encode(data_bits)
        decoded_bits = self.coder.decode(encoded_bits)
        self.assertEqual(decoded_bits, data_bits)


if __name__ == "__main__":
    unittest.main()

