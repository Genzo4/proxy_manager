import pytest
from proxy_manager.proxy import Proxy
from random import Random


def test_create_1():
    proxy = Proxy('1.1.1.1', '1234')
    assert proxy.ip == '1.1.1.1'
    assert proxy.port == '1234'
    assert proxy.protocol == 'http'
    assert not proxy.anonymity
    assert proxy.used == 0
    assert proxy.errors == 0


def test_create_2():
    proxy = Proxy('1.1.1.1', '1234', 'http', False)
    assert proxy.ip == '1.1.1.1'
    assert proxy.port == '1234'
    assert proxy.protocol == 'http'
    assert not proxy.anonymity
    assert proxy.used == 0
    assert proxy.errors == 0


def test_create_3():
    proxy = Proxy('1.1.1.1', '1234', 'https', True)
    assert proxy.ip == '1.1.1.1'
    assert proxy.port == '1234'
    assert proxy.protocol == 'https'
    assert proxy.anonymity
    assert proxy.used == 0
    assert proxy.errors == 0


def test_use():
    proxy = Proxy('1.1.1.1', '1234')
    assert proxy.used == 0
    proxy.use()
    assert proxy.used == 1
    proxy.use()
    assert proxy.used == 2


def test_eq():
    proxy_1 = Proxy('1.1.1.1', '1234')
    proxy_2 = Proxy('1.1.1.1', '1234')
    assert proxy_1 == proxy_2
    proxy_3 = Proxy('1.1.1.1', '124')
    assert proxy_1 != proxy_3
    proxy_4 = Proxy('1.1.2.1', '1234')
    assert proxy_1 != proxy_4
    proxy_5 = Proxy('1.1.3.1', '1334')
    assert proxy_1 != proxy_5
    rnd = Random()
    with pytest.raises(TypeError):
        proxy_1 == rnd


def test_print_proxy(capsys):
    proxy = Proxy('1.1.1.1', '1234')
    print(proxy)
    captured = capsys.readouterr()
    assert captured.out == '1.1.1.1:1234\n'
