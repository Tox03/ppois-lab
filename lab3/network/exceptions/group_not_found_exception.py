# -*- coding: utf-8 -*-
"""Исключение отсутствия сообщества."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class GroupNotFoundException(NetworkBaseException):
    """Вызывается при поиске несуществующего сообщества или группы."""

    def __init__(self, group_id: str = "unknown") -> None:
        """Инициализация исключения отсутствия группы."""
        self.group_id = group_id
        super().__init__(f"Сообщество с идентификатором '{group_id}' не найдено", 404)
