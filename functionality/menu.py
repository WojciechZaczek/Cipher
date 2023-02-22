class Menu:
    """Class responsible for  menu content"""

    hello = "\nHello, this is Cipher program. It allows you to encode an decode text. You can write text or import it from file. Choose one option from menu below and press enter.\n"
    main_menu = "\nMENU:\n1. Select ROT\n2. Import text from a file\n3. Encrypt/Decrypt text\n4. Show buffer\n5. Delete text in buffer\n6. Exit program\n"
    bye = "Thank you! Goodbye!"
    question = "Excuse me?"
    rot = "Selected ROT: "

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

    @staticmethod
    def print_selected_rot(rot: str):
        print(f"{Menu.rot} {rot}")
