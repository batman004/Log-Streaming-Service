import logging

from fastapi import APIRouter
from fastapi import Request

logger = logging.getLogger(__file__)

file_path = "logs/test.log"

router = APIRouter()

# stream logs in real-time and await new changes
@router.get("/stream-logs")
async def stream_logs(request: Request):
    pass


# stream existing logs and then wait for new changes
@router.get("/existing-logs")
async def get_existing_logs():
    pass
