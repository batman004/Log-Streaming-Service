import uvicorn
from config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.endpoints import router as logs_router

# importing server settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "welcome to log streaming service"}


app.include_router(logs_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
        workers=settings.workers,
    )
