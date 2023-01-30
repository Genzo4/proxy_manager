import pytest
from proxy_manager_g4 import ProxyManager
from time import sleep
from proxy_manager_g4.consts import PROTOCOL_NONE, PROTOCOL_HTTP, PROTOCOL_HTTPS


def test_create_1():
    pm = ProxyManager(load_fate_proxy=False)
    assert pm.protocol == PROTOCOL_HTTP
    assert not pm.anonymity
    assert pm.proxy_list == []


def test_create_2():
    pm = ProxyManager(PROTOCOL_HTTPS, True, load_fate_proxy=False)
    assert pm.protocol == PROTOCOL_HTTPS
    assert pm.anonymity
    assert pm.proxy_list == []


def test_add_proxy_1():
    pm = ProxyManager(load_fate_proxy=False)
    pm._add_proxy('1.2.3.4', 1234, PROTOCOL_HTTP, False)
    assert pm.proxy_list[0].ip == '1.2.3.4'
    assert pm.proxy_list[0].port == 1234
    assert pm.proxy_list[0].protocol == PROTOCOL_HTTP
    assert not pm.proxy_list[0].anonymity


def test_add_proxy_2():
    pm = ProxyManager(load_fate_proxy=False)
    pm._add_proxy('4.3.2.1', 234, PROTOCOL_HTTPS, True)
    assert pm.proxy_list[0].ip == '4.3.2.1'
    assert pm.proxy_list[0].port == 234
    assert pm.proxy_list[0].protocol == PROTOCOL_HTTPS
    assert pm.proxy_list[0].anonymity


def test_add_proxy_3():
    pm = ProxyManager(load_fate_proxy=False)

    pm._add_proxy('1.2.3.4', 1234, PROTOCOL_HTTP, False)
    assert pm.proxy_list[0].ip == '1.2.3.4'
    assert pm.proxy_list[0].port == 1234
    assert pm.proxy_list[0].protocol == PROTOCOL_HTTP
    assert not pm.proxy_list[0].anonymity

    pm._add_proxy('4.3.2.1', 234, PROTOCOL_HTTPS, True)
    assert pm.proxy_list[1].ip == '4.3.2.1'
    assert pm.proxy_list[1].port == 234
    assert pm.proxy_list[1].protocol == PROTOCOL_HTTPS
    assert pm.proxy_list[1].anonymity


def test_get_min_used_1():
    pm = ProxyManager(load_fate_proxy=False)
    assert pm._get_min_used() == -1


def test_get_min_used_2():
    pm = ProxyManager(load_fate_proxy=False)
    pm._add_proxy('1.2.3.4', 1234, PROTOCOL_HTTP, False)
    assert pm._get_min_used() == 0


def test_get_min_used_3():
    pm = ProxyManager(load_fate_proxy=False)
    pm._add_proxy('1.2.3.4', 1234, PROTOCOL_HTTP, False)
    pm._add_proxy('4.3.2.1', 234, PROTOCOL_HTTPS, True)
    pm._add_proxy('4.2.1.3', 4321, PROTOCOL_HTTPS, True)
    assert pm._get_min_used() == 0
    pm.proxy_list[0].use()
    assert pm._get_min_used() == 0
    pm.proxy_list[1].use()
    pm.proxy_list[2].use()
    assert pm._get_min_used() == 1


def test_get_min_used_5():
    pm = ProxyManager(load_fate_proxy=False)
    pm._add_proxy('1.2.3.4', 1234, PROTOCOL_HTTP, False)
    pm._add_proxy('4.3.2.1', 234, PROTOCOL_HTTPS, True)
    pm._add_proxy('4.2.1.3', 4321, PROTOCOL_HTTPS, True)
    pm.proxy_list[1].use()
    pm.proxy_list[2].use()
    assert pm._get_min_used() == 0
    pm.proxy_list[0].use()
    assert pm._get_min_used() == 1
    pm.proxy_list[2].use()
    pm.proxy_list[0].use()
    assert pm._get_min_used() == 1
    pm.proxy_list[1].use()
    assert pm._get_min_used() == 2


def test_get_next_candidats():
    pm = ProxyManager(load_fate_proxy=False)
    candidats = pm._get_next_candidats()
    assert len(candidats) == 0

    pm = ProxyManager(load_fate_proxy=False)
    pm._add_proxy('1.2.3.4', 1234, PROTOCOL_HTTP, False)
    pm._add_proxy('4.3.2.1', 234, PROTOCOL_HTTPS, True)
    pm._add_proxy('4.2.1.3', 4321, PROTOCOL_HTTPS, True)
    candidats = pm._get_next_candidats()
    assert len(candidats) == 3
    assert pm.proxy_list[0] == candidats[0]
    assert pm.proxy_list[1] == candidats[1]
    assert pm.proxy_list[2] == candidats[2]

    pm.proxy_list[1].use()
    candidats = pm._get_next_candidats()
    assert len(candidats) == 2
    assert pm.proxy_list[0] == candidats[0]
    assert pm.proxy_list[2] == candidats[1]

    pm.proxy_list[0].use()
    candidats = pm._get_next_candidats()
    assert len(candidats) == 1
    assert pm.proxy_list[2] == candidats[0]

    pm.proxy_list[2].use()
    candidats = pm._get_next_candidats()
    assert len(candidats) == 3
    assert pm.proxy_list[0] == candidats[0]
    assert pm.proxy_list[1] == candidats[1]
    assert pm.proxy_list[2] == candidats[2]


