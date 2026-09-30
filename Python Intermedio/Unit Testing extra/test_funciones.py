from Funciones_test import add_numbers, calculate_average, celsius_to_fahrenheit


class TestNumbers:

    def test_positive_numbers(self):
        assert add_numbers(5, 10) == 15
        assert calculate_average(5, 10, 15) == 10
        assert celsius_to_fahrenheit(10) == 50

    def test_negative_numbers(self):
        assert add_numbers(-5, -10) == -15
        assert calculate_average(-5, -10, -15) == -10
        assert celsius_to_fahrenheit(-10) == 14

    def test_zero_numbers(self):
        assert add_numbers(0, 0) == 0
        assert calculate_average(0, 0, 0) == 0
        assert celsius_to_fahrenheit(0) == 32