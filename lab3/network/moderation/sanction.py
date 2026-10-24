# -*- coding: utf-8 -*-
"""Модуль дисциплинарной санкции к пользователю."""

from lab3.network.core.user_account import UserAccount


class Sanction:
    """Представляет ограничение (бан, мут, предупреждение), наложенное на аккаунт."""

    def __init__(
        self,
        sanction_id: str,
        user_id: str,
        sanction_type: str = "mute",
        duration_days: int = 1,
        reason: str = "спам",
        is_revoked: bool = False,
    ) -> None:
        """Инициализация наложенной санкции."""
        self.sanction_id = sanction_id
        self.user_id = user_id
        self.sanction_type = sanction_type
        self.duration_days = duration_days
        self.reason = reason
        self.is_revoked = is_revoked

    def revoke(self) -> None:
        """Досрочно аннулирует действующую санкцию."""
        self.is_revoked = True

    def is_active_sanction(self, user: UserAccount) -> bool:
        """Проверяет актуальность санкции в отношении конкретного пользователя."""
        return user.user_id == self.user_id and not self.is_revoked and self.duration_days > 0

    def extend_duration(self, extra_days: int) -> int:
        """Продлевает срок действия наложенного ограничения."""
        self.duration_days += max(0, extra_days)
        return self.duration_days

    def apply_sanction(self) -> None:
        """Повторно активирует ранее снятую санкцию."""
        self.is_revoked = False
