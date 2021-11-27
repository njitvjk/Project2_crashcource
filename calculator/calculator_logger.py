import logging

from calculator.Calculator_ISP import Calculator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


class CalculatorLogger(Calculator):
    def __int__(self):
        super.__init__()

    logger = logging.getLogger('CalculatorAdvanced')

    def log_addition_calculation(self):
        result = self.cal_add(3, 4)
        print('The result of addition is ',str(result))
        self.logger.info('addition successful')


calc = CalculatorLogger()
calc.log_addition_calculation()
