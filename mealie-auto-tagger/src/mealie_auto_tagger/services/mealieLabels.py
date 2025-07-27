from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel
from mealie_auto_tagger.model.mealie.paginated import PaginatedQueryResp
from mealie_auto_tagger.model.settings import settings
from mealie_auto_tagger.services import logging
from mealie_auto_tagger.services.mealieAuth import mealieAuth

import urllib.parse
import requests

logger = logging.getlogger()

class __MealieLabels():

    def makeMealieReq(self, api: str):
        fullUrl = urllib.parse.urljoin(settings.mealie_url, api)
        resp = requests.get(
            fullUrl,
            headers=mealieAuth.withAuth({}))

        if not resp.ok:
            raise RuntimeError("Failed to make request: " + resp.text)
        
        return resp

    def getAllLabels(self):
        resp = self.makeMealieReq("api/groups/labels") 
        allLabels :list[MealieLabel] = []

        queryResp = PaginatedQueryResp[MealieLabel](**resp.json())
        allLabels += queryResp.items
        while queryResp.next:
            resp = self.makeMealieReq("api/groups/labels") 
            queryResp = PaginatedQueryResp[MealieLabel](**resp.json())
            allLabels += queryResp.items
        return allLabels
    
    def getOneLabel(self, label:str): 
        resp = self.makeMealieReq(f"api/groups/labels/{label}")
        return resp.json()
    
    def checkLabelValid(self, label: str | None):
        if label == None:
            return False
        try:
            self.getOneLabel(label)
        except:
            return False
        return True


mealieLabels = __MealieLabels()