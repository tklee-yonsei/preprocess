import unittest

from coder.xor_coder import XORCoder


class TestXORCoder(unittest.TestCase):
    """
    XORCoder 클래스의 인코딩 및 디코딩 기능을 테스트합니다.
    """

    def setUp(self):
        """
        테스트를 위한 XORCoder 인스턴스를 생성합니다.
        """
        self.coder = XORCoder()

    def test_encode(self):
        """
        인코딩 테스트:
        주어진 데이터 비트를 키 "1010"과 XOR 연산하여 올바른 결과를 반환하는지 확인합니다.
        """
        data_bits = "1100"
        expected_coded_bits = [0, 1, 1, 0]  # 키 "1010"과 XOR 연산 결과
        self.assertEqual(self.coder.encode(data_bits), expected_coded_bits)

    def test_decode(self):
        """
        디코딩 테스트:
        주어진 인코딩된 비트를 키 "1010"과 XOR 연산하여 원래 데이터 비트를 올바르게 복원하는지 확인합니다.
        """
        coded_bits = [0, 1, 1, 0]  # 키 "1010"과 XOR 연산된 결과
        expected_data_bits = [1, 1, 0, 0]  # 원래 데이터 비트 "1100"
        self.assertEqual(self.coder.decode(coded_bits), expected_data_bits)

    def test_encode_decode(self):
        """
        인코딩 후 디코딩 테스트:
        데이터 비트를 인코딩한 후 다시 디코딩하여 원래 데이터 비트와 동일한지 확인합니다.
        """
        data_bits = "11010011"
        encoded_bits = self.coder.encode(data_bits)
        decoded_bits = self.coder.decode(encoded_bits)
        self.assertEqual(decoded_bits, [int(bit) for bit in data_bits])


if __name__ == "__main__":
    unittest.main()