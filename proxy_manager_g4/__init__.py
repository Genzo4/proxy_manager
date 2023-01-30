import requests
import json
import random
import re

from proxy_manager_g4.proxy import Proxy
from proxy_manager_g4.consts import PROTOCOL_NONE, PROTOCOL_HTTP, PROTOCOL_HTTPS


class ProxyManager:

    FATE_PROXY_URL = 'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list'
    CLARKETM_PROXY_URL = 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt'

    def __init__(self,
                 protocol=PROTOCOL_HTTP,
                 anonymity: bool = False,
                 dont_load_proxy: bool = False,
                 load_fate_proxy: bool = True,
                 load_clarketm_proxy: bool = True
                 ):
        self.protocol = protocol
        self.anonymity = anonymity
        self.proxy_list = []

        if not dont_load_proxy:
            if load_fate_proxy:
                self.load_list_from_fate_proxy()

            if load_clarketm_proxy:
                self.load_list_from_clarketm_proxy()

            if load_fate_proxy or load_clarketm_proxy:
                if len(self.proxy_list) == 0:
                    raise UnboundLocalError('No proxy')

    def clear(self):
        self.proxy_list.clear()

    def proxy_count(self):
        return len(self.proxy_list)

    def get_random(self) -> Proxy or None:
        """
        Get next random proxy
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

    def _get_next_candidats(self) -> list:
        """
        Get the next candidates for issuance (who has the smallest used)
        :return: list
        """

        min_used = self._get_min_used()

        candidats = []
        for el in self.__proxy_list:
            if el.used == min_used:
                candidats.append(el)

        return candidats

    def _get_min_used(self):
        """
        Minimum proxy usage number
        :return: int
        """

        kolvo = -1
        for el in self.__proxy_list:
            if kolvo == -1:
                kolvo = el.used
            elif el.used < kolvo:
                kolvo = el.used

        return kolvo

    def load_list_from_fate_proxy(self):
        spisok = self._get_url(self.FATE_PROXY_URL)

        for line in spisok.splitlines():
            load_proxy = json.loads(line)

            if self.convert_fateproxy_type(load_proxy['type']) == self.protocol \
                    and self.anonymity == self.convert_fateproxy_anonymity(load_proxy['anonymity']):
                self.add_proxy(load_proxy['host'], load_proxy['port'], self.convert_fateproxy_type(load_proxy['type']),
                               self.convert_fateproxy_anonymity(load_proxy['anonymity']))

    def load_list_from_clarketm_proxy(self):
        spisok = self._get_url(self.CLARKETM_PROXY_URL)

        proxy_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+):(\d+)\s(..)-(.)\-?(S|)\!?\s(\+|\-)')

        for line in spisok.splitlines():
            p = proxy_pattern.search(line)
            if p is not None:
                p_type = self.convert_clarketm_proxy_type(p[5])
                p_anonym = self.convert_clarketm_proxy_anonymity(p[4])

                if p_type == self.protocol and p_anonym == self.anonymity:
                    self.add_proxy(p[1], p[2], p_type, p_anonym)

    @staticmethod
    def convert_clarketm_proxy_type(type: str) -> int:
        if type == 'S':
            return PROTOCOL_HTTPS

        return PROTOCOL_HTTP

    @staticmethod
    def convert_clarketm_proxy_anonymity(anonymity: str) -> bool:
        if anonymity == 'N':
            return False

        return True

    @staticmethod
    def convert_fateproxy_type(type: str) -> int:
        if type == 'http':
            return PROTOCOL_HTTP
        if type == 'https':
            return PROTOCOL_HTTPS

        return PROTOCOL_NONE

    @staticmethod
    def convert_fateproxy_anonymity(anonymity: str) -> bool:
        if anonymity == 'anonymous' or anonymity == 'high_anonymous':
            return True

        return False

    def add_proxy(self, ip: str, port: int, protocol: str, anonymity: bool):
        """
        Adding a loaded proxy to the proxy list
        """

        new_proxy = Proxy(ip, port, protocol, anonymity)

        if new_proxy not in self.__proxy_list:
            self.__proxy_list.append(new_proxy)

    @staticmethod
    def _get_url(proxy_url: str):
        r = requests.get(proxy_url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
            })

        return r.text

    @property
    def protocol(self):
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol=PROTOCOL_HTTP):
        self.__protocol = protocol

    @property
    def anonymity(self):
        return self.__anonymity

    @anonymity.setter
    def anonymity(self, anonymity=False):
        self.__anonymity = anonymity

    @property
    def proxy_list(self):
        return self.__proxy_list

    @proxy_list.setter
    def proxy_list(self, proxy_list=[]):
        self.__proxy_list = proxy_list
