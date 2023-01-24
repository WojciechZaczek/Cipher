import datetime


class Buffer:
    """Class responsible for providing string that program will work on"""

    def __init__(self, buffer: list) -> None:
        """Creates buffer"""
        self.buffer = buffer

    def __str__(self):
        """Prints buffer"""
        return f"{self.buffer}"

    def write_buffer(self, original: str, modified: str) -> None:
        """Appends dict with text to Buffer object"""

        mode = input("Write mode(encrypt/decrypt): ")
        now = f"{datetime.datetime.now()}"
        new = {
            "Original text": original,
            "Modified text": modified,
            "Time": now,
            "Mode": mode,
        }
        self.buffer.append(new)
        # return self.buffer
