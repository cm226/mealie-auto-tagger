
from typing import Any

from mealie_auto_tagger.model.settings import settings
from mealie_auto_tagger.services.logging import getlogger

logger = getlogger()

class __MealieAuth() : 

    def withAuth(self, headers: dict[str, Any]):
        headers["Authorization"] = f"Bearer {settings.mealie_api_token}"
        return headers

mealieAuth = __MealieAuth()