# **2ip.ua-api-py**

**API** для получения информации о IP-адресе, сайте, электронной почте без **танца с бубнами**.

### Поддержка

* **Python 2.7.x/3.x**
* **Django > 1.6**
* **Flask > 0.8**

Реализованне методы API (ответ в **json**):

* **get\_provider**: информация о принадлежности IP-адреса
* **get\_geo**: информация о предположительных геоданных IP-адреса
* **get\_hosting**: информация о хостинге сайта
* **check\_email**: проверка существования электронного ящика

Дополнительные возможности **utils**:

* **providers\_by\_ips()**: информация о провайдерах на основе IP-адресов с валидацией и проверкой на локальные

[Официальный сайт](https://2ip.ua/ru)

[Описание доступного API](https://2ip.ua/ru/api/our-api)

### Установка:

```sh
git clone https://github.com/smirnovpaul/2ip.ua-api-py.git
cd 2ip.ua-api-py
pip install -r requirements.txt
```

Лицензия
----
MIT


### Пример:

Инициализация:

```python
from api import IpAddressApiInfo
from utils import providers_by_ips

# получаем список интересующих IP-адресов
ip = ['10.0.0.0', '192.168.1.10', '8.8.8.8',
      '100.100.100.1', '101.25.25.25', '192.168.1.1',
      '172.169.0.0.', '1444.0101', '5.45.65.4',
      '32.32.32.8', '54.79.44.1']

providers_by_ips(ip)
```

Ответ:
```json
{
    "Google Inc.": 1,
    "Invalid_ip": 2,
    "CNC Group": 1,
    "Serverius Holding B.V.": 1,
    "Amazon.com Inc.": 1,
    "Local IP": 4,
    "AT&T Inc.": 1
}
```

* Invalid\_ip - Невалидный IP-адрес;
* Locals\_ip - Локальные IP-адреса.
