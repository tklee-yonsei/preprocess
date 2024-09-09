from abc import ABC, abstractmethod

class PreprocessorInterface(ABC):
    @abstractmethod
    def normalize(self, signal):
        pass

    @abstractmethod
    def filter(self, signal, filter_type, cutoff_frequency):
        pass