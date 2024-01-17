import pytest
from adapters.data_saver import TerminalPrinter
from ports.student import Student


@pytest.fixture
def students_data() -> list[Student]:
    # students_data = [
    #     Student('Romek', [4, 4, 5, 6]),
    #     Student("Tomek", [3, 1, 5]),
    #     Student("Atomek", [2, 5, 5, 6, 2]),
    #     Student("Pawel", [1, 4, 4, 3]),
    # ]
    # return students_data
    pass


def test_terminal_printer(mocker, students_data: list[Student], capsys) -> None:
    mocker.patch("adapters.data_saver.render_content", return_value="zz")

    terminal_printer = TerminalPrinter()
    terminal_printer.write(students_data)

    captured = capsys.readouterr()
    assert "zz" in captured.out