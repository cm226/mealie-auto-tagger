
import requests

from mealie_auto_tagger.services.mealie_auth import mealieAuth


class MealieRequester():

    def __init__(self, timeout=10):
        self.timeout = timeout

    def get_request(self, url: str, params=None):
        resp = requests.get(
            url,
            headers=mealieAuth.with_auth({}),
            params=params,
            timeout=self.timeout)

        if not resp.ok:
            raise RuntimeError("Failed to make request: " + resp.text)

        return resp

    def post_request(self, url: str, json=None):

        headers = {}
        if json is not None:
            headers = {
                "Content-Type": "application/json"
            }

        resp = requests.post(
            url,
            headers=mealieAuth.with_auth(headers),
            json=json,
            timeout=self.timeout)

        if not resp.ok:
            raise RuntimeError("Failed to make request" +
                               resp.text)
        return resp

    def put_request(self, url: str, json=None):

        headers = {}
        if json is not None:
            headers = {
                "Content-Type": "application/json"
            }

        resp = requests.put(
            url,
            headers=mealieAuth.with_auth(headers),
            json=json,
            timeout=self.timeout)

        if not resp.ok:
            raise RuntimeError("Failed to make request" +
                               resp.text)
        return resp
