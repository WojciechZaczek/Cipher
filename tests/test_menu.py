from unittest.mock import patch, call
from functionality.menu import Menu


class TestMenu:
    @patch("builtins.print")
    def test_print_hello(self, mocked_print):
        Menu.print_hello()
        assert mocked_print.mock_calls == [call(Menu.hello)]

    @patch("builtins.print")
    def test_print_main_menu(self, mocked_print):
        Menu.print_menu()
        assert mocked_print.mock_calls == [call(Menu.main_menu)]

    @patch("builtins.print")
    def test_print_bye(self, mocked_print):
        Menu.print_bye()
        assert mocked_print.mock_calls == [call(Menu.bye)]

    @patch("builtins.print")
    def test_print_question(self, mocked_print):
        Menu.print_question()
        assert mocked_print.mock_calls == [call(Menu.question)]
