import datetime


class Buffer:
    """Class responsible for providing string that program will work on"""

    def __init__(self, buffer: list) -> None:
        self.buffer = buffer

    def __str__(self):
        return f"{self.buffer}"

    def write_buffer(self, original: str, modified: str):

        mode = input("Write mode(encrypt/decrypt): ")
        now = f"{datetime.datetime.now()}"
        new = {
            "Original text": original,
            "Modified text": modified,
            "Time": now,
            "Mode": mode,
        }
        self.buffer.append(new)
        return self.buffer
