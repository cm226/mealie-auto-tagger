import urllib.parse
from mealie_auto_tagger.mixins.mealie_requester import MealieRequester
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel
from mealie_auto_tagger.model.mealie.paginated import PaginatedQueryResp
from mealie_auto_tagger.model.settings import settings
from mealie_auto_tagger.services import logging


logger = logging.getlogger()


class _MealieLabels(MealieRequester):

    def make_mealie_req(self, api: str):
        full_url = urllib.parse.urljoin(settings.mealie_url, api)
        return self.get_request(full_url)

    def get_all_labels(self):
        resp = self.make_mealie_req("api/groups/labels")
        all_labels: list[MealieLabel] = []

        query_resp = PaginatedQueryResp[MealieLabel](**resp.json())
        all_labels += query_resp.items
        while query_resp.next:
            resp = self.make_mealie_req("api/groups/labels")
            query_resp = PaginatedQueryResp[MealieLabel](**resp.json())
            all_labels += query_resp.items
        return all_labels

    def get_one_label(self, label: str):
        resp = self.make_mealie_req(f"api/groups/labels/{label}")
        return resp.json()

    def check_label_valid(self, label: str | None):
        if label is None:
            return False
        try:
            self.get_one_label(label)
        except Exception:  # pylint: disable=broad-exception-caught
            return False
        return True


mealieLabels = _MealieLabels()
