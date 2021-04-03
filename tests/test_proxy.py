import pytest
from proxy_manager.proxy import Proxy


def test_create_1():
    proxy = Proxy('1.1.1.1', '1234')
    assert proxy.ip == '1.1.1.1'
    assert proxy.port == '1234'
    assert proxy.protocol == 'http'
    assert not proxy.anonymity


def test_create_2():
    proxy = Proxy('1.1.1.1', '1234', 'http', False)
    assert proxy.ip == '1.1.1.1'
    assert proxy.port == '1234'
    assert proxy.protocol == 'http'
    assert not proxy.anonymity


def test_use():
    proxy = Proxy('1.1.1.1', '1234')
    proxy.use()

    assert proxy.used == 1
