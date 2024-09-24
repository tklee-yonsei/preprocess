from abc import ABC, abstractmethod

class ChannelCoder(ABC):
    @abstractmethod
    def encode(self, data_bits):
        pass

    @abstractmethod
    def decode(self, coded_bits):
        pass
