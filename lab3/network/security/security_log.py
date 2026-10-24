# -*- coding: utf-8 -*-
"""Модуль журнала событий информационной безопасности."""

from lab3.network.core.user_account import UserAccount


class SecurityLog:
    """Регистрирует попытки входа, смены паролей и потенциальные угрозы."""

    def __init__(
        self,
        event_id: str,
        user_id: str,
        ip_address: str,
        event_name: str = "login_success",
        status: str = "ok",
        timestamp: str = "2026-01-01",
    ) -> None:
        """Инициализация записи журнала безопасности."""
        self.event_id = event_id
        self.user_id = user_id
        self.ip_address = ip_address
        self.event_name = event_name
        self.status = status
        self.timestamp = timestamp

    def is_suspicious(self) -> bool:
        """Выявляет признаки вредоносной активности (подбор пароля, брутфорс)."""
        suspicious_events = ("brute_force_detected", "password_failed_repeated", "ip_blacklisted")
        return self.event_name in suspicious_events or self.status == "blocked"

    def format_audit_string(self) -> str:
        """Форматирует строку отчета для офицера ИБ."""
        return f"[{self.timestamp}] IP={self.ip_address} User={self.user_id} Event={self.event_name}:{self.status}"

    def flag_failed_attempt(self, user: UserAccount) -> None:
        """Фиксирует неудачную попытку доступа к аккаунту."""
        self.user_id = user.user_id
        self.event_name = "login_failed"
        self.status = "warning"