def test_get_random_1():
    # Проверка на выдуачу None при пустом списке
    pm = ProxyManager(load_fate_proxy=False)
    assert pm.get_random() is None

    # Проверка на выдачу разных прокси

    pm = ProxyManager(load_fate_proxy=False)
    pm._add_proxy('1.2.3.4', 1234, PROTOCOL_HTTP, False)
    pm._add_proxy('4.3.2.1', 234, PROTOCOL_HTTPS, True)
    pm._add_proxy('4.2.1.3', 4321, PROTOCOL_HTTPS, True)

    proxy = pm.get_random()
    assert proxy in pm.proxy_list
    i_1 = pm.proxy_list.index(proxy)

    proxy = pm.get_random()
    assert proxy in pm.proxy_list
    i_2 = pm.proxy_list.index(proxy)
    assert i_2 != i_1

    proxy = pm.get_random()
    assert proxy in pm.proxy_list
    i_3 = pm.proxy_list.index(proxy)
    assert i_3 != i_2 and i_3 != i_1

    proxy = pm.get_random()
    assert proxy in pm.proxy_list


def test_get_random_2():
    """
    Проверка get_random на выдачу случайных результатов
    """

    proxys = []
    kolvo_otl = 0   # Количество отличающихся элементов

    for i in range(10):
        pm = ProxyManager(load_fate_proxy=False)
        pm._add_proxy('1.2.3.4', 1234, PROTOCOL_HTTP, False)
        pm._add_proxy('4.3.2.1', 234, PROTOCOL_HTTPS, True)
        pm._add_proxy('4.2.1.3', 4321, PROTOCOL_HTTPS, True)
        pm._add_proxy('4.4.4.4', 4444, PROTOCOL_HTTPS, True)
        pm._add_proxy('5.5.5.5', 5555, PROTOCOL_HTTPS, True)

        proxy = pm.get_random()
        j = pm.proxy_list.index(proxy)
        if j not in proxys:
            kolvo_otl += 1
        proxys.append(j)

    assert kolvo_otl >= 3


def test_convert_fateproxy_type():
    pm = ProxyManager()

    assert pm.convert_fateproxy_type('http') == PROTOCOL_HTTP
    assert pm.convert_fateproxy_type('https') == PROTOCOL_HTTPS
    assert pm.convert_fateproxy_type('ht') == PROTOCOL_NONE


def test_convert_fateproxy_anonymity():
    pm = ProxyManager()

    assert pm.convert_fateproxy_anonymity('anonymous') == True
    assert pm.convert_fateproxy_anonymity('high_anonymous') == True
    assert pm.convert_fateproxy_anonymity('transparent') == False
    assert pm.convert_fateproxy_anonymity('hz') == False


def test_load_list_from_fateproxy():
    pm = ProxyManager(protocol=PROTOCOL_HTTP, anonymity=False, load_fate_proxy=True)
    assert len(pm.proxy_list) > 0
    for p in pm.proxy_list:
        assert p.protocol == PROTOCOL_HTTP
        assert not p.anonymity

    sleep(2)

    pm = ProxyManager(protocol=PROTOCOL_HTTP, anonymity=True, load_fate_proxy=True)
    assert len(pm.proxy_list) > 0
    for p in pm.proxy_list:
        assert p.protocol == PROTOCOL_HTTP
        assert p.anonymity

    sleep(1)

    pm = ProxyManager(protocol=PROTOCOL_HTTPS, anonymity=True, load_fate_proxy=True)
    assert len(pm.proxy_list) > 0
    for p in pm.proxy_list:
        assert p.protocol == PROTOCOL_HTTPS
        assert p.anonymity

    sleep(2)

    with pytest.raises(UnboundLocalError):
        pm = ProxyManager(protocol=PROTOCOL_HTTPS, anonymity=False, load_fate_proxy=True)

        if len(pm.proxy_list) > 0:
            for p in pm.proxy_list:
                assert p.protocol == PROTOCOL_HTTPS
                assert not p.anonymity

    sleep(1)

    with pytest.raises(UnboundLocalError):
        pm = ProxyManager(protocol='htt', anonymity=False, load_fate_proxy=True)
