# -*- coding: utf-8 -*-
"""Модуль пользовательских интерфейсных настроек."""


class UserSettings:
    """Хранит персональные интерфейсные предпочтения и каналы уведомлений."""

    def __init__(
        self,
        language: str = "ru",
        theme: str = "dark",
        email_notifications: bool = True,
        push_notifications: bool = True,
        sound_enabled: bool = True,
    ) -> None:
        """Инициализация настроек интерфейса пользователя."""
        self.language = language
        self.theme = theme
        self.email_notifications = email_notifications
        self.push_notifications = push_notifications
        self.sound_enabled = sound_enabled

    def switch_theme(self, new_theme: str) -> str:
        """Переключает цветовую схему оформления интерфейса."""
        if new_theme in ("light", "dark", "system"):
            self.theme = new_theme
        return self.theme

    def toggle_push(self) -> bool:
        """Инвертирует разрешение отправки push-уведомлений."""
        self.push_notifications = not self.push_notifications
        return self.push_notifications

    def change_language(self, lang_code: str) -> None:
        """Изменяет локаль пользовательского интерфейса."""
        if len(lang_code) == 2 and lang_code.isalpha():
            self.language = lang_code.lower()
