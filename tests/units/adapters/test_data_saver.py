import pytest

from adapters.data_saver import TerminalPrinter, TxtWriter
from ports.student import Student
from unittest.mock import Mock, call


@pytest.fixture
def students_data() -> list[Student]:
    students_data = [
        Student('Romek', [4, 4, 5, 6]),
        Student('Tomek', [3, 1, 5]),
        Student('Atomek', [2, 5, 5, 6, 2]),
        Student('Pawel', [1, 4, 4, 3]),
    ]
    return students_data


@pytest.fixture
def terminal_printer():
    return TerminalPrinter()


@pytest.fixture
def txt_writer(tmpdir):
    output_path = tmpdir.mkdir("output").strpath
    return TxtWriter(output_path)


def test_terminal_printer(mocker, students_data: list[Student], caplog, terminal_printer) -> None:
    mocker.patch('adapters.data_saver.render_content', return_value='Romek')

    terminal_printer.write(students_data)

    for record in caplog.records:
        assert 'Romek' in record.message


def test_txt_writer_writes_file(tmpdir, mocker, students_data: list[Student], txt_writer) -> None:
    txt_writer.write(students_data)

    time_str = mocker.datetime.now().strftime('%Y%m%d%H%M%S')
    expected_file_path = tmpdir.join(f'scores_{time_str}.txt')

    assert expected_file_path.exists()
    content = expected_file_path.read_text()
    assert 'Romek' in content
