class Proxy:
    """
    Класс описывающий прокси сервер
    """

    def __init__(self, ip: str, port: str, protocol="http", anonymity=False):
        self.__ip = ip
        self.__port = port
        self.__protocol = protocol
        self.__anonymity = anonymity
        self.__used = 0
        self.__errors = 0

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, ip: str):
        self.__ip = ip

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

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

    @property
    def used(self) -> int:
        return self.__used

    @used.setter
    def used(self, used: int):
        self.__used = used if used > 0 else 0

    @property
    def errors(self) -> int:
        return self.__errors

    @errors.setter
    def errors(self, errors: int):
        self.__errors = errors if errors > 0 else 0

    def __str__(self):
        """Overrides the default implementation"""
        return ":".join((self.ip, str(self.port)))

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Proxy):
            return self.ip == other.ip and self.port == other.port
        return NotImplemented
