"""Calculator program """

class Calculator:
    """Class with arithematic operations """
    output=0
    def addition(self, num_1:int, num_2:int):
        """Perform addition operation on num_1 and num_2"""
        self.output=num_1+num_2
        return self.output
    def subtraction(self, num_1:int, num_2:int):
        """Perform subtraction operation on num_! and num_2 """
        self.output = num_1 - num_2
        return self.output
    def division(self, num_1:int, num_2:int):
        """Perform division operation on num_1 and num_2"""
        #if b == 0:
        try:
            self.output = num_1/num_2
            return self.output
        except ZeroDivisionError as ex_div:
            return ex_div

    def multiplication(self, num_1:int, num_2:int):
        """Perform multiplication operation on a and b """
        self.output = num_1 *num_2
        return self.output
