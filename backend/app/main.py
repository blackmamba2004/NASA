from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dishka.integrations.fastapi import setup_dishka

from backend.app.container import container
from backend.app.endpoints import api_router


app = FastAPI()
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все домены, вы можете ограничить на конкретные домены
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST и т. д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

setup_dishka(container, app)

