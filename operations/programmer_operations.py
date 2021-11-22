from abc import ABC, abstractmethod


class IProgrammerCalci(ABC):

    @abstractmethod
    def convert_hex_to_binary(self, input):
        pass

    @abstractmethod
    def convert_binary_to_hex(self, input):
        pass