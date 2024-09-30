from .interfaces import ChannelCoder


class XORCoder(ChannelCoder):
    def __init__(self, key="1010"):
        self.key = [int(bit) for bit in key]

    def encode(self, data_bits):
        data_bits = [int(bit) for bit in data_bits]
        return self._xor_operation(data_bits)

    def decode(self, coded_bits):
        return self._xor_operation(coded_bits)

    def _xor_operation(self, bits):
        return [(bit ^ self.key[i % len(self.key)]) for i, bit in enumerate(bits)]
