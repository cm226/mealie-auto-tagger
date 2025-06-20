from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI

from routes import makeRouter
from services.makeNotifier import makeNotifier
from services.mealieLabels import mealieLabels
from services.logging import getlogger
from services.embedding.embeddingService import EmbeddingService
from model.settings import settings

description = """
Automatically tag Mealie shopping list items
"""

logger = getlogger()

@asynccontextmanager
async def lifespan_fn(_: FastAPI) -> AsyncGenerator[None, None]:
    logger.info("-----SYSTEM STARTUP-----")

    init = makeNotifier()
    init.make()

    labels = mealieLabels.createLables(settings.labels)

    embedding = EmbeddingService()
    labelEmbeddings = embedding.computingLabelEmbeddings(labels)

    app.include_router(makeRouter(labelEmbeddings))
    yield

    logger.info("-----SYSTEM SHUTDOWN----- \n")

app = FastAPI(
    title="Mealie-auto-tagger",
    description=description,
    version="1.0",
    docs_url="",
    redoc_url="",
    lifespan=lifespan_fn
)
