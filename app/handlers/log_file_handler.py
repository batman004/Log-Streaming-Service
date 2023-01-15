import asyncio
import logging
from itertools import islice

from sh import tail
from utils.file_stats import FileUtils

logger = logging.getLogger(__file__)


class LogFileHandler:
    def __init__(self, file_location) -> None:
        self.file_location = file_location
        self.line_chunk_size = 10

    async def read_from_file(self):
        """
        Reads log file in chunks if its larger
        than threshold file size, else returns
        a list of all lines
        """

        if FileUtils(self.file_location).is_file_big:
            with open(self.file_location, "r") as input_file:
                while input_file.readline():
                    lines_cache = islice(input_file, self.line_chunk_size)
                    chunk = []
                    for current_line in lines_cache:
                        chunk.append(current_line)
                    yield chunk

                    await asyncio.sleep(2)

        else:
            with open(self.file_location, "r") as input_file:
                total_lines = []
                for line in input_file:
                    total_lines.append(line)
            yield total_lines

    async def file_update_listener(self, request):
        """
        This async generator will listen
        to our log file in an infinite while
        loop, and  anytime the generator detects
        a new line in the log file, it will yield it.
        """
        for line in tail("-f", self.file_location, _iter=True):
            if await request.is_disconnected():
                logger.debug("Request disconnected")
                break
            yield line
            await asyncio.sleep(0.5)
