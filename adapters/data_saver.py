import datetime
from abc import ABC, abstractmethod

from ports.data_parser import FileSaveError
from jinja2 import Environment, FileSystemLoader


class FileWriter(ABC):

    @abstractmethod
    def write(self, content: str) -> None:
        pass


class TxtWriter(FileWriter):
    def __init__(self, output_path: str):
        self.output_path = output_path

    def write(self, students_data: list) -> None:

        try:
            time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            file_path = f'{self.output_path}scores_{time_str}.txt'

            rendered_content = DataRenderer.render_content(students_data)

            with open(file_path, 'w') as file:
                file.write(rendered_content)
            print(f'Scores saved to "{file_path}" successfully.')
        except OSError as e:
            raise FileSaveError(e)


class PdfWriter(FileWriter):

    def __init__(self, output_path: str):
        self.output_path = output_path

    def write(self, content: str) -> None:
        try:
            time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            file_path = f'{self.output_path}scores_{time_str}.pdf'
            with open(file_path, 'w') as file:
                pass  # to:do
            print(f'Scores saved to "{file_path}" successfully.')
        except OSError as e:
            raise FileSaveError(e)


class TerminalPrinter(FileWriter):

    def write(self, students_data: list) -> None:
        rendered_content = DataRenderer.render_content(students_data)
        print(rendered_content)


class DataRenderer:
    @staticmethod
    def render_content(students_data: list) -> str:
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('student_report_template.html')

        rendered_html_report = template.render({
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            'students': students_data
        })
        return rendered_html_report
