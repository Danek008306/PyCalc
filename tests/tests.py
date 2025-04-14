import pytest
from src.calc import Calculator

@pytest.fixture
def calculator():
    """Фикстура для создания экземпляра калькулятора."""
    return Calculator()

# Параметризованный тест для метода сложения
@pytest.mark.parametrize("a, b, expected", [
    # Базовый случай положительных чисел
    (3, 5, 8),
    # Отрицательные числа
    (-2, 7, 5),
    # Нули
    (0, 0, 0),
    # Смешанные знаки
    (-5, 10, 5)
])
def test_sum(calculator, a, b, expected):
    result = calculator.sum(a, b)
    assert result == expected, f"Сложение {a} + {b} должно давать {expected}, получено {result}"

# Параметризованный тест для метода вычитания
@pytest.mark.parametrize("a, b, expected", [
    # Простое вычитание
    (10, 5, 5),
    # Отрицательное число
    (-10, -15, 5),
    # Числа одинакового знака
    (20, 10, 10),
    # Число минус себя
    (10, 10, 0)
])
def test_subtract(calculator, a, b, expected):
    result = calculator.subtract(a, b)
    assert result == expected, f"Вычитание {a} - {b} должно давать {expected}, получено {result}"

# Параметризованный тест для метода умножения
@pytest.mark.parametrize("a, b, expected", [
    # Положительные числа
    (2, 3, 6),
    # Отрицательные числа
    (-5, 7, -35),
    # Умножение нуля
    (0, 10, 0),
    # Произведение двух больших чисел
    (1000, 1000, 1000000)
])
def test_multiply(calculator, a, b, expected):
    result = calculator.multiply(a, b)
    assert result == expected, f"Умножение {a} * {b} должно давать {expected}, получено {result}"

# Параметризованный тест для метода деления
@pytest.mark.parametrize("a, b, expected", [
    # Деление целых чисел
    (10, 2, 5),
    # Деление отрицательных чисел
    (-10, -2, 5),
    # Деление на единицу
    (100, 1, 100),
    # Дробное деление
    (9, 3, 3)
], ids=["int_division", "negatives", "divide_by_one", "fractional"])
def test_divide(calculator, a, b, expected):
    result = calculator.divide(a, b)
    assert result == expected, f"Деление {a} / {b} должно давать {expected}, получено {result}"

# Специальный тест на исключение при делении на ноль
def test_divide_by_zero_raises_exception(calculator):
    with pytest.raises(ValueError):
        calculator.divide(10, 0)