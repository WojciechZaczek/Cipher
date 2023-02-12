from functionality.menu import Menu
from functionality.filehandler import Filehandler


from typing import Callable


class BufferUtils:
    @staticmethod
    def delete_only_one_text_in_buffer(obj) -> None:  # new
        """Deletes one text in obj"""

        print(obj)
        no = int(input("Please write number of text you would like to delete: "))
        while 1 > no > len(obj.buffer):
            Menu.print_question()
            no = int(input("Please write number of text you would like to delete: "))
        obj.delete_one_text(no)
        print("\nText has been deleted!")

    @staticmethod
    def clear_buffer(obj) -> None:
        """Deletes all text in obj"""

        obj.clear()
