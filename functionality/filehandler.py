import json


class Filehandler:
    """Class responsible for operation on files"""

    @staticmethod
    def open_file() -> str | None:
        """Opens json file"""

        try:
            path: str = input("Write a path:")
            with open(path) as json_file:
                file = json.load(json_file)
            return file
        except OSError as error:
            print(error)
            print("")

    @staticmethod
    def create_file() -> None:
        """Creates json file"""

        data = dict()
        with open("sample.json", "a") as outfile:
            json.dump(data, outfile)

    @staticmethod
    def write_line(text, path=None) -> None:
        """Writes text in json file"""

        if not path:
            path = "rot_data.json"

        with open(path, "a") as outfile:
            json.dump(text, outfile)
        print(path)
