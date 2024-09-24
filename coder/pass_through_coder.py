from .interfaces import ChannelCoder


class PassThroughCoder(ChannelCoder):
    def encode(self, data_bits):
        return data_bits

    def decode(self, coded_bits):
        return coded_bits
