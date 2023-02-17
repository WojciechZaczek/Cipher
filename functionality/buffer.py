import datetime
from dataclasses import dataclass


@dataclass
class Text:
    """Dataclass - Buffer class object information"""

    org_text: str
    mdf_text: str
    rot: str
    mode: str
    time: datetime = datetime.datetime.now()

    def to_dct(self) -> dict[str, str | datetime.datetime]:
        """Creates dicts with Text class instances"""
        return {
            "Original text": self.org_text,
            "Modified text": self.mdf_text,
            "Used Rot": self.rot,
            "Mode": self.mode,
            "Time": self.time,
        }

    def __str__(self):
        return f"Text: {self.mdf_text}, Mode: {self.mode}, Used Rot: {self.rot}, Time {self.time}"


class Buffer:
    """Object of this class stores data"""

    def __init__(self) -> None:
        self.__data: list[Text] = []

    @property
    def get_data(self):
        return self.__data

    @get_data.setter
    def get_data(self, value):
        self.__data = value

    def __str__(self) -> str:
        """Prints buffer"""
        if not self.__data:
            return "\nBuffer is empty!"
        if len(self.__data) == 1:
            body = f"\nYou buffer has {len(self.__data)} text message:\n"
        else:
            body = f"\nYou buffer has {len(self.__data)} text messages:\n"

        arr = [(idx, str(text)) for idx, text in enumerate(self.__data, start=1)]
        for idx, text in arr:
            body += f"{idx}. {text}\n"
        return body

    def write(
        self, original: str, modified: str, rot: str, mode: str
    ) -> None:  # new - rot parameter and new is Text obj
        """Appends dict with text to Buffer object"""

        text = Text(
            org_text=original,
            mdf_text=modified,
            mode=mode,
            rot=rot,
        )
        self.__data.append(text)

    def delete_one_text(self, no: int) -> None:  # new
        """Deletes one element in Buffer object"""
        del self.__data[no - 1]

    def clear(self) -> None:  # new
        """Deletes all elements in Buffer object"""
        self.__data.clear()

    def peak_buffer(self):
        print(self.__data)
