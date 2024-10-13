import pytest

from titanic.print_utilities import print_introduction


class TestTitanic:

    @pytest.mark.parametrize("add_text_input, add_expected_output",
                             [
                                 ("2+2", 4)
                             ]
                             )
    def test_addition(self, add_text_input, add_expected_output):
        assert True

    @pytest.mark.parametrize("text_to_print",
                             [
                                 "Welcome to the Ships CLI! Enter 'help' to view available commands."
                             ]
                             )
    def test_subtraction(self, text_to_print):
        assert print_introduction(text_to_print) == "Welcome to the Ships CLI! Enter 'help' to view available commands."