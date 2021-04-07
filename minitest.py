from proxy_manager import ProxyManager
from proxy_manager.consts import PROTOCOL_HTTPS

proxy_list = ProxyManager(protocol=PROTOCOL_HTTPS, anonymity=True)

for i in range(1, 1000):
    pr = proxy_list.get_random()
    print(i, ": ", pr, "(", pr.used, ")")
