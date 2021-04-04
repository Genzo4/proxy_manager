import pytest
from proxy_manager import ProxyManager


def test_create_1():
    pm = ProxyManager(load_fate_proxy=False)
    assert pm.protocol == 'http'
    assert not pm.anonymity
    assert pm.proxy_list == []


def test_create_2():
    pm = ProxyManager('https', True, load_fate_proxy=False)
    assert pm.protocol == 'https'
    assert pm.anonymity
    assert pm.proxy_list == []


def test_add_proxy_1():
    pm = ProxyManager(load_fate_proxy=False)
    pm._add_proxy('1.2.3.4', '1234', 'http', False)
    assert pm.proxy_list[0].ip == '1.2.3.4'
    assert pm.proxy_list[0].port == '1234'
    assert pm.proxy_list[0].protocol == 'http'
    assert not pm.proxy_list[0].anonymity


def test_add_proxy_2():
    pm = ProxyManager(load_fate_proxy=False)
    pm._add_proxy('4.3.2.1', '234', 'https', True)
    assert pm.proxy_list[0].ip == '4.3.2.1'
    assert pm.proxy_list[0].port == '234'
    assert pm.proxy_list[0].protocol == 'https'
    assert pm.proxy_list[0].anonymity


def test_add_proxy_3():
    pm = ProxyManager(load_fate_proxy=False)

    pm._add_proxy('1.2.3.4', '1234', 'http', False)
    assert pm.proxy_list[0].ip == '1.2.3.4'
    assert pm.proxy_list[0].port == '1234'
    assert pm.proxy_list[0].protocol == 'http'
    assert not pm.proxy_list[0].anonymity

    pm._add_proxy('4.3.2.1', '234', 'https', True)
    assert pm.proxy_list[1].ip == '4.3.2.1'
    assert pm.proxy_list[1].port == '234'
    assert pm.proxy_list[1].protocol == 'https'
    assert pm.proxy_list[1].anonymity


