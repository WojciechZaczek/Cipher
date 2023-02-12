from functionality.buffer import Text
import pytest
from dataclasses import dataclass


class TestText:
    def setup(self):

        self.text = "abc"
        self.encrypted_text = "cbd"
        self.rot = "rot00"
        self.time = "00:00:00"
        self.mode = "encrypt"

    def test_create_text_obj(self):

        text_obj = Text(self.text, self.encrypted_text, self.rot, self.mode, self.time)

        assert text_obj.org_text == "abc"
        assert text_obj.mdf_text == "cbd"
        assert text_obj.rot == "rot00"
        assert text_obj.time == "00:00:00"
        assert text_obj.mode == "encrypt"

    def test_text_to_dict(self):
        test_dict = {
            "Original text": "abc",
            "Modified text": "cbd",
            "Used Rot": "rot00",
            "Mode": "encrypt",
            "Time": "00:00:00",
        }
        text_obj = Text(self.text, self.encrypted_text, self.rot, self.mode, self.time)
        assert text_obj.to_dct() == test_dict
