# -*- coding: utf-8 -*-
"""Модуль аккаунта пользователя и учетной записи."""

import hashlib
from lab3.network.core.user_profile import UserProfile
from lab3.network.core.user_settings import UserSettings
from lab3.network.exceptions.authentication_exception import AuthenticationException


class UserAccount:
    """Содержит учетные данные, логин, пароль и статус аккаунта."""

    def __init__(
        self,
        user_id: str,
        username: str,
        password_hash: str,
        email: str,
        is_active: bool = True,
        created_at: str = "2026-01-01",
    ) -> None:
        """Инициализация учетной записи пользователя."""
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.email = email
        self.is_active = is_active
        self.created_at = created_at

    def verify_password(self, raw_password: str) -> bool:
        """Проверяет совпадение введенного пароля с хэшем."""
        computed_hash = hashlib.sha256(raw_password.encode("utf-8")).hexdigest()
        if computed_hash != self.password_hash:
            raise AuthenticationException("Введен неверный пароль аккаунта")
        return True

    def change_password(self, old_pwd: str, new_pwd: str) -> None:
        """Сменяет пароль учетной записи с валидацией текущего."""
        self.verify_password(old_pwd)
        if len(new_pwd) < 6:
            raise AuthenticationException("Длина нового пароля должна быть не менее 6 символов")
        self.password_hash = hashlib.sha256(new_pwd.encode("utf-8")).hexdigest()

    def deactivate(self) -> None:
        """Деактивирует учетную запись пользователя."""
        self.is_active = False

    def activate(self) -> None:
        """Восстанавливает активность учетной записи пользователя."""
        self.is_active = True

    def bind_profile(self, profile: UserProfile) -> str:
        """Связывает профиль с учетной записью пользователя."""
        return f"Профиль '{profile.bio[:20]}' привязан к @{self.username}"

    def bind_settings(self, settings: UserSettings) -> str:
        """Применяет персональные настройки к учетной записи."""
        return f"Настройки темы '{settings.theme}' применены к @{self.username}"
