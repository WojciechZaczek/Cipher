from functionality.manager import Manager
from unittest.mock import patch, call
from functionality.buffer import Buffer


class TestManager:
    def setup_method(self):
        self.manager = Manager()

    def test_write_text_method(self):
        mock_args = ["test", "ppp"]
        with patch("builtins.input", side_effect=mock_args):
            self.manager._Manager__write_text()

        assert self.manager.original_text == mock_args[0]

    def test_get_valid_input_choice_in_prompt(self):  # new
        mock_arg = ["passed"]

        with patch("builtins.input", side_effect=mock_arg):
            test = self.manager.get_valid_input("Test passed?", ["passed"])

        assert test == mock_arg[0]

    def test_get_user_instruction(self):  # new
        mock_arg = ["1"]
        with patch("builtins.input", side_effect=mock_arg):
            test = self.manager.get_user_instruction()

        assert test == 1

    def test_handle_instruction(self):  # new

        menu = {1: "A", 2: "B", 3: "C"}
        test = self.manager._Manager__handle_instruction(4, menu)

        assert test == f"{4} is not a instruction"

    def test_delete_only_one_text(self):
        self.manager.buffer.get_data = ["A", "B", "C"]
        expected = ["A", "C"]
        mock_arg = ["2"]
        with patch("builtins.input", side_effect=mock_arg):
            self.manager._Manager__delete_only_one_text_in_buffer()

        assert self.manager.buffer.get_data == expected
