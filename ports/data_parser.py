class StudentGradesAppError(Exception):
    pass


class EmptyFileError(StudentGradesAppError):
    pass


class FileNotFound(StudentGradesAppError):
    pass


class UnsupportedFileFormatError(StudentGradesAppError):
    pass


class AccessDeniedError(StudentGradesAppError):
    pass


class InvalidGradeError(StudentGradesAppError):
    pass


class DataProcessingError(StudentGradesAppError):
    pass


class BinaryFileError(StudentGradesAppError):
    pass


class UnknownError(StudentGradesAppError):
    pass


class FileSaveError(Exception):
    pass
