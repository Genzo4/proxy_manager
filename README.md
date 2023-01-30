![Language](https://img.shields.io/badge/English-brigthgreen)

# Proxy Manager

![PyPI](https://img.shields.io/pypi/v/proxy-manager-g4)
![PyPI - License](https://img.shields.io/pypi/l/proxy-manager-g4)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/proxy-manager-g4)

Proxy manager to download a list of proxy servers from the Internet with the required parameters 
(protocol and degree of anonymity) and work with loading servers (for example, getting a random
proxy servers from this list).

***

## Installation

### Package Installation from PyPi

```bash
$ pip3 install proxy-manager-g4
```

### Package Installation from Source Code

The source code is available on [GitHub](https://github.com/Genzo4/proxy_manager).  
Download and install the package.

```bash
$ git clone https://github.com/Genzo4/proxy_manager
$ cd proxy_manager
$ pip3 install .
```

***

## Basic usage

Import:
```python
from proxy_manager_g4 import ProxyManager
from proxy_manager_g4.consts import PROTOCOL_HTTPS
```

We create an instance of the proxy manager. At the same time, loading a list of proxy servers from the Internet 
with the required parameters (protocol and degree of anonymity).
```python
proxy_manager = ProxyManager(protocol=PROTOCOL_HTTPS, anonymity=True)
```

Get random proxy:
```python
proxy = proxy_manager.get_random()
```

When getting a random proxy server multiple times, proxy manager will track the number of uses of each
proxy for uniform delivery.  

Using the received proxy server:
```python
proxy.ip                # "1.2.3.4"
proxy.port              # 8080
proxy.get_ip_port()     # "1.2.3.4:8080"
print(proxy)            # "1.2.3.4:8080"
```

Usage example in file minitest.py

[Changelog](https://github.com/Genzo4/proxy_manager/blob/main/CHANGELOG.md)

***

The list of proxy servers is loaded from 
- [https://github.com/fate0/proxylist/](https://github.com/fate0/proxylist/)
- [https://github.com/clarketm/proxy-list/](https://github.com/clarketm/proxy-list/)

***

![Language](https://img.shields.io/badge/Русский-brigthgreen)

# Proxy Manager

![PyPI](https://img.shields.io/pypi/v/proxy-manager-g4)
![PyPI - License](https://img.shields.io/pypi/l/proxy-manager-g4)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/proxy-manager-g4)

Прокси менеджер для загрузки из интернета списка прокси серверов с требуемыми параметрами 
(протокол и степень анонимности) и работы с загруженными серверами (например, получение случайного 
прокси-сервера из данного списка).

***

## Установка

### Установка пакета с PyPi

```bash
$ pip3 install proxy-manager-g4
```

### Установка пакета из исходного кода

Исходный код размещается на [GitHub](https://github.com/Genzo4/proxy_manager).  
Скачайте его и установите пакет:

```bash
$ git clone https://github.com/Genzo4/proxy_manager
$ cd proxy_manager
$ pip3 install .
```

***

## Использование

Подключаем:
```python
from proxy_manager_g4 import ProxyManager
from proxy_manager_g4.consts import PROTOCOL_HTTPS
```

Создаём экземпляр прокси менеджера. При этом происходит загрузка списка прокси-серверов из интернета 
с требуемыми параметрами: протокол и степень анонимности.
```python
proxy_manager = ProxyManager(protocol=PROTOCOL_HTTPS, anonymity=True)
```

Получение случайного прокси-сервера из списка:
```python
proxy = proxy_manager.get_random()
```
При многократном получении случайного прокси-сервера, прокси менеджер будет отслеживать количество использований 
каждого прокси для равномерной выдачи.  

Использование полученного прокси-сервера:
```python
proxy.ip                # "1.2.3.4"
proxy.port              # 8080
proxy.get_ip_port()     # "1.2.3.4:8080"
print(proxy)            # "1.2.3.4:8080"
```

Пример использования см. в файле minitest.py

[Changelog](https://github.com/Genzo4/proxy_manager/blob/main/CHANGELOG.md)

***

Загрузка списка прокси-серверов осуществляется с 
- [https://github.com/fate0/proxylist/](https://github.com/fate0/proxylist/)
- [https://github.com/clarketm/proxy-list/](https://github.com/clarketm/proxy-list/)

