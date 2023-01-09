import string


class Menu:
    """Class responsible for  menu content"""

    @staticmethod
    def print_hello():
        """Displays a greeting"""
        print(
            "\nHello, this is Cipher program. It allows you to encode an decode text. You can write text or import it from file. Choose one option from menu below and press enter.\n"
        )

    @staticmethod
    def print_menu():
        """Displays main menu"""
        print(
            "MENU:\n1. Import text from a file\n2. Write text\n3. Exit program\n\nChoose one option from menu below and press enter:"
        )

    @staticmethod
    def print_decrypt_encrypt_menu():
        """Displays mode menu encrypt/decrypt"""
        print(
            f"What do you want to do with text? Please choose one option from menu below and press enter:\n1. Encrypt\n2. Decrypt\n3. Go back to main menu\n4. Exit program"
        )

    @staticmethod
    def print_rot13_rot47_menu():
        """Displays mode menu Rot13/Rot47"""
        print(
            "Which cipher  would youlike to use? Please choose one option from menu below and press enter:\n1. Rot13\n2. Rot47\n3. Go back to main menu\n4. Exit program"
        )

    @staticmethod
    def print_save_options():
        """Displays save options"""
        print(
            "Would you like to save this text? Please choose one option from menu below and press enter:\n1. Yes - create new file\n2. Yes - upload to file \n3. No - bo back to main menu\n No - exit program"
        )

    @staticmethod
    def print_file_path():
        """Displays question about file path"""
        print("Please write a file path: ")

    @staticmethod
    def print_file_name():
        """Displays question about file name"""
        print("Please write a file name: ")

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


class Buffer:
    """Class responsible provide string that program will work on"""

    def __init__(self, text: str) -> None:
        self.text = text

    def __str__(self) -> str:
        return f"{self.text}"

    def write_buffer(self) -> str:
        """Method allows user to write string that program will work on"""
        self.text = input("Write text: ")
        return self.text

    def upload_buffer(self):
        """Uploads string from jons file"""
        pass


class Rot:
    """Abstract class - cipher constructor and methods"""

    def __init__(self, txt: str, key) -> None:
        self.txt = txt
        self.key = key

    def encrypt(self, symbols: str) -> str:
        """Abstract encrypt method"""
        encrypt_text = ""

        for l in self.txt:
            if l in symbols:
                l_index = symbols.find(l)
                encrypt_text_index = l_index + self.key
                if encrypt_text_index >= len(symbols):
                    encrypt_text_index -= len(symbols)
                encrypt_text += symbols[encrypt_text_index]
            else:
                encrypt_text += l
        return encrypt_text

    def decrypt(self, symbols: str) -> str:
        """Abstract decrypt method - constructor and methods"""
        decrypt_text = ""

        for l in self.txt:
            if l in symbols:

                l_index = symbols.find(l)

                decrypt_text_index = l_index - self.key
                if decrypt_text_index < 0:
                    decrypt_text_index += len(symbols)
                decrypt_text += symbols[decrypt_text_index]
            else:
                decrypt_text += l
        return decrypt_text


class Rot13(Rot):
    """Rot 13 cipher class, - constructor and methods. Rot subclass"""

    def __init__(self, txt: str, key=13) -> None:
        super().__init__(txt, key)

    def encrypt(
        self, symbols=string.ascii_lowercase * 2 + string.ascii_uppercase * 2
    ) -> str:
        """Rot 13 encrypt method"""

        return super().encrypt(symbols)

    def decrypt(self, symbols=""):
        """Rot 13 decrypt method"""
        decrypt_text = ""

        for l in self.txt:
            if l.isupper():
                symbols = 2 * string.ascii_uppercase
            elif l.islower():
                symbols = 2 * string.ascii_lowercase

            if l in symbols:
                l_index = symbols.find(l)
                decrypt_text_index = l_index - self.key
                if decrypt_text_index < 0:
                    decrypt_text_index += len(symbols)
                decrypt_text += symbols[decrypt_text_index]
            else:
                decrypt_text += l
        return decrypt_text


class Rot47(Rot):
    """Rot 47 cipher class, - constructor and methods. Rot subclass"""

    def __init__(self, txt: str, key=47) -> None:
        super().__init__(txt, key)

    def encrypt(self, symbols="") -> str:
        """Rot 47 encrypt method"""

        for i in range(33, 127):
            symbols += chr(i)
        return super().encrypt(symbols)

    def decrypt(self, symbols="") -> str:
        """Rot 13 decrypt method"""
        for i in range(33, 127):
            symbols += chr(i)
        return super().decrypt(symbols)


class Filehandler:
    pass
