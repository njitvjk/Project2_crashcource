from abc import abstractmethod, ABC


class CalculationHistory(ABC):
    calculation_history = []

    @abstractmethod
    def append_calculation_to_history(self):
        """ Task 5: add calculation to history"""
        pass

    @staticmethod
    def get_history():
        """ Task 1:get history"""
        return CalculationHistory.calculation_history[-1]
        # return Calculator.history[-1].get_output()

    @staticmethod
    def get_result_of_first_calculation():
        """ Task 2: Get first calculation result"""
        return CalculationHistory.calculation_history[0]

    @staticmethod
    def clear_history():
        """ Task 3: clear history"""
        CalculationHistory.calculation_history.clear()
        return True

    @staticmethod
    def history_count():
        """ Task 4: count history"""
        return len(CalculationHistory.calculation_history)

    @staticmethod
    def get_result_of_last_calculation():
        """ Task 6: Get last calculation result"""
        return CalculationHistory.calculation_history[-1]
