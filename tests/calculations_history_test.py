"""Testing the Calculator"""
import pytest
from history.calculations import Calculations
from operations.addition import Addition

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
@pytest.fixture
def setup_addition_calculation_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    addition = Addition(values)
    Calculations.add_calculation(addition)

def test_add_calculation_to_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.history_count() == 1

def test_clear_calculation_history(clear_history_fixture, setup_addition_calculation_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.history_count() == 1
    Calculations.clear_history()
    assert Calculations.history_count() == 0
    assert Calculations.clear_history() == True

def test_get_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(0).get_output() == 3

def test_get_calc_last_result_value(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_result_of_last_calculation() == 3
def test_get_calculation_first(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the first calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation().get_output() == 3
def test_get_calc_first_result_value(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the first calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_result_of_first_calculation() == 3
def test_history_count(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.history_count() == 1
def test_get_calc_last_result_object(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    #This test if it returns the last calculation as an object
    assert isinstance(Calculations.get_last_calculation(), Addition)
