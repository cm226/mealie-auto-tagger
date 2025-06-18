from model.mealie.shoppingListItem import ShoppingListItem
import requests

from model.settings import settings
import urllib.parse

from services.mealieAuth import mealieAuth

class __MealieShoppingList():
    def getListItem(self, itemID: str):
        reqURL = urllib.parse.urljoin(settings.mealie_url, f"api/households/shopping/items/{itemID}") 
        resp = requests.get(reqURL, headers=mealieAuth.withAuth({}))

        if not resp.ok:
            raise RuntimeError(f"Failed to get list Item {itemID} : {resp.text}")

        print(resp.json())
        listItem = ShoppingListItem(**resp.json())
        return listItem
    
    def updateListItem(self, listItem: ShoppingListItem):
        reqURL = urllib.parse.urljoin(settings.mealie_url, f"api/households/shopping/items/{listItem.id}")
        resp = requests.put(
            reqURL,
            headers=mealieAuth.withAuth({}),
            json=listItem.model_dump())

        if not resp.ok:
            raise RuntimeError(f"Failed to update list item")


mealieShoppingList = __MealieShoppingList()