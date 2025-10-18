import urllib.parse
from mealie_auto_tagger.mixins.mealie_requester import MealieRequester
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieShoppingListItem
from mealie_auto_tagger.model.settings import settings


class _MealieShoppingList(MealieRequester):
    def get_list_item(self, item_id: str):
        req_url = urllib.parse.urljoin(
            settings.mealie_url, f"api/households/shopping/items/{item_id}")
        resp = self.get_request(req_url)
        list_item = MealieShoppingListItem(**resp.json())
        return list_item

    def update_list_item(self, list_item: MealieShoppingListItem):
        req_url = urllib.parse.urljoin(
            settings.mealie_url, f"api/households/shopping/items/{list_item.id}")
        self.put_request(
            req_url,
            json=list_item.model_dump())


mealieShoppingList = _MealieShoppingList()
