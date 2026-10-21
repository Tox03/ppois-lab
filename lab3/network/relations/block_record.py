# -*- coding: utf-8 -*-
"""Модуль записи блокировки (черного списка)."""

from lab3.network.core.user_account import UserAccount


class BlockRecord:
    """Представляет запись о блокировке нежелательного пользователя."""

    def __init__(
        self,
        blocker_id: str,
        blocked_id: str,
        reason: str = "спам",
        created_at: str = "2026-01-01",
        is_active: bool = True,
    ) -> None:
        """Инициализация записи о блокировке."""
        self.blocker_id = blocker_id
        self.blocked_id = blocked_id
        self.reason = reason
        self.created_at = created_at
        self.is_active = is_active

    def deactivate(self, blocker: UserAccount) -> None:
        """Снимает блокировку инициатором."""
        if blocker.user_id == self.blocker_id:
            self.is_active = False

    def matches_pair(self, u1: str, u2: str) -> bool:
        """Проверяет, соответствует ли пара пользователей данной блокировке."""
        return self.is_active and (self.blocker_id == u1 and self.blocked_id == u2)

    def format_block_notice(self) -> str:
        """Формирует уведомление о причине внесения в черный список."""
        return f"Пользователь {self.blocked_id} заблокирован по причине: {self.reason}"

    def activate(self, blocker: UserAccount) -> None:
        """Повторно активирует блокировку инициатором."""
        if blocker.user_id == self.blocker_id:
            self.is_active = True
