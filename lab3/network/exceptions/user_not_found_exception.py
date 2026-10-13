# -*- coding: utf-8 -*-
"""Исключение при отсутствии пользователя."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class UserNotFoundException(NetworkBaseException):
    """Вызывается, если пользователь не найден в системе."""

    def __init__(self, user_id: str = "unknown") -> None:
        """Инициализация исключения отсутствия пользователя."""
        self.user_id = user_id
        super().__init__(f"Пользователь с идентификатором '{user_id}' не найден", 404)
