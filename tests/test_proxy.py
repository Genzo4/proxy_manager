import pytest
from proxy_manager_g4.proxy import Proxy
from random import Random
from proxy_manager_g4.consts import PROTOCOL_HTTP, PROTOCOL_HTTPS


def test_create_1():
    proxy = Proxy('1.2.3.4', 1234)
    assert proxy.ip == '1.2.3.4'
    assert proxy.port == 1234
    assert proxy.protocol == PROTOCOL_HTTP
    assert not proxy.anonymity
    assert proxy.used == 0
    assert proxy.errors == 0


def test_create_2():
    proxy = Proxy('1.2.3.4', 1234, PROTOCOL_HTTP, False)
    assert proxy.ip == '1.2.3.4'
    assert proxy.port == 1234
    assert proxy.protocol == PROTOCOL_HTTP
    assert not proxy.anonymity
    assert proxy.used == 0
    assert proxy.errors == 0


def test_create_3():
    proxy = Proxy('1.2.3.4', 1234, PROTOCOL_HTTPS, True)
    assert proxy.ip == '1.2.3.4'
    assert proxy.port == 1234
    assert proxy.protocol == PROTOCOL_HTTPS
    assert proxy.anonymity
    assert proxy.used == 0
    assert proxy.errors == 0


def test_use():
    proxy = Proxy('1.2.3.4', 1234)
    assert proxy.used == 0
    proxy.use()
    assert proxy.used == 1
    proxy.use()
    assert proxy.used == 2


def test_eq():
    proxy_1 = Proxy('1.2.3.4', 1234)
    proxy_2 = Proxy('1.2.3.4', 1234)
    assert proxy_1 == proxy_2
    proxy_3 = Proxy('1.2.3.4', 124)
    assert proxy_1 != proxy_3
    proxy_4 = Proxy('1.1.2.1', 1234)
    assert proxy_1 != proxy_4
    proxy_5 = Proxy('1.1.3.1', 1334)
    assert proxy_1 != proxy_5
    rnd = Random()
    with pytest.raises(TypeError):
        proxy_1 == rnd


def test_print_proxy(capsys):
    proxy = Proxy('1.2.3.4', 1234)
    print(proxy)
    captured = capsys.readouterr()
    assert captured.out == '1.2.3.4:1234\n'


def test_get_ip_port():
    proxy = Proxy('1.2.3.4', 1234)
    assert proxy.get_ip_port() == '1.2.3.4:1234'
