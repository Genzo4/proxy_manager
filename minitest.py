from proxy_manager_g4 import ProxyManager
from proxy_manager_g4.consts import PROTOCOL_HTTPS

proxy_manager = ProxyManager(protocol=PROTOCOL_HTTPS, anonymity=True)

for i in range(1, 1000):
    pr = proxy_manager.get_random()
    print(i, ": ", pr, "(", pr.used, ")")
