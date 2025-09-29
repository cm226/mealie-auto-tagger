from mealie_auto_tagger.model.mealie.shoppingListItem import MealieShoppingListItem
import requests

from mealie_auto_tagger.model.settings import settings
import urllib.parse

from mealie_auto_tagger.services.mealieAuth import mealieAuth


class __MealieShoppingList():
    def getListItem(self, itemID: str):
        req_url = urllib.parse.urljoin(
            settings.mealie_url, f"api/households/shopping/items/{itemID}")
        resp = requests.get(req_url, headers=mealieAuth.withAuth({}))

        if not resp.ok:
            raise RuntimeError(
                f"Failed to get list Item {itemID} : {resp.text}")

        listItem = MealieShoppingListItem(**resp.json())
        return listItem

    def updateListItem(self, list_item: MealieShoppingListItem):
        req_url = urllib.parse.urljoin(
            settings.mealie_url, f"api/households/shopping/items/{list_item.id}")
        resp = requests.put(
            req_url,
            headers=mealieAuth.withAuth({}),
            json=list_item.model_dump())

        if not resp.ok:
            raise RuntimeError(f"Failed to update list item")


mealieShoppingList = __MealieShoppingList()
