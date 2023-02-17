class Menu:
    """Class responsible for  menu content"""

    hello = "\nHello, this is Cipher program. It allows you to encode an decode text. You can write text or import it from file. Choose one option from menu below and press enter.\n"
    main_menu = "\nMENU:\n1. Import text from a file\n2. Write text\n3. Show buffer\n4. Delete text in buffer\n5. Exit program\n"
    bye = "Thank you! Goodbye!"
    question = "Excuse me?"

    @staticmethod
    def print_hello():
        """Displays a greeting"""
        print(Menu.hello)

    @staticmethod
    def print_menu():
        """Displays main menu"""
        print(Menu.main_menu)

    @staticmethod
    def print_bye():
        """Displays a goodbye"""
        print(Menu.bye)

    @staticmethod
    def print_question():
        """Displays a question"""
        print(Menu.question)
