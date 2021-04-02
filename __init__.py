import logzero
from logzero import logger
from proxy import Proxy
import requests
from bs4 import BeautifulSoup
import json
import random


class ProxyManager:
    """
    Прокси менеджер для скрапперов
    """

    FATE_PROXY_URL = "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list"

    def __init__(self, protocol="http", anonymity=False):
        """
        Конструктор
        """
        self.__protocol = protocol
        self.__anonymity = anonymity
        self.__proxy_list = []

        self._load_list_from_fateproxy()

        print(self.__proxy_list[0], self.__proxy_list[1], self.__proxy_list[2])

    def get_random(self) -> Proxy:
        """
        Получить следующий рандомный прокси
        :return: Proxy
        """

        if len(self.__proxy_list) == 0:
            return None

        candidats = self._get_next_candidats()

        if len(candidats) == 0:
            return None

        select_proxy = random.choice(candidats)
        select_proxy.use()

        return select_proxy

    def _get_next_candidats(self):
        """
        Получить следующих кандидатов на выдачу (у кого самый маленький used)
        :return: Proxy []
        """

        min_used = self._get_min_used()

        candidats = []
        for el in self.__proxy_list:
            if el.used == min_used:
                candidats.append(el)

        return candidats

    def _get_min_used(self):
        """
        Число минимального использования прокси
        :return: int
        """

        kolvo = -1
        for el in self.__proxy_list:
            if kolvo == -1:
                kolvo = el.used
            elif el.used < kolvo:
                kolvo = el.used

        return kolvo

    def _load_list_from_fateproxy(self):
        spisok = self._get_url(self.FATE_PROXY_URL)

        for line in spisok.splitlines():
            load_proxy = json.loads(line)

            add = False
            if load_proxy['type'] == self.protocol:
                if self.anonymity:
                    if load_proxy['anonymity'] == 'anonymous' or load_proxy['anonymity'] == 'high_anonymous':
                        add = True
                else:
                    add = True

            if add:
                self._add_proxy(load_proxy['host'], load_proxy['port'], load_proxy['type'], load_proxy['anonymity'])

    def _add_proxy(self, ip: str, port: str, protocol: str, anonymity: bool):
        """
        Добавление загруженного прокси в список прокси
        """

        new_proxy = Proxy(ip, port, protocol, anonymity)

        if new_proxy not in self.__proxy_list:
            self.__proxy_list.append(new_proxy)

    def _get_url(self, proxy_url: str):
        r = requests.get(proxy_url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
            })

        return r.text

    @property
    def protocol(self):
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol="http"):
        self.__protocol = protocol

    @property
    def anonymity(self):
        return self.__anonymity

    @anonymity.setter
    def anonymity(self, anonymity=False):
        self.__anonymity = anonymity


if __name__ == "__main__":
    logzero.loglevel(logzero.DEBUG)

    proxy_list = ProxyManager(protocol="https", anonymity=True)

    for i in range(1, 1000):
        pr = proxy_list.get_random()
        print(i, ": ", pr, "(", pr.used, ")")
