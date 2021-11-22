from abc import ABC, abstractmethod


class ICommonCalci(ABC):
    @abstractmethod
    def clear_calculator(self):
        pass

