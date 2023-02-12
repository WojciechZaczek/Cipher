from typing import Callable
from functionality.buffer import Buffer
from functionality.menu import Menu
from functionality.rot import RotFactory
from functionality.filehandler import Filehandler
from utils import BufferUtils


class Manager:
    Menu.print_hello()

    def __init__(self) -> None:
        self.__is_running = True
        self.buffer = Buffer()
        self.original_text = ""
        self.rot_text = ""
        self.__main_options = {
            1: self.__upload_file,
            2: self.__write_text,
            3: self.__show_buffer,  # new
            4: self.__delete_text_in_buffer,  # new
            5: self.__end_program,
        }

    def run(self) -> None:
        """Starts program"""

        while self.__is_running:
            Menu.print_menu()
            user_instruction = int(input(""))
            self.__handle_instruction(user_instruction, self.__main_options)
            print(f"\nYour text is: {self.original_text}")
            self.__rot_use()
            print(self.rot_text)
            self.__save_text_in_buffer()
            break

    @staticmethod
    def __handle_instruction(user_input: int | str, menu: dict[int, Callable]) -> None:
        """Allows user to choose option from menu"""

        if user_input in menu:
            menu.get(user_input)()
        else:
            print(f"{user_input} is not a instruction")

    def __end_program(self) -> None:
        """ "Stops program"""

        Menu.print_bye()
        self.__is_running = False
        exit()

    def __show_buffer(self) -> None:
        """Prints buffer"""
        print(self.buffer)
        self.run()

    def __delete_text_in_buffer(self) -> None:  # new
        """Allows user to delete one text in buffer or clear buffer"""

        choice = input(
            "Do you want to delete all text messages or just one(all/one)?: "
        )
        while choice not in ["all", "one"]:
            choice = input(
                "Do you want to delete all text messages or just one(all/one)?: "
            )
        match choice:
            case "all":
                BufferUtils.clear_buffer(self.buffer)
                self.__show_buffer()
            case "one":
                BufferUtils.delete_only_one_text_in_buffer(self.buffer)
                self.__show_buffer()

    def __write_text(self) -> None:
        """Allows user write text"""

        self.original_text = input("Write your text: ")

    def __upload_file(self) -> None:
        """Allows user to upload text from file"""

        self.original_text = Filehandler.open_file()

    def __rot_use(self) -> None:
        """Applies selected cipher to the text"""

        self.shift = input("Which rot would you like to use (rot13 or rot47): ")
        match self.shift:
            case "rot13" | "Rot13" | "rot 13" | "Rot 13" | "rot_13" | "Rot_13" | "13":
                new = RotFactory.get_rot("rot13", self.original_text)
                self.rot_text = new.use_rot()

            case "rot47" | "Rot47" | "rot 47" | "Rot 47" | "rot_47" | "Rot_47" | "47":
                new = RotFactory.get_rot("rot47", self.original_text)
                self.rot_text = new.use_rot()

            case _:
                Menu.print_question()
                self.__rot_use()

    def __save_text_in_buffer(self) -> None:
        """Allows user to save text and modified text in buffer. Text is saved as dict with date and selected mode"""

        choice = input("Would you like to save text in buffer (Y/N): ")
        match choice:
            case "Y" | "y" | "Yes":
                mode = ""
                while mode not in ["encrypt", "decrypt"]:
                    mode = input("Write mode(encrypt/decrypt): ")
                self.buffer.write(
                    self.original_text, self.rot_text, mode=mode, rot=self.shift
                )
                print("Text saved in buffer")
                print(self.buffer)
                self.__write_another_text()
            case "N" | "n" | "No":
                self.run()
            case _:
                Menu.print_question()
                self.__save_text_in_buffer()

    def __write_another_text(self) -> None:
        """Allows user to go to main menu and write another text"""

        choice = input(
            "Would you like to write another one and go back to main menu?(Y/N)?: "
        )
        match choice:
            case "Y" | "y" | "Yes":
                self.run()

            case "N" | "n" | "No":
                self.__save_buffer_in_file()

            case _:
                Menu.print_question()
                self.__write_another_text()

    def __save_buffer_in_file(self) -> None:
        """Allows user to save buffer in json file. User can create new file or upload file"""

        choice = input("Would you like to save buffer in file (Y/N)?: ")
        match choice:
            case "Y" | "y" | "Yes":
                create_or_upload = input(
                    "Would you like create a new file or upload (create/upload)?: "
                )
                match create_or_upload:
                    case "Create" | "create" | "c":
                        name = input("Write file name: ")

                        Filehandler.write_line(self.buffer.buffer, name + ".json")
                        print(f"Buffer saved in file {name}.json")
                        self.run()
                    case "Upload" | "upload" | "u":
                        path = input("Write a path: ")
                        Filehandler.write_line(self.buffer.buffer, path)
                        print(f"Buffer saved")
                        self.run()

                    case _:
                        Menu.print_question()
                        self.__save_buffer_in_file()

            case "N" | "n" | "No":
                self.run()

            case _:
                Menu.print_question()
                self.__save_buffer_in_file()
