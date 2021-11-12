"""Parent Class"""
class Calculation:
    """Constructor and class method """
    #Initialization
    # pylint: disable=too-few-public-methods
    def __init__(self,value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b
    #Factory
    @classmethod
    def create(cls, value_a, value_b):
        """class method returns the class """
        return cls(value_a,value_b)
