import requests


class MainPortalProxy:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_user_list(self):
        url = self.base_url + "?act=getUsersList"
        response = requests.get(url)
        response.raise_for_status()
        response_json = response.json()
        return response_json

    def register_new_user(self, currency):
        url = self.base_url + f"?act=registerNewUser&currency={currency}"
        response = requests.get(url)
        response.raise_for_status()
        response_json = response.json()
        return response_json

    def set_user_balance(self, user_id, balance, currency):
        url = self.base_url + f"?act=setbalance&user_id={user_id}&balance={balance}&currency={currency}"
        response = requests.get(url)
        response.raise_for_status()
        return response

    def get_user_balance(self, user_id, balance, currency):
        url = self.base_url + f"?act=setbalance&user_id={user_id}&balance={balance}&currency={currency}"
        response = requests.get(url)
        response.raise_for_status()
        response_json = response.json()
        return response_json

    def get_game_url(self, currency, user_id, game_id):
        url = self.base_url + f"?act=game&mode=real&denom=1&lang=en&cur={currency}&user_id={user_id}&game=fullstate%5Chtml5%5Cnovomatic%5C{game_id}"
        response = requests.get(url)
        response.raise_for_status()
        response_json = response.json()
        game_url = response_json['link']
        return game_url
