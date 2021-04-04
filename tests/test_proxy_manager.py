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
