from abc import ABC, abstractmethod


class ITrigonometryCalci(ABC):

    @abstractmethod
    def sin_of(self, x):
        pass

    @abstractmethod
    def cos_of(self, x):
        pass

    @abstractmethod
    def tan_of(self, x):
        pass