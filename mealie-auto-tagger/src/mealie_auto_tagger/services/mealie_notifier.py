import urllib.parse
from mealie_auto_tagger.mixins.mealie_requester import MealieRequester
from mealie_auto_tagger.model.settings import settings
from mealie_auto_tagger.model.mealie.notifier import Notifier
from mealie_auto_tagger.model.mealie.paginated import PaginatedQueryResp
from mealie_auto_tagger.services.logging import getlogger

logger = getlogger()


class _MealieNotifier(MealieRequester):

    NAME = "mealie-auto-tagger"

    def __check_for_existing(self):

        get_notifiers_url = urllib.parse.urljoin(
            settings.mealie_url, "api/households/events/notifications")
        params = {
            "queryFilter": f"name == \"{self.NAME}\""
        }
        resp = self.get_request(get_notifiers_url, params)
        query_resp = PaginatedQueryResp[Notifier](**resp.json())
        if query_resp.total != 0:
            return query_resp.items[0]

        return None

    def __create_new(self):
        payload = {
            "name": "mealie-auto-tagger",
            "appriseUrl": f"json://{settings.host}/webhooks/post/"
        }
        create_notifier_url = urllib.parse.urljoin(
            settings.mealie_url, "api/households/events/notifications")
        create_notifiaction_resp = self.post_request(
            create_notifier_url, json=payload)

        notifier = Notifier(**create_notifiaction_resp.json())

        return notifier

    def make(self):
        notifier = self.__check_for_existing()
        if notifier is None:
            notifier = self.__create_new()

        notifier.options.shoppingListUpdated = True
        notifier.options.labelCreated = True
        notifier.options.labelUpdated = True
        notifier.options.labelDeleted = True
        notifier.appriseUrl = f"json://{settings.host}/webhooks/post/"

        update_notifier_url = urllib.parse.urljoin(
            settings.mealie_url, f"/api/households/events/notifications/{notifier.id}")
        self.put_request(
            update_notifier_url,
            json=notifier.model_dump())


mealieNotifier = _MealieNotifier()
