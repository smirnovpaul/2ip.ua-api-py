# -*- coding: utf-8 -*-
from collections import defaultdict
from netaddr import IPNetwork, AddrFormatError

from api import IpAddressApiInfo


def providers_by_ips(ips):
    """
    Формирование словаря Компаний и количества IP-адресов.

    Учитываются локальные адреса:
    IPv4: 10.0.0.0/8
          172.16.0.0/12
          192.168.0.0/16
    IPv6: fc00::/7

    Происходит валидация IP-адреса.

    ARGUMENTS:
        :param list ips:
        :return: dict
    """
    companies = defaultdict(int)
    for ip in set(ips):
        try:
            ip = IPNetwork(ip)
            local = ip.is_private()
            name_company = "Local IP" if local else get_provider(ip.ip)
        except AddrFormatError:
            name_company = "Invalid IP"
        companies[name_company] += 1
    return companies


def get_provider(ip):
    """
    Имя компании, которой принадлежит IP-адрес.

    ARGUMENTS:
        :param str ip: IPv4, IPv6
        :return str
    """
    provider_info = IpAddressApiInfo(ip=ip).get_provider
    try:
        provider_name = provider_info["name_ripe"]
    except KeyError:
        provider_name = "Unknown"
    return provider_name
