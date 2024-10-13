import pytest

from my_package.calculator import calculate


class TestCalculator:

    @pytest.mark.parametrize("add_text_input, add_expected_output",
                             [
                                 ("2+2", 4),
                                 ("4+1", 5),
                                 ("9+7", 16)
                             ]
                             )
    def test_addition(self, add_text_input, add_expected_output):
        assert calculate(add_text_input) == add_expected_output

    @pytest.mark.parametrize("subtract_text_input, subtract_expected_output",
                             [
                                 ("4-1", 3),
                                 ("5-1", 4)
                             ]
                             )
    def test_subtraction(self, subtract_text_input, subtract_expected_output):
        assert calculate(subtract_text_input) == subtract_expected_output

    @pytest.mark.parametrize("multiply_text_input, multiply_expected_output",
                             [
                                 ("1*1", 1),
                                 ("3*3", 9)
                             ]
                             )
    def test_multiplication(self, multiply_text_input,
                            multiply_expected_output):
        assert calculate(multiply_text_input) == multiply_expected_output

    @pytest.mark.parametrize("divide_text_input, divide_expected_output",
                             [
                                 ("9/3", 3.0),
                                 ("8/2", 4.0)
                             ]
                             )
    def test_division(self, divide_text_input, divide_expected_output):
        assert calculate(divide_text_input) == divide_expected_output

    @pytest.mark.parametrize("remainder_text_input, remainder_expected_output",
                             [
                                 ("6~3", (2, 0)),
                                 ("7~3", (2, 1))
                             ]
                             )
    def test_division_remainder(self, remainder_text_input,
                                remainder_expected_output):
        assert calculate(remainder_text_input) == remainder_expected_output
