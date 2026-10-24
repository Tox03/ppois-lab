# -*- coding: utf-8 -*-
"""Исключение дублирования дружбы."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class FriendshipAlreadyExistsException(NetworkBaseException):
    """Вызывается при повторной отправке заявки в друзья или существующей дружбе."""

    def __init__(self, user_pair: str = "") -> None:
        """Инициализация исключения дублирования дружбы."""
        self.user_pair = user_pair
        super().__init__(f"Связь дружбы уже существует или ожидает подтверждения: {user_pair}", 409)
