from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel
from mealie_auto_tagger.model.mealie.paginated import PaginatedQueryResp
from mealie_auto_tagger.model.settings import settings
from mealie_auto_tagger.services import logging
from mealie_auto_tagger.services.mealieAuth import mealieAuth

import urllib.parse
import requests

logger = logging.getlogger()

class __MealieLabels():

    def checkExists(self, labelName: str):

        params = {
            "queryFilter": f"name == \"{labelName}\""
        }
        lableURL = urllib.parse.urljoin(settings.mealie_url, "api/groups/labels")
        resp = requests.get(
            lableURL,
            headers=mealieAuth.withAuth({}),
            params=params)

        if not resp.ok:
            raise RuntimeError("Failed to get labels: " + resp.text)
        

        queryResp = PaginatedQueryResp[MealieLabel](**resp.json())
        logger.info(queryResp) 
        if queryResp.total != 0:
            return queryResp.items[0]
        
        return None
        

    def makeLabel(self, labelName: str):
        label = self.checkExists(labelName)
        if not label == None:
            return label
        
        label = {
            "name": labelName,
            "color": "#959595"
        }

        lableURL = urllib.parse.urljoin(settings.mealie_url, "api/groups/labels")
        resp = requests.post(
            lableURL,
            headers=mealieAuth.withAuth({}),
            json=label)

        if not resp.ok:
            raise RuntimeError("Failed to create new label " + resp.text)

        return MealieLabel(**resp.json())

    def createLabels(self, labels: list[str]) -> list[MealieLabel]:
        return [self.makeLabel(name) for name in labels]
            

mealieLabels = __MealieLabels()