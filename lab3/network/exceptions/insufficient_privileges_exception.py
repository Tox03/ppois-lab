# -*- coding: utf-8 -*-
"""Исключение нехватки прав доступа."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class InsufficientPrivilegesException(NetworkBaseException):
    """Вызывается при нехватке полномочий модератора или администратора."""

    def __init__(self, action: str = "действие") -> None:
        """Инициализация исключения нехватки прав."""
        self.action = action
        super().__init__(f"Недостаточно прав для выполнения действия: '{action}'", 403)
