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

#Calculator from Console
calc = Calculator()

while True:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")

    choice = int(input("Select operation: "))
    " Make sure the user have entered the valid choice"
    if choice in (1, 2, 3, 4, 5):
        # first check whether user want to exit
        if choice == 5:
            break
        # if not exit then show user with choices and perform operation
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if choice == 1:
            print(num1, "+", num2, "=",Calculator.addition(Calculator,num1,num2))
        elif choice == 2:
            print(num1, "-", num2, "=", Calculator.subtraction(Calculator,num1,num2))
        elif choice == 3:
            print(num1, "*", num2, "=", Calculator.multiplication(Calculator,num1,num2))
        elif choice == 4:
            if num2==0:
                print(Calculator.division(Calculator,num1,num2))
            print(num1, "/", num2, "=",Calculator.division(Calculator,num1,num2))
    else:
        print("Invalid Input")
