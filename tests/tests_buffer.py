import pytest
import datetime
from datetime import datetime, timezone

import functionality.buffer
from functionality.buffer import Buffer


class TestBuffer:
    def test_created_buffer_obj(self):
        buffer_obj = Buffer()
        assert list() == buffer_obj.buffer

    def test_write_to_buffer_method(self):
        text = "abc"
        encrypted_text = "abc"
        rot = "rot"
        mode = "encrypt"
        buffer_obj = Buffer()

        buffer_obj.write_buffer(text, encrypted_text, mode, rot)

        assert len(buffer_obj.buffer) == 1
        assert type(buffer_obj.buffer[0]) == dict

        dct = buffer_obj.buffer[0]

        assert "Original text" in dct.keys()
        assert "Modified text" in dct.keys()
        assert "Time" in dct.keys()
        assert "Mode" in dct.keys()

    def test_write_buffer(self, mocker):
        mock_buffer_class = mocker.patch("functionality.buffer.Buffer")
        mock_write_buffer = mocker.patch("functionality.buffer.Buffer.write_buffer.new")
        mock_write_buffer.return_value = "test"
        expected = ["test"]
        assert mock_buffer_class.write_buffer()

    def test_print_buffer(self):  # Todo
        pass

    def test_clear_buffer(self):  # Todo
        pass

    def test_delete_one_text(self):  # Todo
        pass
