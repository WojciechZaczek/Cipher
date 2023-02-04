import datetime
from dataclasses import dataclass


@dataclass
class Text:  # new - whole class
    """Dataclass - Buffer class object information"""

    org_text: str
    mdf_text: str
    rot: str
    time: str
    mode: str

    def text_to_dct(self) -> dict:
        """Creates dicts with Text class instances"""
        return {
            "Original text": self.org_text,
            "Modified text": self.mdf_text,
            "Used Rot": self.rot,
            "Mode": self.mode,
            "Time": self.time,
        }


class Buffer:
    """Object of this class stores data"""

    def __init__(self) -> None:
        """Creates buffer"""

        self.buffer = []

    def __str__(self) -> str:
        """Prints buffer"""

        return f"{self.buffer}"

    def write_buffer(
        self, original: str, modified: str, rot: str, mode: str
    ) -> None:  # new - rot parametr and new is Text obj
        """Appends dict with text to Buffer object"""

        text = Text(
            org_text=original,
            mdf_text=modified,
            mode=mode,
            rot=rot,
            time=f"{datetime.datetime.now()}",
        )
        new = text.text_to_dct()
        self.buffer.append(new)

    def print_buffer(self) -> None:  # new way of print buffer
        """Prints information about stored data"""

        if not self.buffer:
            print("\nBuffer is empty!")
        else:
            if len(self.buffer) == 1:
                print(f"\nYou buffer has {len(self.buffer)} text message:")
            else:
                print(f"\nYou buffer has {len(self.buffer)} text messages:")
            n = 0
            for i in self.buffer:
                n += 1
                print(f"Text number {n}: {str(i)[1:-1]}")

    def delete_one_text(self, no: int) -> None:  # new
        """Deletes one element in Buffer object"""
        del self.buffer[no - 1]

    def clear_buffer(self) -> None:  # new
        """Deletes all elements in Buffer object"""

        self.buffer.clear()
