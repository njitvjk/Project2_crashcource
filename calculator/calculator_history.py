from abc import abstractmethod


class CalculatorHistory():
    calculation_history = []


def get_history_list(calculation_history=None):
    return calculation_history


def display_history(calculation_history=None):
    return calculation_history[-1]

@abstractmethod
def clear_calculator(self):
    pass


@abstractmethod
def add_to_history():
    pass
