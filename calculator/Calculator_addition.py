from calculator.Calculator_ISP import Calculator


class CalculatorAddition(Calculator):

    # Violates the Rule- argument mismatch
    def cal_add(self, *nums):
        result = sum(nums)
        # self.add_to_history(result)
        return result
        # Violates the Rule- argument mismatch

    # Violates the Rule-type mismatch
    def cal_add(self, a, b):
        result = a + b
        # self.add_to_history(result)
        return float(result)

    #alternate way
    def cal_multiple_numbers(self, *nums):
        result = 0
        for result in nums:
            result = sum(nums)
        # self.add_to_history(result)
        return result

