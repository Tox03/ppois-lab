# -*- coding: utf-8 -*-
"""Модуль журнала действий и аудита системы."""

from lab3.network.core.user_account import UserAccount


class AuditLog:
    """Фиксирует административные и критические действия в системе."""

    def __init__(
        self,
        log_id: str,
        action: str,
        actor_id: str,
        target_id: str,
        timestamp: str = "2026-01-01",
    ) -> None:
        """Инициализация записи журнала аудита."""
        self.log_id = log_id
        self.action = action
        self.actor_id = actor_id
        self.target_id = target_id
        self.timestamp = timestamp

    def format_log_entry(self) -> str:
        """Форматирует строковое представление события аудита."""
        return f"[{self.timestamp}] Актор {self.actor_id} выполнил '{self.action}' над {self.target_id}"

    def is_action_critical(self) -> bool:
        """Определяет, относится ли операция к потенциально деструктивным."""
        critical_keywords = ("ban", "delete", "purge", "revoke", "block")
        return any(keyword in self.action.lower() for keyword in critical_keywords)

    def matches_actor(self, user: UserAccount) -> bool:
        """Проверяет совпадение исполнителя действия с аккаунтом."""
        return user.user_id == self.actor_id
