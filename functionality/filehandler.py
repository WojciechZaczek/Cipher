import json


class Filehandler:
    """Class responsible for operation on files"""

    @staticmethod
    def open_file():
        try:
            x = input("Write a path:")
            with open(x) as json_file:
                file = json.load(json_file)
            return file
        except OSError as error:
            print(error)
            print("")

    @staticmethod
    def create_file():
        data = {""}
        with open("sample.json", "a") as outfile:
            json.dump(data, outfile)

    @staticmethod
    def write_line(text: list, path=None):
        if path is None:
            path = "rot_data.json"

        with open(path, "a") as outfile:
            json.dump(text, outfile)
        print(path)
