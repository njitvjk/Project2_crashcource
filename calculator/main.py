""" This is the increment function"""
class Calculator:
    """ This is the Calculator class"""

    output = 0
    def get_result(self):
        """ Get Result of Calculation"""
        return self.output

    def addition(self, num_x,num_y):
        """ adds x and y and stores the value in output"""
        #self.result = self.result + value_a
        self.output = num_x + num_y
        return self.output
    def subtraction(self,num_x,num_y):
        """ subtract y from x and stores the value in output """
        self.output = num_x - num_y
        return self.output
    def multiplication(self, num_x, num_y):
        """ multiply x and y and store the value in output"""
        self.output = num_x * num_y
        return self.output
    def division(self, num_x, num_y):
        """ divide two numbers and store the value in output,Exception handler for divide by zero"""
        try:
            self.output = num_x / num_y
            return self.output
        except ZeroDivisionError as division_exception:
            print("Exception:Invalid Input")
            return division_exception
