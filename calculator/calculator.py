"""Calculator program """
class Calculator:
    """Class with arithematic operations """
    output = 0
    

    def addition(self, num_1, num_2):
        """Perform addition operation on num_1 and num_2"""
        self.output = float(num_1) + float(num_2)
        print('The result of addition is ', str(self.output))

        return self.output

    def subtraction(self, num_1, num_2):
        """Perform subtraction operation on num_! and num_2 """
        self.output = float(num_1) - float(num_2)
        print('The result of subtraction is ', str(self.output))

        return self.output

    def division(self, num_1, num_2):
        """Perform division operation on num_1 and num_2"""
        # if b == 0:
        try:
            self.output = float(num_1) / float(num_2)
            print('The result of division is ', str(self.output))

            return self.output
        except ZeroDivisionError as ex_div:
            print('The result of division is ', 'invalid input')


    def multiplication(self, num_1, num_2):
        """Perform multiplication operation on a and b """
        self.output = float(num_1) * float(num_2)
        print('The result of multiplication is ', str(self.output))

        return self.output
