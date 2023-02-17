from typing import Callable
from functionality.buffer import Buffer
from functionality.menu import Menu
from functionality.rot import RotFactory
from functionality.filehandler import Filehandler


class Manager:

    Menu.print_hello()  # new- wrzucilem z powrotem  bo w self.print_buffer musiałem wrzucic self.run, inaczej przechodzil do self.writetext. To samo dzialo sie przy Buffer.peak_buffer

    def __init__(self) -> None:
        self.__is_running = True
        self.buffer = Buffer()
        self.original_text = ""
        self.rot_text = ""
        self.shift = ""
        self.__main_options = {
            1: self.__upload_file,
            2: self.__write_text,
            3: self.print_buffer,
            4: self.delete_text_in_buffer,
            5: self.__end_program,
        }

    def run(self) -> None:
        """Starts program"""

        while self.__is_running:
            print(
                self.__handle_instruction(
                    self.get_user_instruction(), self.__main_options
                )
            )
            print(f"\nYour text is: {self.original_text}")
            self.get_rot_text()
            print(self.rot_text)
            self.__save_text_in_buffer()

    def print_buffer(
        self,
    ):  # zmieniłem z Buffer.peak_buffer bo wyglada wtedy ladniej -> Buffer__str__
        print(self.buffer)
        self.run()

    def get_user_instruction(self) -> int:
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
        choice = input(prompt)
        while choice not in valid_options:
            choice = input(f"Invalid option. {prompt}")
        return choice

    @staticmethod
    def __handle_instruction(user_input: int | str, menu: dict[int, Callable]) -> str:
        """Allows user to choose option from menu"""
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

    def delete_text_in_buffer(self) -> None:  # new
        """Allows user to delete one text in buffer or clear buffer"""
        choice = self.get_valid_input(
            "Do you want to delete all text messages or just one(all/one)?: ",
            ["all", "one"],
        )
        if choice == "all":
            self.buffer.clear()
            self.print_buffer()  # new: zamienilem na print_buffer: przy Buffer.peak_buffer pokazywalo tylko pusta liste i nie wracalo do MENU

        elif choice == "one":
            self.__delete_only_one_text_in_buffer()
            self.print_buffer()  # new: zamienilem na print_buffer: przy Buffer.peak_buffer pokazywalo tylko pusta liste i nie wracalo do MENU

    def __write_text(self) -> None:
        """Allows user write text"""
        self.original_text = input("Write your text: ")

    def __upload_file(self) -> None:
        """Allows user to upload text from file"""

        self.original_text = Filehandler.open_file()

    def get_rot_text(self) -> None:
        self.shift = self.get_valid_input(
            "Which rot would you like to use (rot13 or rot47): ", ["rot13", "rot47"]
        )
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
                self.original_text, self.rot_text, mode=mode, rot=self.shift
            )
            print("Text saved in buffer")
            print(self.buffer)
            self.__write_another_text()
        elif choice == "N":
            self.run()

    def __write_another_text(self) -> None:  # new
        """Allows user to go to main menu and write another text"""

        choice = self.get_valid_input(
            "Would you like to write another one and go back to main menu?(Y/N)?: ",
            ["Y", "N"],
        )
        if choice == "Y":
            self.run()
        elif choice == "N":
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
                Filehandler.write_line(
                    self.buffer.get_data, name + ".json"
                )  # new @property get/setter
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
