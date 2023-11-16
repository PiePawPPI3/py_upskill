import datetime
from abc import ABC, abstractmethod

from ports.data_parser import FileSaveError


class FileWriter(ABC):
    @abstractmethod
    def write(self, content: str, output_path: str) -> None:
        pass


class TxtWriter(FileWriter):
    def write(self, content: str, output_path: str) -> None:
        try:
            time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            file_path = f'{output_path}scores_{time_str}.txt'
            with open(file_path, 'w') as file:
                file.write(content)
            print(f'Scores saved to "{file_path}" successfully.')
        except OSError as e:
            raise FileSaveError(e)


class PdfWriter(FileWriter):
    def write(self, content: str, output_path: str) -> None:
        try:
            time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            file_path = f'{output_path}scores_{time_str}.pdf'
            with open(file_path, 'w') as file:
                pass  # to:do
            print(f'Scores saved to "{file_path}" successfully.')
        except OSError as e:
            raise FileSaveError(e)
