import pytest
from functionality.menu import Menu


class TestMenu:
    def setup(self):
        self.hello = "\nHello, this is Cipher program. It allows you to encode an decode text. You can write text or import it from file. Choose one option from menu below and press enter.\n"
        self.main_menu = "\nMENU:\n1. Import text from a file\n2. Write text\n3. Exit program\n\nChoose one option from menu below and press enter: "
        self.bye = "Thank you! Goodbye!"
        self.question = "Excuse me?"

    def test_print_hello(self):
        expected = print(self.hello)
        assert Menu.print_hello() == expected

    def test_print_main_menu(self):
        expected = print(self.main_menu)
        assert Menu.print_menu() == expected

    def test_print_bye(self):
        expected = print(self.bye)
        assert Menu.print_bye() == expected

    def test_print_question(self):
        expected = print(self.question)
        assert Menu.print_question() == expected
