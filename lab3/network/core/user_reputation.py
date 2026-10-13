# -*- coding: utf-8 -*-
"""Модуль репутации и кармы пользователя."""

from lab3.network.core.user_account import UserAccount


class UserReputation:
    """Управляет очками кармы, уровнем доверия и предупреждениями."""

    def __init__(
        self,
        karma_points: int = 0,
        warnings_count: int = 0,
        trust_level: str = "neutral",
        is_shadow_banned: bool = False,
        badge_title: str = "Новичок",
    ) -> None:
        """Инициализация репутации пользователя."""
        self.karma_points = karma_points
        self.warnings_count = warnings_count
        self.trust_level = trust_level
        self.is_shadow_banned = is_shadow_banned
        self.badge_title = badge_title

    def add_karma(self, amount: int, account: UserAccount) -> int:
        """Начисляет очки кармы за полезную активность."""
        if account.is_active and not self.is_shadow_banned:
            self.karma_points += max(0, amount)
            self.calculate_trust_rank()
        return self.karma_points

    def deduct_karma(self, amount: int) -> int:
        """Списывает очки кармы за нарушения."""
        self.karma_points -= max(0, amount)
        self.calculate_trust_rank()
        return self.karma_points

    def issue_warning(self) -> int:
        """Выносит предупреждение пользователю и может назначить теневой бан."""
        self.warnings_count += 1
        if self.warnings_count >= 3:
            self.is_shadow_banned = True
        self.calculate_trust_rank()
        return self.warnings_count

    def calculate_trust_rank(self) -> str:
        """Пересчитывает категорию благонадежности пользователя."""
        if self.warnings_count >= 3 or self.karma_points < -20:
            self.trust_level = "untrusted"
            self.badge_title = "Нарушитель"
        elif self.karma_points >= 100:
            self.trust_level = "trusted"
            self.badge_title = "Активист"
        else:
            self.trust_level = "neutral"
            self.badge_title = "Пользователь"
        return self.trust_level
