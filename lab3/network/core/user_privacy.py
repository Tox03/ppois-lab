# -*- coding: utf-8 -*-
"""Модуль управления приватностью пользователя."""

from lab3.network.exceptions.access_denied_exception import AccessDeniedException


class UserPrivacy:
    """Определяет параметры видимости профиля и ограничения доступа."""

    def __init__(
        self,
        profile_visibility: str = "public",
        allow_messages_from_strangers: bool = True,
        show_online_status: bool = True,
        blocked_users_count: int = 0,
        searchable_by_phone: bool = False,
    ) -> None:
        """Инициализация настроек приватности."""
        self.profile_visibility = profile_visibility
        self.allow_messages_from_strangers = allow_messages_from_strangers
        self.show_online_status = show_online_status
        self.blocked_users_count = blocked_users_count
        self.searchable_by_phone = searchable_by_phone

    def set_visibility(self, visibility_level: str) -> None:
        """Устанавливает уровень видимости страницы (public, friends_only, private)."""
        valid_levels = ("public", "friends_only", "private")
        if visibility_level not in valid_levels:
            raise AccessDeniedException(f"Недопустимый уровень видимости: {visibility_level}")
        self.profile_visibility = visibility_level

    def can_receive_message_from(self, is_friend: bool) -> bool:
        """Проверяет, разрешено ли получение входящего сообщения."""
        if self.allow_messages_from_strangers:
            return True
        return is_friend

    def toggle_online_status(self) -> bool:
        """Переключает видимость сетевого статуса (онлайн)."""
        self.show_online_status = not self.show_online_status
        return self.show_online_status
