from typing import Callable
from functionality.buffer import Buffer
from functionality.menu import Menu
from functionality.rot import RotFactory
from functionality.filehandler import Filehandler


class Manager:
    def __init__(self) -> None:
        self.__is_running = True
        self.buffer: Buffer = Buffer()
        self.original_text: str = ""
        self.rot_text: str = ""
        self.shift: str = ""
        self.selected_rot = None
        self.__main_options = {
            1: self.__set_rot,
            2: self.__upload_file,
            3: self.__encrypt_decrypt,
            4: self.buffer.peak_buffer,
            5: self.delete_text_in_buffer,
            6: self.__end_program,
        }

    def run(self) -> None:
        """Starts program"""
        Menu.print_hello()
        self.__set_rot()
        while self.__is_running:
            Menu.print_selected_rot(self.selected_rot)
            print(
                self.__handle_instruction(
                    self.get_user_instruction(), self.__main_options
                )
            )

    def __set_rot(self) -> None:
        """Sets self.selected_rot used in self run method"""

        self.selected_rot = self.__set_shift()

    def __set_shift(self) -> str:
        """Sets self shift which determines which cipher will be used"""

        self.shift = self.get_valid_input(
            "Which rot would you like to use (rot13 or rot47): ", ["rot13", "rot47"]
        )
        return self.shift

    def get_user_instruction(self) -> int:
        """Allows user to choose option from main menu"""

        Menu.print_menu()
        user_instruction = input("Choose one option from menu below and press enter:  ")
        try:
            user_instruction = int(user_instruction)
        except ValueError:
            print("Invalid input. Please enter a number")
            return self.get_user_instruction()
        return user_instruction

    @staticmethod
    def get_valid_input(prompt: str, valid_options: list) -> str:
        """Method determines the correct choices, used in other methods where user can choose or input option"""

        choice = input(prompt)
        while choice not in valid_options:
            choice = input(f"Invalid option. {prompt}")
        return choice

    @staticmethod
    def __handle_instruction(user_input: int | str, menu: dict[int, Callable]) -> str:
        """Allows user to choose option from menu - universal method"""

        if user_input in menu:
            menu.get(user_input)()
        else:
            return f"{user_input} is not a instruction"

    def __delete_only_one_text_in_buffer(self) -> None:
        """Deletes one text in obj"""

        print(self.buffer)
        no = int(input("Please write number of text you would like to delete: "))
        try:
            self.buffer.delete_one_text(no)

        except IndexError:
            self.__delete_only_one_text_in_buffer()

    def delete_text_in_buffer(self) -> None:
        """Allows user to delete one text in buffer or clear buffer"""

        choice = self.get_valid_input(
            "Do you want to delete all text messages or just one(all/one)?: ",
            ["all", "one"],
        )
        if choice == "all":
            self.buffer.clear()
            self.buffer.peak_buffer()

        elif choice == "one":
            self.__delete_only_one_text_in_buffer()
            self.buffer.peak_buffer()

    def __encrypt_decrypt(self) -> None:
        """Allows user write text"""

        self.original_text = input("Write your text: ")
        self.get_rot_text()
        print(f"\nYour text is: {self.original_text}")
        self.__save_text_in_buffer()

    def __upload_file(self) -> None:
        """Allows user to upload text from file"""

        self.original_text = Filehandler.open_file()

    def get_rot_text(self) -> None:
        """Encrypts/decrypts self.original_text using chosen rot"""
        rot = RotFactory.get_rot(self.shift, self.original_text)
        self.rot_text = rot.use_rot()

    def __save_text_in_buffer(self) -> None or str:
        """Allows user to save text and modified text in buffer. Text is saved as dict with date and selected mode"""

        choice = self.get_valid_input(
            "Would you like to save text in buffer (Y/N): ", ["Y", "N"]
        )
        if choice == "Y":
            mode = ""
            while mode not in ["encrypt", "decrypt"]:
                mode = input("Write mode(encrypt/decrypt): ")
            self.buffer.write(
                original=self.original_text,
                modified=self.rot_text,
                mode=mode,
                rot=self.shift,
            )
            print("Text saved in buffer")
            print(self.buffer.peak_buffer())
            self.__write_another_text()

    def __write_another_text(self) -> None:
        """Allows user to go to main menu and write another text"""

        choice = self.get_valid_input(
            "Would you like return to main menu to write another text?(Y/N)?: ",
            ["Y", "N"],
        )
        if choice == "N":
            self.__save_buffer_in_file()

    def __save_buffer_in_file(self) -> None:
        """Allows user to save buffer in json file. User can create new file or upload file"""

        choice = self.get_valid_input(
            "Would you like to save buffer in file (Y/N)?: ", ["Y", "N"]
        )
        if choice == "Y":
            create_or_upload = self.get_valid_input(
                "Would you like create a new file or upload (create/upload)?: ",
                ["create", "upload"],
            )
            if create_or_upload == "create":
                name = input("Write file name: ")
                Filehandler.write_line(self.buffer.get_data, name + ".json")
                print(f"Buffer saved in file {name}.json")
            elif create_or_upload == "upload":
                path = input("Write a path: ")
                Filehandler.write_line(self.buffer.get_data, path)
                print(f"Buffer saved")

    def __end_program(self) -> None:
        """ "Stops program"""

        Menu.print_bye()
        self.__is_running = False
        exit()
