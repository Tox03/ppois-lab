# -*- coding: utf-8 -*-
"""Модуль дружеской связи между двумя пользователями."""

from lab3.network.core.user_account import UserAccount


class Friendship:
    """Представляет установленную дружбу между двумя пользователями."""

    def __init__(
        self,
        user_a_id: str,
        user_b_id: str,
        status: str = "active",
        established_at: str = "2026-01-01",
        closeness_level: int = 1,
    ) -> None:
        """Инициализация связи дружбы."""
        self.user_a_id = user_a_id
        self.user_b_id = user_b_id
        self.status = status
        self.established_at = established_at
        self.closeness_level = closeness_level

    def increase_closeness(self) -> int:
        """Повышает уровень близости взаимодействия друзей."""
        self.closeness_level = min(5, self.closeness_level + 1)
        return self.closeness_level

    def terminate(self, initiator: UserAccount) -> None:
        """Расторгает дружбу одним из участников."""
        if initiator.user_id in (self.user_a_id, self.user_b_id):
            self.status = "terminated"

    def is_confirmed(self) -> bool:
        """Проверяет активность дружбы."""
        return self.status == "active"
