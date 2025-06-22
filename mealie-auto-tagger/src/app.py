from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI

from routes.webhook import makeRouter
from db.init import SessionLocal
from db.repos.all_repositories import get_repositories
from services.makeNotifier import mealieNotifier
from services.mealieLabels import mealieLabels
from services.logging import getlogger
from services.embedding.embeddingService import embeddingService
from model.settings import settings
description = """
Automatically tag Mealie shopping list items
"""

logger = getlogger()

@asynccontextmanager
async def lifespan_fn(_: FastAPI) -> AsyncGenerator[None, None]:
    logger.info("-----SYSTEM STARTUP-----")
    mealieNotifier.make()

    labels = mealieLabels.createLabels(settings.labels)

    with SessionLocal() as session:
        get_repositories(session)\
            .labelRepo\
            .storeAllMealieLabels(labels)

    labelEmbeddings = embeddingService.computingLabelEmbeddings(labels)

    app.include_router(makeRouter(labelEmbeddings))

    logger.info("-----SYSTEM STARTUP FINISHED-----")

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
