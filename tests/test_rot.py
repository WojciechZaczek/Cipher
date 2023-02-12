import pytest


from functionality.rot import Rot, Rot47, Rot13, RotFactory


class TestRot:
    def setup(self):
        self.text = "abc"
        self.text_2 = "abc abc"

    @pytest.mark.rot
    def test_rot_string(self):
        expected = "bcd"
        test = Rot(self.text, 1)
        assert test.use_rot("abcd") == expected

    @pytest.mark.rot
    def test_rot_string_with_white_chr(self):
        expected = "bcd bcd"
        test = Rot(self.text_2, 1)
        assert test.use_rot("abcd") == expected


class TestRot13:
    def setup(self):
        self.name = "Marvin"
        self.text = "dog"
        self.sentence = "Marvin the dog."

    @pytest.mark.rot13
    def test_rot13_string_with_small_letters(self):
        expected = "qbt"
        test = Rot13(self.text)
        assert test.use_rot() == expected

    @pytest.mark.rot13
    def test_rot13_string_with_small_and_big_letters(self):
        expected = "Zneiva"
        test = Rot13(self.name)
        assert test.use_rot() == expected

    @pytest.mark.rot13
    def test_rot13_string_with_small_big_letters_and_other_characters(self):
        expected = "Zneiva gur qbt."
        test = Rot13(self.sentence)
        assert test.use_rot() == expected


class TestRot47:
    def setup(self):
        self.name = "Marvin"
        self.text = "dog"
        self.sentence = "Marvin the dog 123!"

    @pytest.mark.rot47
    def test_rot47_string_with_small_letters(self):
        expected = "5@8"
        test = Rot47(self.text)
        assert test.use_rot() == expected

    @pytest.mark.rot47
    def test_rot47_string_with_small_and_big_letters(self):
        expected = "|2CG:?"
        test = Rot47(self.name)
        assert test.use_rot() == expected

    @pytest.mark.rot47
    def test_rot47_string_with_small_big_letters_and_other_characters(self):
        expected = "|2CG:? E96 5@8 `abP"
        test = Rot47(self.sentence)
        assert test.use_rot() == expected


class TestRotFactory:
    def setup(self):
        self.text = "text"

    @pytest.mark.rot_factory
    def test_factory_with_rot13_compare_self_text(self):
        actual = RotFactory.get_rot("rot13", self.text)
        expected = Rot13(self.text)
        assert actual.text == expected.text

    @pytest.mark.rot_factory
    def test_factory_with_rot47_compare_self_text(self):
        actual = RotFactory.get_rot("rot47", self.text)
        expected = Rot47("text")
        assert actual.text == expected.text
