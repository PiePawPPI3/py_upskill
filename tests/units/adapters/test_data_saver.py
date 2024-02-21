import datetime
import json
from pathlib import Path

import pytest

from adapters.data_saver import TerminalPrinter, TxtWriter, HtmlWriter, render_content
from ports.student import Student

TEMPLATE_PATH = Path(__file__).parent.parent.parent.parent / 'templates'
TEMPLATE_PATH_DATA = Path(__file__).parent / 'data'


@pytest.fixture
def students_data() -> list[Student]:
    students_data = [
        Student('Cezary', [3.0, 5.0, 1.0, 3.0, 1.0, 1.0, 5.0, 4.0, 6.0]),
        Student('Dionizy', [6.0, 3.0, 6.0, 5.5, 5.0, 3.5, 4.0]),
        Student('Barnaba', [5.0, 4.0, 5.5, 4.0, 6.0, 3.5, 1.0])
    ]
    return students_data


@pytest.fixture
def terminal_printer():
    return TerminalPrinter()


@pytest.fixture
def txt_writer(tmpdir):
    output_path = tmpdir.mkdir("outputs").strpath
    return TxtWriter(output_path)


@pytest.fixture
def html_writer(tmpdir):
    output_path = tmpdir.mkdir("outputs").strpath
    return HtmlWriter(output_path)


@pytest.fixture(params=['txt', 'html'])
def template_name_fixture(request) -> str:
    if request.param == 'txt':
        return str('student_report_template.txt')
    elif request.param == 'html':
        return str('student_report_template.html')


@pytest.mark.parametrize('expected_content',
                         [
                             (TEMPLATE_PATH_DATA / 'test_data_student.txt').read_text(),
                             (TEMPLATE_PATH_DATA / 'test_data_student.html').read_text()
                         ])
def test_render_content(students_data: list[Student], template_name_fixture: str,
                        expected_content: str) -> None:
    assert render_content(students_data, template_name_fixture) == expected_content


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


def test_html_writer_writes_file(tmpdir, mocker, students_data: list[Student], html_writer) -> None:
    mocker.patch('adapters.data_saver.render_content', return_value='<p>Romek</p>')

    html_writer.write(students_data)

    time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    expected_file_path = tmpdir.join(f'scores_{time_str}.html')

    assert expected_file_path.exists()
    content = expected_file_path.read_text()
    assert '<p>Romek</p>' in content
