
from typing import Any
import requests
import urllib.parse

from mealie_auto_tagger.model.settings import settings
from mealie_auto_tagger.services.logging import getlogger

logger = getlogger()

class __MealieAuth() : 

    __token = None
    
    def __makeToken(self):
        data = {
            "username": settings.mealie_user,
            "password": settings.mealie_pw
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        authURL = urllib.parse.urljoin(settings.mealie_url, "/api/auth/token") 

        logger.info("Authenticating with mealie at: " + authURL)
        response = requests.post(authURL, data=data, headers=headers)

        if not response.ok:
           logger.error("Failed to authenticate with mealie app") 
           raise PermissionError("Mealie authentication failed: " + response.text)

        if "access_token" not in response.json():
           logger.error("Response from mealie was the wrong shape: " + response.json()) 
           raise RuntimeError("Bad response shape from mealie authentication")

        logger.info("Authentication sucessfull")
        
        self.__token = response.json()["access_token"]

    def withAuth(self, headers: dict[str, Any]):
        if self.__token == None:
            self.__makeToken()

        headers["Authorization"] = f"Bearer {self.__token}"
        return headers

mealieAuth = __MealieAuth()