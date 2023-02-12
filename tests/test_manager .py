from functionality.manager import Manager
from unittest.mock import patch, call
from functionality.buffer import Buffer


class TestManager:
    def setup_method(self):
        self.manager = Manager()

    def test_write_text_method(self):  # Todo
        mock_args = ["test", "ppp"]
        with patch("builtins.input", side_effect=mock_args):
            self.manager._Manager__write_text()

        assert self.manager.original_text == mock_args[0]

    def test_write_another_text(self):  # Todo
        mock_args = ["y"]
        with patch("builtins.input", side_effect=mock_args):
            self.manager._Manager__write_another_text()
            assert self.manager.__write_another_text == self.manager.run()
