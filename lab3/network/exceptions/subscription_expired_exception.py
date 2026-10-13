# -*- coding: utf-8 -*-
"""Исключение истечения срока подписки."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class SubscriptionExpiredException(NetworkBaseException):
    """Вызывается при попытке доступа к премиум-функции с истекшей подпиской."""

    def __init__(self, tier_name: str = "Премиум") -> None:
        """Инициализация исключения истечения подписки."""
        self.tier_name = tier_name
        super().__init__(f"Срок действия платной подписки '{tier_name}' истек", 403)
