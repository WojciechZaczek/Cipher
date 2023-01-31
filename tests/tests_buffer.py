import pytest
import datetime
from datetime import datetime, timezone

import functionality.buffer
from functionality.buffer import Buffer


class TestBuffer:
    def test_print_buffer(self):
        expected = ["test"]
        buffer = Buffer(["test"])
        assert expected == buffer.buffer

    # @pytest.fixture
    # def buffer_now(self, mocker):
    #     now = datetime.fromisoformat('2023-01-01 00:00:00.000000')
    #
    #     mock_datetime = mocker.patch("functionality.buffer.datetime")
    #     mocker.patch("functionality.datetime.now", return_value=now)
    #
    #     mock_datetime.fromisoformat = datetime.fromisoformat
    #     return now
    #
    # @pytest.fixture
    # def buffer_mode(self, mocker):
    #     mode = "encrypt"
    #     mocker.patch("functionality.buffer.Buffer.write_buffer.mode", return_value=mode)
    #
    # def test_write_buffer(self):
    #     expected=Buffer
    def test_write_buffer(self, mocker):
        mock_buffer_class = mocker.patch("functionality.buffer.Buffer")
        mock_write_buffer = mocker.patch("functionality.buffer.Buffer.write_buffer.new")
        mock_write_buffer.return_value = "test"
        expected = ["test"]
        assert mock_buffer_class.write_buffer()
