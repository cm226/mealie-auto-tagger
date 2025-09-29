from werkzeug import Request
from pytest_httpserver import RequestMatcher
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieShoppingListItem


class ListItemMatcher(RequestMatcher):

    def __init__(self, expected: MealieShoppingListItem, **kwargs):
        super().__init__(**kwargs)
        self.expected = expected

    def match(self, request: Request) -> bool:
        match = super().match(request)
        if not match:  # existing parameters didn't match -> return with False
            return match

        json = request.json
        if isinstance(json, dict):
            listItem = MealieShoppingListItem(**json)
            return self.expected == listItem

        return False
