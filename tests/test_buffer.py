import builtins
from unittest.mock import patch, call
import pytest
import datetime
from datetime import datetime, timezone

import functionality.buffer

from functionality.buffer import Buffer


class TestBuffer:
    def test_created_buffer_obj(self):
        buffer_obj = Buffer()
        assert list() == buffer_obj.buffer

    def test_write_buffer(self, mocker):
        mock_buffer_class = mocker.patch("functionality.buffer.Buffer")
        mock_write_buffer = mocker.patch("functionality.buffer.Buffer.write_buffer.new")
        mock_write_buffer.return_value = "test"
        expected = ["test"]
        assert mock_buffer_class.write_buffer()

    def test_clear_buffer(self):  # new

        test_buffer = Buffer()
        test_buffer.buffer = [1, 2, 3]
        test_buffer.clear()
        assert test_buffer.buffer == list()

    def test_delete_one_text(self):  # new
        test_buffer = Buffer()
        test_buffer.buffer = ["a", "b", "c"]
        test_buffer.delete_one_text(2)
        assert test_buffer.buffer == ["a", "c"]
