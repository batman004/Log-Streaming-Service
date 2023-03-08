import logging

from fastapi import APIRouter
from fastapi import Request
from sse_starlette.sse import EventSourceResponse

logger = logging.getLogger(__file__)

from handlers.log_file_handler import LogFileHandler

file_path = "logs/test.log"

router = APIRouter()


@router.get("/stream-logs")
async def stream_logs(request: Request):
    log_file_handler = LogFileHandler(file_path)
    event_generator = log_file_handler.file_update_listener(request)
    return EventSourceResponse(event_generator)


@router.get("/existing-logs")
async def get_existing_logs():
    log_file_handler = LogFileHandler(file_path)
    existing_logs = log_file_handler.read_from_file()
    return EventSourceResponse(existing_logs)
