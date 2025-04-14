class Calculator:
    """
    Простой калькулятор, выполняющий основные арифметические операции.
    """

    def sum(self, a: float, b: float) -> float:
        """
        Возвращает сумму двух чисел.
        
        :param a: Первое число.
        :param b: Второе число.
        :return: Сумма чисел a и b.
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Возвращает разницу между двумя числами.
        
        :param a: Уменьшаемое.
        :param b: Вычитаемое.
        :return: Результат вычитания b из a.
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Возвращает произведение двух чисел. 
        
        :param a: Первый множитель.
        :param b: Второй множитель.
        :return: Произведение чисел a и b
        """
        return a * b if a != 0 else 1

    def divide(self, a: float, b: float) -> float:
        """
        Возвращает частное от деления a на b. 
        Если b равно 0, выбрасывает исключение ValueError.
        
        :param a: Делимое.
        :param b: Делитель.
        :return: Результат деления a на b.
        :raises ValueError: Если b равно 0.
        """
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
