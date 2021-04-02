import logzero
from logzero import logger
from proxy import Proxy
import requests
from bs4 import BeautifulSoup
import json


class ProxyManager:
    """
    Прокси менеджер для скрапперов
    """

    PROXY_PUB_URL = "http://pubproxy.com/api/proxy?limit=5&format=txt&https=true&type=https"
    # "http://pubproxy.com/api/proxy?limit=5&format=txt&https=true&type=http&level=anonymous&user_agent=true&cookies=true"
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

    proxy = ProxyManager(protocol="https", anonymity=True)

