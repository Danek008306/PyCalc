import pytest
from src.calc import Calculator
calc = Calculator()


@pytest.fixture
def calculator():
    """Фикстура для создания экземпляра калькулятора"""
    return Calculator()


# Тесты для метода sum
def test_sum_positive(calculator):
    assert calculator.sum(2, 3) == 5
    assert calculator.sum(10, 20) == 30
    assert calculator.sum(-5, 7) == 2


def test_subtract_positive(calculator):
    assert calculator.subtract(10, 5) == 5
    assert calculator.subtract(100, 50) == 50
    assert calculator.subtract(-10, -15) == 5


def test_multiply_positive(calculator):
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(10, 20) == 200
    assert calculator.multiply(-5, 7) == -35


def test_divide_positive(calculator):
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(100, 25) == 4
    assert calculator.divide(-10, -2) == 5


def test_divide_by_zero_raises_exception(calculator):
    with pytest.raises(ValueError):
        calculator.divide(10, 0)