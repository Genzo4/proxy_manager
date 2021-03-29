import logzero
from logzero import logger
#from proxy import Proxy
import requests
from bs4 import BeautifulSoup


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

    def _load_list_from_fateproxy(self):
        bs = self._get_url(self.FATE_PROXY_URL)
        print(bs)

    def _get_url(self, proxy_url: str):
        r = requests.get(proxy_url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
            })

        #return r.text
        return BeautifulSoup(r.text, "lxml")


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

