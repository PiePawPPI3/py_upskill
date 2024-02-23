import datetime
import os
from pathlib import Path

import pytest

from freezegun import freeze_time
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
def output_path(tmpdir):
    return tmpdir.mkdir('output')


@pytest.fixture
def txt_writer(output_path):
    output_path_str = output_path.strpath
    return TxtWriter(output_path_str)


@pytest.fixture
def html_writer(output_path):
    output_path_str = output_path.strpath
    return HtmlWriter(output_path_str)


@pytest.mark.parametrize('expected_content_path, template_type',
                         [
                             ((TEMPLATE_PATH_DATA / 'test_data_student.txt'), 'txt'),
                             ((TEMPLATE_PATH_DATA / 'test_data_student.html'), 'html')
                         ])
@freeze_time("2024-02-21 22:58")
def test_render_content(students_data: list[Student], expected_content_path: Path, template_type: str) -> None:
    expected_content = expected_content_path.read_text()
    template_name = f"student_report_template.{template_type}"
    assert render_content(students_data, template_name) == expected_content


def test_terminal_printer(mocker, students_data: list[Student], caplog, terminal_printer) -> None:
    mocker.patch('adapters.data_saver.render_content', return_value='Cezary')

    terminal_printer.write(students_data)

    for record in caplog.records:
        assert 'Cezary' in record.message


@freeze_time('2024-02-21 22:58:34')
def test_txt_writer_writes_file(students_data: list[Student], txt_writer) -> None:
    txt_writer.write(students_data)
    output_files = os.listdir(txt_writer.output_path)
    time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    for file in output_files:
        assert file.startswith(f'scores_{time_str}') and file.endswith('.txt')


@freeze_time('2024-02-22 23:11:11')
def test_html_writer_writes_file(students_data: list[Student], html_writer, mocker) -> None:
    mocker.patch('adapters.data_saver.render_content', return_value='<p>Cezary</p>')

    html_writer.write(students_data)
    output_files = os.listdir(html_writer.output_path)
    time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    for file in output_files:
        assert file.startswith(f'scores_{time_str}') and file.endswith('.html')

        expected_file_path = os.path.join(html_writer.output_path, file)
        with open(expected_file_path, 'r') as f:
            content = f.read()
            assert '<p>Cezary</p>' in content
