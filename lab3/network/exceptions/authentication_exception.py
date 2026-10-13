# -*- coding: utf-8 -*-
"""Исключение аутентификации."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class AuthenticationException(NetworkBaseException):
    """Вызывается при неверном пароле или недействительном токене."""

    def __init__(self, reason: str = "Неверные учетные данные") -> None:
        """Инициализация исключения аутентификации."""
        self.reason = reason
        super().__init__(f"Ошибка аутентификации: {reason}", 401)
