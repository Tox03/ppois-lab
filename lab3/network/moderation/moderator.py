# -*- coding: utf-8 -*-
"""Модуль модератора платформы."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.insufficient_privileges_exception import InsufficientPrivilegesException
from lab3.network.moderation.moderation_report import ModerationReport


class Moderator:
    """Сотрудник службы безопасности и модерации контента."""

    def __init__(
        self,
        moderator_id: str,
        badge_name: str = "Младший модератор",
        reports_reviewed: int = 0,
        is_head_moderator: bool = False,
        permissions_level: int = 1,
    ) -> None:
        """Инициализация профиля модератора."""
        self.moderator_id = moderator_id
        self.badge_name = badge_name
        self.reports_reviewed = reports_reviewed
        self.is_head_moderator = is_head_moderator
        self.permissions_level = permissions_level

    def review_report(self, report: ModerationReport, verdict: str) -> bool:
        """Рассматривает инцидент и закрывает жалобу вердиктом."""
        if not report.is_pending():
            return False
        report.resolve(verdict)
        self.reports_reviewed += 1
        return True

    def elevate_permissions(self, new_level: int) -> None:
        """Повышает уровень полномочий модератора."""
        if not self.is_head_moderator:
            raise InsufficientPrivilegesException("Только главный модератор может повышать права")
        self.permissions_level = max(self.permissions_level, new_level)

    def can_ban_permanently(self) -> bool:
        """Проверяет право на бессрочную блокировку пользователя."""
        return self.is_head_moderator or self.permissions_level >= 3

    def assign_badge(self, user: UserAccount, title: str) -> str:
        """Назначает почетный или служебный бейдж пользователю."""
        return f"Пользователю @{user.username} присвоен статус '{title}'"
