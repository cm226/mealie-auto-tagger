from messages.test_messages import shopping_list_item, label, notified_message
from matchers.list_item_matcher import ListItemMatcher
from fastapi.testclient import TestClient
from mealie_auto_tagger.model.mealie.urls import MealieURLS
from mealie_auto_tagger.app import app
from mealie_auto_tagger.model.mealie.notifiedMessage import ShoppingListUpdate


def test_update_new_item(mealie_server):

    # Setup
    only_label = label()
    new_list_item = shopping_list_item()

    mealie_server.add_notifiers()
    mealie_server.add_labels([only_label])
    mealie_server.add_shopping_list_items([new_list_item])

    with TestClient(app) as client:

        # Check
        expected_list_item = shopping_list_item()
        expected_list_item.label = only_label
        expected_list_item.labelId = only_label.id
        mealie_server.expect(
            ListItemMatcher(expected_list_item, uri=MealieURLS.shopping_list_item(new_list_item.id), method="PUT")).respond_with_data("", 200)

        # Act
        list_update = ShoppingListUpdate(
            shoppingListId="", shoppingListItemIds=[new_list_item.id])
        response = client.post(
            "/webhooks/post/", content=notified_message("shopping_list_updated", list_update).model_dump_json())
        assert response.status_code == 200
