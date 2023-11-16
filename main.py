# main.py
from adapters.data_parser import read_scores, general_summary
from adapters.data_saver import TxtWriter, PdfWriter
from ports.data_parser import UnsupportedFileFormatError, FileNotFound, AccessDeniedError, BinaryFileError, \
    EmptyFileError, InvalidGradeError, DataProcessingError, UnknownError,FileSaveError




def main():
    file_path = "resources/grades1.txt"
    output_path = "outputs/"

    save_as_txt = True
    save_as_pdf = False
    display_summary = True

    try:
        lines = read_scores(file_path)
        txt_writer = TxtWriter()
        pdf_writer = PdfWriter()
        general_summary(lines, output_path, save_as_txt, save_as_pdf, display_summary, txt_writer, pdf_writer)

    except FileNotFound:
        print('File not found.')
    except BinaryFileError:
        print('Decode Error UTF-8.')
    except AccessDeniedError:
        print('Access to the file is denied.')
    except EmptyFileError:
        print('File is empty.')
    except UnsupportedFileFormatError:
        print('Not supported file type.')
    except InvalidGradeError:
        print('Grades beyond the range 1-6')
    except DataProcessingError:
        print('Data processing error')
    except UnknownError:
        print('Unknown error encountered')
    except FileSaveError as e:
        print(f'Error occurred while saving the file: {e}')


if __name__ == "__main__":
    main()
