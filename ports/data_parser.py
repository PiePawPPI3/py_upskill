class EmptyFileError(Exception):
    pass


class FileNotFound(Exception):
    pass


class UnsupportedFileFormatError(Exception):
    pass


class AccessDeniedError(Exception):
    pass


class InvalidGradeError(Exception):
    pass


class DataProcessingError(Exception):
    pass


class BinaryFileError(Exception):
    pass


class UnknownError(Exception):
    pass


class FileSaveError(Exception):
    pass
