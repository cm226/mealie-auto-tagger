import pytest
from pydantic import BaseModel
from pytest_httpserver import HTTPServer
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieShoppingListItem
from mealie_auto_tagger.model.mealie.urls import MealieURLS

from tests.integration.messages.test_messages import notifier, paginated, label


class FakeMealieHTTPServer(HTTPServer):

    def add_notifiers(self, notifiers=None):
        if notifiers is None:
            notifiers = [notifier()]

        notifications_resp = paginated(notifiers)
        self.respond_with(MealieURLS.NOTIFICATIONS, notifications_resp)
        self.expect_request(MealieURLS.NOTIFICATIONS+'/',
                            method="PUT").respond_with_data("", 200)

    def add_labels(self, labels=None):
        if labels is None:
            labels = [label()]

        self.respond_with(
            MealieURLS.LABELS, paginated(labels))

    def add_shopping_list_items(self, list_items: list[MealieShoppingListItem]):
        for list_item in list_items:
            self.respond_with(MealieURLS.shopping_list_item(
                list_item.id), list_item)

    def respond_with(
            self,
            url: str,
            model: BaseModel):
        self.expect_request(
            url, method="GET").respond_with_data(model.model_dump_json(), content_type="application/json")


@pytest.fixture
def mealie_server():

    # Create an instance of your mixed-in server
    server = FakeMealieHTTPServer(host='localhost', port=9000)
    server.start()
    yield server
    server.check_assertions()
