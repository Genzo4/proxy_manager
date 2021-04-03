import pytest
from proxy_manager.proxy import Proxy


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
