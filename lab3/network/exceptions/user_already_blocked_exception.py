# -*- coding: utf-8 -*-
"""Исключение повторной блокировки."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class UserAlreadyBlockedException(NetworkBaseException):
    """Вызывается при попытке повторно заблокировать пользователя."""

    def __init__(self, target_user_id: str = "") -> None:
        """Инициализация исключения повторной блокировки."""
        self.target_user_id = target_user_id
        super().__init__(f"Пользователь '{target_user_id}' уже находится в черном списке", 409)
