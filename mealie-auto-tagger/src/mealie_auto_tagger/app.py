""" Mealie auto tagger app
This module is the mealie atuo tagger application. 
It communicates with mealie to register notifiers and handles the notifications. 
"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI

from mealie_auto_tagger.routes.webhook import router as mealie_webhook
from mealie_auto_tagger.services.mealie_notifier import mealieNotifier
from mealie_auto_tagger.services.mealie_auto_tagger_logging import getlogger

DESCRIPTION = """
Automatically tag Mealie shopping list items
"""

logger = getlogger()


@asynccontextmanager
async def lifespan_fn(_: FastAPI) -> AsyncGenerator[None, None]:
    logger.info("-----SYSTEM STARTUP-----")
    mealieNotifier.make()

    app.include_router(mealie_webhook)

    logger.info("-----SYSTEM STARTUP FINISHED-----")

    yield

    logger.info("-----SYSTEM SHUTDOWN----- \n")

app = FastAPI(
    title="Mealie-auto-tagger",
    description=DESCRIPTION,
    version="1.0",
    docs_url="",
    redoc_url="",
    lifespan=lifespan_fn
)
