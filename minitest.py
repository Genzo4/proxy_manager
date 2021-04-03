from proxy_manager import ProxyManager

proxy_list = ProxyManager(protocol="https", anonymity=True)

for i in range(1, 1000):
    pr = proxy_list.get_random()
    print(i, ": ", pr, "(", pr.used, ")")
