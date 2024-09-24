from .interfaces import ChannelCoder


class RepetitionCoder(ChannelCoder):
    def encode(self, data_bits):
        coded_bits = "".join([bit * 3 for bit in data_bits])
        return coded_bits

    def decode(self, coded_bits):
        bits = [coded_bits[i : i + 3] for i in range(0, len(coded_bits), 3)]
        decoded_bits = ""
        for triplet in bits:
            decoded_bits += max(set(triplet), key=triplet.count)
        return decoded_bits
