from functionality.manager import Manager
from unittest.mock import patch, call


class TestManager:
    def setup_method(self):
        self.manager = Manager()

    # def test_write_text_method(self): # Todo
    #     mock_args = ['test', 'ppp']
    #     with patch('builtins.input', side_effect=mock_args):
    #         self.manager._Manager__write_text()
    #
    #     assert self.manager.original_text == mock_args[0]
