from .interfaces import ChannelCoder


class XORCoder(ChannelCoder):
    def encode(self, data_bits):
        return data_bits

    def decode(self, coded_bits):
        return coded_bits
