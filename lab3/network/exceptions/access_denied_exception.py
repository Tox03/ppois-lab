# -*- coding: utf-8 -*-
"""Исключение отказа в доступе."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class AccessDeniedException(NetworkBaseException):
    """Вызывается при попытке доступа к приватному или заблокированному ресурсу."""

    def __init__(self, resource: str = "ресурс") -> None:
        """Инициализация исключения отказа в доступе."""
        self.resource = resource
        super().__init__(f"Доступ к ресурсу '{resource}' ограничен настройками приватности", 403)
