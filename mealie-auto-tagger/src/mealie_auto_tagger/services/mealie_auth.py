
from typing import Any

from mealie_auto_tagger.model.settings import settings
from mealie_auto_tagger.services.mealie_auto_tagger_logging import getlogger

logger = getlogger()


class _MealieAuth():

    def with_auth(self, headers: dict[str, Any]):
        headers["Authorization"] = f"Bearer {settings.mealie_api_token}"
        return headers


mealieAuth = _MealieAuth()
