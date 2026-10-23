# -*- coding: utf-8 -*-
"""Модуль мониторинга активности и сессий пользователя."""

from lab3.network.core.user_account import UserAccount


class UserActivity:
    """Отслеживает историю авторизаций, серию посещений и сетевой статус."""

    def __init__(
        self,
        last_login_at: str = "",
        login_streak_days: int = 0,
        total_sessions: int = 0,
        current_status: str = "offline",
        is_online: bool = False,
    ) -> None:
        """Инициализация метрик пользовательской активности."""
        self.last_login_at = last_login_at
        self.login_streak_days = login_streak_days
        self.total_sessions = total_sessions
        self.current_status = current_status
        self.is_online = is_online

    def record_login(self, account: UserAccount, timestamp: str) -> None:
        """Регистрирует новый вход в социальную сеть и обновляет серию дней."""
        if not account.is_active:
            return
        self.last_login_at = timestamp
        self.total_sessions += 1
        self.login_streak_days += 1
        self.is_online = True
        self.current_status = "online"

    def set_status(self, custom_status: str) -> None:
        """Устанавливает произвольный текстовый статус присутствия."""
        self.current_status = custom_status[:50]

    def go_offline(self) -> None:
        """Переводит пользователя в режим офлайн."""
        self.is_online = False
        self.current_status = "offline"

    def go_online(self) -> None:
        """Переводит пользователя в режим онлайн."""
        self.is_online = True
        self.current_status = "online"
