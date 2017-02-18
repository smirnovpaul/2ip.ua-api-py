# API. **IpAddressApiInfo**
[Описание доступных методов API](https://2ip.ua/ru/api/our-api)

* Инициализация: **email**, **ip**, **site** - параметры не являются обязательными.
* **basic\_method\_api**: базовый метод для расширения функционала

## Логирование

Возможно переопределить базовые параметры.

## Доступные методы:

* **get\_provider**: информация о принадлежности IP-адреса

Ответ *Unicode*:
```json
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
```

*name\_ripe* — официальное название провайдера в базе данных Internet Routing Registry (IRR);
*name\_rus* — название провайдера/бренд на русском;
*site* — сайт провайдера;
*as* — номер автономной системы провайдера;
*ip\_range\_start* — числовое значение (iptolong) первого IP-адреса сети провайдера (в IP на основе netaddr, IPNetwork);
*ip\_range\_end* — числовое значение (iptolong) последнего IP-адреса сети провайдера (в IP на основе netaddr, IPNetwork);
*route* — сеть провайдера;
*mask* — маска сети провайдера.

* **get\_geo**: информация о предположительных геоданных IP-адреса

Ответ *Unicode*:
```json
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
```

*country\_code* — 2-х символьный идентификатор страны по стандарту ISO 3166-1;
*country* — название страны на английском языке;
*country\_rus* — название страны на русском языке;
*region* — название региона на английском языке;
*region\_rus* — название региона на русском языке;
*city* — название населенного пункта (города) на английском языке;
*city\_rus* — название населенного пункта (города) на русском языке;
*latitude* — географическая широта;
*longitude* — географическая долгота;
*zip\_code* — почтовый индекс;
*time\_zone* — часовой пояс.

* **get\_hosting**: информация о хостинге сайта

Ответ *Unicode*:
```json
{
    "name_ripe":"Mail.Ru LLC",
    "name_rus":"\u041e\u041e\u041e \"\u041c\u044d\u0439\u043b.\u0420\u0443\"",
    "site":"https:\/\/mail.ru\/"
}
```

*name\_ripe* — официальное название хостинг провайдера в базе данных Internet Routing Registry (IRR);
*site* — сайт хостинг провайдера.

* **check\_email**: проверка существования электронного ящика

Ответ *Unicode*:
```json
True/False
```
