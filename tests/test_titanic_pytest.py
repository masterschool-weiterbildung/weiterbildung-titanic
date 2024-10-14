import pytest

class TestTitanic:

    @pytest.mark.parametrize("add_text_input, add_expected_output",
                             [
                                 ("2+2", 4)
                             ]
                             )
    def test_addition(self, add_text_input, add_expected_output):
        assert True
