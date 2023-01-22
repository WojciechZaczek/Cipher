import string


class RotFactory:
    """Abstract class - RotFactory"""

    @classmethod
    def get_rot(cls, shift: str, text: str):
        if shift == "rot47":
            return Rot47(text)
        elif shift == "rot13":
            return Rot13(text)


class Rot:
    """Cipher constructor and methods"""

    def __init__(self, text: str, key) -> None:
        self.text = text
        self.key = key

    def use_rot(self, symbols: str) -> str:
        """Abstract encrypt method"""

        encrypt_text = ""
        for l in self.text:
            if l in symbols:
                l_index = symbols.find(l)
                encrypt_text_index = l_index + self.key
                if encrypt_text_index >= len(symbols):
                    encrypt_text_index -= len(symbols)
                encrypt_text += symbols[encrypt_text_index]
            else:
                encrypt_text += l
        return encrypt_text


class Rot13(Rot):
    """Rot 13 cipher class, - constructor and methods. Rot subclass"""

    def __init__(self, text, key=13) -> None:
        super().__init__(text, key)

    def use_rot(
        self, symbols=string.ascii_lowercase * 2 + string.ascii_uppercase * 2
    ) -> str:
        """Rot 13 encrypt method"""

        return super().use_rot(symbols)


class Rot47(Rot):
    """Rot 47 cipher class, - constructor and methods. Rot subclass"""

    def __init__(self, text: str, key=47) -> None:
        super().__init__(text, key)

    def use_rot(self, symbols="") -> str:
        """Rot 47 encrypt method"""

        for i in range(33, 127):
            symbols += chr(i)
        return super().use_rot(symbols)
