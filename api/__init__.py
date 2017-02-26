# -*- coding: utf-8 -*-
import logging
import requests

# В случае логгирования в папку OS Windows '/'; OS Linux '\'
FORMAT = "%(asctime)s [%(levelname)s] [%(filename)s %(lineno)d] %(funcName)s: %(message)s"
FILE_NAME = "log/log.log"
LOGGER = logging.basicConfig(format=FORMAT, level=logging.DEBUG, filename=FILE_NAME)


class IpAddressApiInfo(object):
    def __init__(self, email=None, ip=None, site=None, timeout=6):
        """
        Описание доступных методов API.
        Ограничено 100 запросами с одного IP-адреса.

        https://2ip.ua/ru/api/our-api

        ARGUMENTS:
            :param None | str email
            :param None | str ip
            :param None | str site
        """
        self.url = "http://api.2ip.ua/"
        self.api = None
        self.timeout = timeout
        self.message = "Получение информации в JSON формате"

        self.email = email
        self.ip = ip
        self.site = site

    def __connect(self, payload):
        """
        ARGUMENTS:
            :param dict payload:
            :return:
        """
        try:
            r = requests.get(''.join((self.url, self.api)), params=payload, timeout=self.timeout)
        except (requests.RequestException, requests.Timeout) as e:
            LOGGER.error("Ошибка выполнения запроса {}: {}".format(self.message, e))
            return None

        try:
            r.raise_for_status()
        except requests.HTTPError as e:
            LOGGER.error("Ошибка выполнения запроса {}: {}".format(self.message, e))
            return None

        try:
            json = r.json()
        except ValueError as e:
            LOGGER.error("Ошибка выполнения запроса {}: {}".format(self.message, e))
            return None
        else:
            return json

    def basic_method_api(self, api, message):
        """
        Базовый метод для расширения функционала API.

        ARGUMENTS:
            :param str api:
            :param str message:
        """
        payload = {}
        self.api = api
        self.message = message
        return self.__connect(payload)

    @property
    def provider(self):
        """
        Получение информации о провайдере данного IP-адреса.

        При отсутствии "self.ip" вернется информацию об IP-адресе,
        с которого происходит обращение.

        ARGUMENTS:
            :return json

        Пример ОТВЕТА:
            {
                "ip":"5.1.5.1",
                "name_ripe":"PJSC \"Datagroup\"",
                "name_rus":"\u0427\u0410\u041e \"\u0414\u0430\u0442\u0430\u0433\u0440\u0443\u043f\"",
                "site":"http:\/\/www.domtele.com\/",
                "as":"21219",
                "ip_range_start":"83951616",
                "ip_range_end":"83959807",
                "route":"5.1.0.0",
                "mask":"19"
            }

        name_ripe — официальное название провайдера в базе данных Internet Routing Registry (IRR);
        name_rus — название провайдера/бренд на русском;
        site — сайт провайдера;
        as — номер автономной системы провайдера;
        ip_range_start — числовое значение (iptolong) первого IP-адреса сети провайдера;
        ip_range_end — числовое значение (iptolong) последнего IP-адреса сети провайдера;
        route — сеть провайдера;
        mask — маска сети провайдера.
        """
        payload = {"ip": self.ip}
        self.api = "provider.json"
        return self.__connect(payload)

    @property
    def geo(self):
        """
        Получение информации о предположительных геоданных данного IP-адреса.

        При отсутствии "self.ip" вернется информацию об IP-адресе,
        с которого происходит обращение.

        ARGUMENTS:
            :return json

        Пример ОТВЕТА:
        {
            "ip":"8.8.8.8",
            "country_code":"US",
            "country":"United states",
            "country_rus":"\u0421\u0428\u0410\r",
            "region":"California",
            "region_rus":"\u041a\u0430\u043b\u0438\u0444\u043e\u0440\u043d\u0438\u044f",
            "city":"Mountain view",
            "city_rus":"\u041c\u0430\u0443\u043d\u0442\u0438\u043d-\u0412\u044c\u044e",
            "latitude":"37.405992",
            "longitude":"-122.078515",
            "zip_code":"94043",
            "time_zone":"-07:00"
        }

        country_code — 2-х символьный идентификатор страны по стандарту ISO 3166-1;
        country — название страны на английском языке;
        country_rus — название страны на русском языке;
        region — название региона на английском языке;
        region_rus — название региона на русском языке;
        city — название населенного пункта (города) на английском языке;
        city_rus — название населенного пункта (города) на русском языке;
        latitude — географическая широта;
        longitude — географическая долгота;
        zip_code — почтовый индекс;
        time_zone — часовой пояс.
        """
        payload = {"ip": self.ip}
        self.api = "geo.json"
        return self.__connect(payload)

    @property
    def hosting(self):
        """
        Информация о хостинге.

        ARGUMENTS:
            :return: json

        Пример ОТВЕТА:
        {
            "name_ripe":"Mail.Ru LLC",
            "name_rus":"\u041e\u041e\u041e \"\u041c\u044d\u0439\u043b.\u0420\u0443\"",
            "site":"https:\/\/mail.ru\/"
        }

        name_ripe — официальное название хостинг провайдера в базе данных Internet Routing Registry (IRR);
        site — сайт хостинг провайдера;
        """
        payload = {"site": self.site}
        self.api = "hosting.json"
        return self.__connect(payload)

    @property
    def check_email(self):
        """
        Существование email.

        ARGUMENTS:
            :return: bool
        """
        payload = {"email": self.email}
        self.api = "email.txt"
        return self.__connect(payload)
