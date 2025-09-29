from pydantic import BaseModel


class __MealieEndpoints(BaseModel, frozen=True):
    NOTIFICATIONS: str = "/api/households/events/notifications"
    LABELS: str = "/api/groups/labels"

    def shopping_list_item(self, list_item_id: str) -> str:
        """Return full URL for a specific user."""
        return f"/api/households/shopping/items/{list_item_id}"


MealieURLS = __MealieEndpoints()
