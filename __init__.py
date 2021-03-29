import logzero
from logzero import logger
from .proxy import Proxy

class ProxyManager:
    """
    Прокси менеджер для скрапперов
    """

    PROXY_PUB_URL = "http://pubproxy.com/api/proxy?limit=5&format=txt&https=true&type=https"
    # "http://pubproxy.com/api/proxy?limit=5&format=txt&https=true&type=http&level=anonymous&user_agent=true&cookies=true"

    def __init__(self, protocol="http", anonymity=False):
        """
        Конструктор
        """
        self.__protocol = protocol
        self.__anonymity = anonymity

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

