from functionality.buffer import Buffer
from functionality.menu import Menu
from functionality.rot import Rot, Rot47, RotFactory, Rot13
from functionality.filehandler import Filehandler


class Manager:
    Menu.print_hello()

    def __init__(self):
        self.__is_running = True
        self.buffer = Buffer([])
        self.original_text = ""
        self.rot_text = ""
        self.__main_options = {
            1: self.__upload_file,
            2: self.__write_text,
            3: self.__end_program,
        }

    def run(self):

        while self.__is_running:
            Menu.print_menu()
            user_instruction = int(input(""))
            self.__handle_instruction(user_instruction, self.__main_options)
            print(f"\nYour text is: {self.original_text}")
            self.__rot_use()
            print(self.rot_text)
            self.__save_text_in_buffer()

            break

    def __handle_instruction(self, user_input, menu):
        if user_input in menu:
            menu.get(user_input)()
        else:
            print(f"{user_input} is not a instruction")

    def __end_program(self):
        Menu.print_bye()
        self.__is_running = False
        exit()

    def __write_text(self):
        self.original_text = input("Write your text: ")
        return self.original_text
        # {'text': 'djr', 'rot_type': 'rot13', 'status': 'encrypted'}

    def __upload_file(self):
        self.original_text = Filehandler.open_file()
        return self.original_text

    def __rot_use(self):
        shift = input("Which rot would you like to use(rot13 or rot47): ")
        match shift:
            case "rot13" | "Rot13" | "rot 13" | "Rot 13" | "rot_13" | "Rot_13" | "13":
                new = RotFactory.get_rot("rot13", self.original_text)
                self.rot_text = new.use_rot()

            case "rot47" | "Rot47" | "rot 47" | "Rot 47" | "rot_47" | "Rot_47" | "47":
                new = RotFactory.get_rot("rot47", self.original_text)
                self.rot_text = new.use_rot()

            case _:
                print("Excuse me?")
                return self.__rot_use()

    def __save_text_in_buffer(self):
        choice = input("Would you like to save text in buffer (Y/N): ")
        match choice:
            case "Y" | "y" | "Yes":
                self.buffer.write_buffer(self.original_text, self.rot_text)
                print(self.buffer)
                # self.save_buffer

            case "N" | "n" | "No":
                return self.run()
            case _:
                print("Excuse me?")
                return self.__save_text_in_buffer()

    def __save_buffer_in_file(self):
        pass
