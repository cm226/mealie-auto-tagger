import requests
from services.mealieAuth import mealieAuth
import urllib.parse

from model.settings import settings
from model.mealie.notifier import Notifier
from model.mealie.paginated import PaginatedQueryResp
from services.logging import getlogger

logger = getlogger()


class __mealieNotifier():

    NAME = "mealie-auto-tagger"

    def __check_for_existing(self):

        getNotifiersURL = urllib.parse.urljoin(settings.mealie_url, "api/households/events/notifications")
        
        params = {
            "queryFilter" : f"name == \"{self.NAME}\""
        }
        
        resp = requests.get(getNotifiersURL, params=params, headers=mealieAuth.withAuth({}))
        if not resp.ok:
            raise RuntimeError("Failed to check for existing: "+ resp.text)


        queryResp = PaginatedQueryResp[Notifier](**resp.json())
        if queryResp.total != 0:
            return queryResp.items[0]
    
        return None
    
    def __create_new(self):
        headers = {
            "Content-Type": "application/json" 
        }

        payload = {
            "name": "mealie-auto-tagger",
            "appriseUrl": f"json://{settings.host}/webhooks/post/"
        }
        createNotifierURL = urllib.parse.urljoin(settings.mealie_url, "api/households/events/notifications") 
        createNotifiactionResp = requests.post(
            createNotifierURL,
            headers=mealieAuth.withAuth(headers),
            json=payload)

        if not createNotifiactionResp.ok:
            raise RuntimeError("Failed to create notifier: "+ createNotifiactionResp.text)
        
        notifier = Notifier(**createNotifiactionResp.json())
 

        return notifier


    def make(self):
        notifier = self.__check_for_existing()
        if notifier == None:
            notifier = self.__create_new()

        notifier.options.shoppingListUpdated = True
        notifier.appriseUrl = f"json://{settings.host}/webhooks/post/"

        headers = {
            "Content-Type": "application/json" 
        }
        updateNotifierURL = urllib.parse.urljoin(settings.mealie_url, f"/api/households/events/notifications/{notifier.id}")
        updateNotifiactionResp = requests.put(
            updateNotifierURL,
            headers=mealieAuth.withAuth(headers),
            json=notifier.model_dump())

        if not updateNotifiactionResp.ok:
            raise RuntimeError("Failed to update notifier: " + updateNotifiactionResp.text)
        
mealieNotifier = __mealieNotifier()