from .interfaces import ChannelCoder


class HammingCoder(ChannelCoder):
    def encode(self, data_bits):
        # 문자열을 정수 리스트로 변환
        data_bits = [int(bit) for bit in data_bits]

        # 4비트씩 나누어 인코딩
        encoded_bits = []
        for i in range(0, len(data_bits), 4):
            block = data_bits[i:i+4]
            # 마지막 블록이 4비트가 되도록 패딩 추가
            if len(block) < 4:
                block.extend([0] * (4 - len(block)))
            encoded_bits.extend(self._encode_block(block))

        # 리스트를 문자열로 변환하여 반환
        return ''.join(map(str, encoded_bits))  # 수정된 부분

    def _encode_block(self, data_bits):
        # 해밍(7,4) 코딩 구현
        n = 7  # 총 비트 수

        # 데이터 비트를 7비트로 확장
        coded_bits = [0] * n
        coded_bits[2] = data_bits[0]
        coded_bits[4] = data_bits[1]
        coded_bits[5] = data_bits[2]
        coded_bits[6] = data_bits[3]

        # 패리티 비트 계산
        coded_bits[0] = coded_bits[2] ^ coded_bits[4] ^ coded_bits[6]
        coded_bits[1] = coded_bits[2] ^ coded_bits[5] ^ coded_bits[6]
        coded_bits[3] = coded_bits[4] ^ coded_bits[5] ^ coded_bits[6]

        return coded_bits

    def decode(self, coded_bits):
        # 7비트씩 나누어 디코딩
        decoded_bits = []
        for i in range(0, len(coded_bits), 7):
            block = coded_bits[i:i+7]
            decoded_bits.extend(self._decode_block(block))

        # 리스트를 문자열로 변환
        decoded_bits_str = ''.join(map(str, decoded_bits))

        # 패딩된 0 제거
        decoded_bits_str = decoded_bits_str.rstrip('0')

        return decoded_bits_str

    def _decode_block(self, coded_bits):
        # 해밍(7,4) 디코딩 구현

        # 문자열을 정수로 변환
        coded_bits = [int(bit) for bit in coded_bits]  # 수정된 부분

        # 패리티 비트 계산
        p1 = coded_bits[0] ^ coded_bits[2] ^ coded_bits[4] ^ coded_bits[6]
        p2 = coded_bits[1] ^ coded_bits[2] ^ coded_bits[5] ^ coded_bits[6]
        p4 = coded_bits[3] ^ coded_bits[4] ^ coded_bits[5] ^ coded_bits[6]

        # 오류 위치 계산
        error_position = p1 + (p2 << 1) + (p4 << 2)

        # 오류 수정
        if error_position != 0:
            coded_bits[error_position - 1] ^= 1

        # 데이터 비트 추출
        decoded_bits = [coded_bits[2], coded_bits[4], coded_bits[5], coded_bits[6]]

        return decoded_bits
