import datetime
from abc import ABC, abstractmethod
from pathlib import Path

from ports.data_parser import FileSaveError
from jinja2 import Environment, FileSystemLoader

from ports.student import Student

TEMPLATE_PATH = Path(__file__).parent.parent / 'templates'


class FileWriter(ABC):

    @abstractmethod
    def write(self, students_data: list[Student]) -> None:
        pass


class TxtWriter(FileWriter):
    def __init__(self, output_path: str):
        self.output_path = output_path

    def write(self, students_data: list[Student]) -> None:

        try:
            time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            file_path = f'{self.output_path}/scores_{time_str}.txt'

            rendered_content = render_content(students_data, 'student_report_template.txt')

            with open(file_path, 'w') as file:
                file.write(rendered_content)
            print(f'Scores saved to "{file_path}" successfully.')
        except OSError as e:
            raise FileSaveError(e)


class HtmlWriter(FileWriter):

    def __init__(self, output_path: str):
        self.output_path = output_path

    def write(self, students_data: list[Student]) -> None:
        try:
            time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            file_path = f'{self.output_path}/scores_{time_str}.html'

            rendered_content = render_content(students_data, 'student_report_template.html')

            with open(file_path, 'w') as file:
                file.write(rendered_content)
            print(f'Scores saved to "{file_path}" successfully.')
        except OSError as e:
            raise FileSaveError(e)


class TerminalPrinter(FileWriter):
    def write(self, students_data: list[Student]) -> None:
        rendered_content = render_content(students_data, 'student_report_template.txt')
        print(rendered_content)


def render_content(students_data: list[Student], template_name: str) -> str:
    env = Environment(loader=FileSystemLoader(TEMPLATE_PATH))
    template = env.get_template(template_name)

    rendered_report = template.render({
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        'students': students_data
    })
    return rendered_report
