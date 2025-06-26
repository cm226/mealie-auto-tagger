from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI

from mealie_auto_tagger.routes.webhook import makeRouter
from mealie_auto_tagger.db.init import SessionLocal
from mealie_auto_tagger.db.repos.all_repositories import get_repositories
from mealie_auto_tagger.services.makeNotifier import mealieNotifier
from mealie_auto_tagger.services.mealieLabels import mealieLabels
from mealie_auto_tagger.services.logging import getlogger
from mealie_auto_tagger.services.embedding.embeddingService import embeddingService
from mealie_auto_tagger.model.settings import settings
description = """
Automatically tag Mealie shopping list items
"""

logger = getlogger()

@asynccontextmanager
async def lifespan_fn(_: FastAPI) -> AsyncGenerator[None, None]:
    logger.info("-----SYSTEM STARTUP-----")
    mealieNotifier.make()

    labels = mealieLabels.getAllLabels()

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
