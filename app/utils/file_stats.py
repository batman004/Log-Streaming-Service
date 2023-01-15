import os


class FileUtils:
    def __init__(self, file_location) -> None:
        self.file_location = file_location

    def get_file_size(self) -> int:
        # size of file in KB
        file_size = os.stat(self.file_location).st_size // 1024
        return file_size

    def is_file_big(self) -> bool:
        file_size = self.get_file_size()
        if file_size > 20:
            return True

        return False
