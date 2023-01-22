class Menu:
    """Class responsible for  menu content"""

    HELLO = "\nHello, this is Cipher program. It allows you to encode an decode text. You can write text or import it from file. Choose one option from menu below and press enter.\n"

    @staticmethod
    def print_hello():
        """Displays a greeting"""
        print(Menu.HELLO)

    @staticmethod
    def print_menu():
        """Displays main menu"""
        print(
            "\nMENU:\n1. Import text from a file\n2. Write text\n3. Exit program\n\nChoose one option from menu below and press enter:"
        )

    @staticmethod
    def print_decrypt_encrypt_menu_Rot13():
        """Displays mode menu encrypt/decrypt"""
        print(
            f"Cipher Rot 13:\nWhat do you want to do with text? Please choose one option from menu below and press enter:\n1. Encrypt\n2. Decrypt\n3. Go back to main menu\n4. Exit program"
        )

    @staticmethod
    def print_decrypt_encrypt_menu_Rot47():
        """Displays mode menu encrypt/decrypt"""
        print(
            f"Cipher Rot 47:\nWhat do you want to do with text? Please choose one option from menu below and press enter:\n1. Encrypt\n2. Decrypt\n3. Go back to main menu\n4. Exit program"
        )

    @staticmethod
    def print_rot13_rot47_menu():
        """Displays mode menu Rot13/Rot47"""
        print(
            "Which cipher would youlike to use? Please choose one option from menu below and press enter:\n1. Rot13\n2. Rot47\n3. Go back to main menu\n4. Exit program"
        )

    @staticmethod
    def print_save_options():
        """Displays save options"""
        print(
            "Would you like to save this text? Please choose one option from menu below and press enter:\n1. Yes - create new file\n2. No - bo back to main menu\n3. No - exit program"
        )

    @staticmethod
    def print_file_path():
        """Displays question about file path"""
        print("Please write a file path and file name: ")

    @staticmethod
    def print_after_saving():
        """Displays question after saving file"""
        print(
            "File saved! Would you like to:\n1. Go back to main menu\n2. Exit program"
        )

    @staticmethod
    def print_bye():
        """Displays a goodbye"""
        print("Thank you! Goodbye!")
