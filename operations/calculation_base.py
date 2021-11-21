"""Parent Class"""
class Calculation:
    """Constructor and class method """
    #Initialization
    # pylint: disable=too-few-public-methods
    def __init__(self,value_a, value_b):
        self._value_a = value_a     #protected variable
        self._value_b = value_b     #protected_variable

    def get_value_a(self):
        print(self._value_a)
        return self._value_a

    def get_value_b(self):
        print(self._value_b)
        return self._value_b

    def get_description(self):
        print("Variables Initialized ")


