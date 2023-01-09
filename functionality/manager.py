from functionality.operations import Menu, Buffer


class Manager:
    def __init__(self):
        self.__is_running = True
        self.__options = {
            1: self.__end_program,
            2: self.__write_text,
            3: self.__end_program,
        }

    def run(self):
        Menu.print_hello()
        while self.__is_running:
            Menu.print_menu()
            user_instruction = int(input(""))
            self.__handle_instruction(user_instruction)
            print("\n")
            break

    def __handle_instruction(self, user_input):
        if user_input in self.__options:
            self.__options.get(user_input)()
        else:
            print(f"{user_input} is not a instruction")

    def __end_program(self):
        self.__is_running = False

    def __write_text(self):
        buffer = Buffer("")
        Buffer.write_buffer(buffer)
        print(buffer.text)
        Menu.decrypt_encrypt_menu()
