import bs4
import json
import requests
import time

from bs4 import BeautifulSoup
from random import randint
from requests.adapters import HTTPAdapter
from datetime import datetime
from urllib3.util import Retry

class SteamGifts():

    def __init__(self, cookie, gifts_type, pinned, min_points):
        self.cookie = {
            'PHPSESSID': cookie
        }

        self.gifts_type = gifts_type
        self.pinned = pinned
        self.min_points = min_points

        self.base = "https://www.steamgifts.com"
        self.session = requests.Session()

        self.xsrf_token = None
        self.points = None

        self.filter_url = {
            'All': "search?page=%d",
            'Wishlist': "search?page=%d&type=wishlist",
            'Recommended': "search?page=%d&type=recommended",
            'Copies': "search?page=%d&copy_min=2",
            'DLC': "search?page=%d&dlc=true",
            'Group': "search?page=%d&type=group",
            'New': "search?page=%d&type=new"
        }

    def requests_retry_session(
        self,
        retries=5,
        backoff_factor=0.3
    ):
        session = self.session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=(500, 502, 504),
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

    def get_soup_from_page(self, url):
        r = self.requests_retry_session().get(url)
        r = requests.get(url, cookies=self.cookie)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    def update_info(self):
        soup = self.get_soup_from_page(self.base)

        try:
            self.xsrf_token = soup.find('input', {'name': 'xsrf_token'})['value']
            self.points = int(soup.find('span', {'class': 'nav__points'}).text)  # storage points
        except TypeError:
            datetime_now = datetime.now()
            print(f"{str(datetime_now)}: ERROR - Cookie is not valid!")
            exit()

    def get_game_content(self,  page=1):
        n = page

        while True:
            datetime_now = datetime.now()
            txt = f"{str(datetime_now)}: Retrieving {self.gifts_type} games from page {n}."

            filtered_url = self.filter_url[self.gifts_type] % n
            paginated_url = f"{self.base}/giveaways/{filtered_url}"

            soup = self.get_soup_from_page(paginated_url)

            pinned = soup.find('div', {'class': 'pinned-giveaways__outer-wrap'})

            game_list = []
            if self.pinned:
                game_list = pinned.find_all('div', {'class': 'giveaway__row-inner-wrap'})

            common_sections = pinned.find_next_siblings()
            common_list = []
            for item in common_sections:
                common_list += item.find_all('div', {'class': 'giveaway__row-inner-wrap'})

            if not len(common_list):
                break

            game_list += common_list

            for item in game_list:
                if 'is-faded' in item['class']:
                    continue

                if self.points == 0 or self.points < self.min_points:
                    datetime_now = datetime.now()
                    txt = f"{str(datetime_now)}: We have {self.points} points, but we need {self.min_points} to start. Sleeping for 15 min to get 6 points."
                    print(txt)
                    time.sleep(900)
                    self.start()

                game_cost = item.find_all('span', {'class': 'giveaway__heading__thin'})[-1]

                if game_cost:
                    game_cost = game_cost.getText().replace('(', '').replace(')', '').replace('P', '')
                else:
                    continue

                game_name = item.find('a', {'class': 'giveaway__heading__name'}).text

                if self.points - int(game_cost) < 0:
                    datetime_now = datetime.now()
                    txt = f"{str(datetime_now)}: Not enough points to enter {self.gifts_type}: {game_name}."
                    print(txt)
                    continue

                elif self.points - int(game_cost) >= 0:
                    game_id = item.find('a', {'class': 'giveaway__heading__name'})['href'].split('/')[2]
                    res = self.enter_giveaway(game_id)
                    if res:
                        self.points -= int(game_cost)
                        datetime_now = datetime.now()
                        txt = f"{str(datetime_now)}: One more {self.gifts_type} game! Has just entered {game_name}."
                        print(txt)
                        time.sleep(randint(3, 7))

            n = n+1

        print(f"List of {self.gifts_type} games has ended. Sleeping for 15 mins to update...")
        time.sleep(900)
        self.start()

    def enter_giveaway(self, game_id):
        payload = {'xsrf_token': self.xsrf_token, 'do': 'entry_insert', 'code': game_id}
        entry = requests.post('https://www.steamgifts.com/ajax.php', data=payload, cookies=self.cookie)
        json_data = json.loads(entry.text)

        if json_data['type'] == 'success':
            return True

    def remove_entry(self, game_id):
        print("TODO: remove_entry ...")

    def start(self):
        self.update_info()

        if self.points > 0:
            datetime_now = datetime.now()
            txt = f"{str(datetime_now)}: SteamGifts bot active! You have {self.points} points. Checking games."
            print(txt)

        self.get_game_content()