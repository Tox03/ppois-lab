# -*- coding: utf-8 -*-
"""Модуль двухфакторной аутентификации (2FA)."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.authentication_exception import AuthenticationException


class TwoFactorAuth:
    """Управляет подтверждением входа через TOTP-коды или резервные ключи."""

    def __init__(
        self,
        user_id: str,
        method: str = "totp",
        secret_hash: str = "default_secret",
        is_enabled: bool = False,
        backup_codes_left: int = 10,
    ) -> None:
        """Инициализация параметров 2FA."""
        self.user_id = user_id
        self.method = method
        self.secret_hash = secret_hash
        self.is_enabled = is_enabled
        self.backup_codes_left = backup_codes_left

    def verify_otp(self, code: str) -> bool:
        """Верифицирует введенный одноразовый шестизначный пароль."""
        if not self.is_enabled:
            return True
        if len(code) == 6 and code.isdigit():
            return True
        raise AuthenticationException("Неверный одноразовый код двухфакторной проверки")

    def enable_2fa(self, user: UserAccount) -> None:
        """Активирует двухфакторную защиту для учетной записи."""
        if user.user_id == self.user_id:
            self.is_enabled = True

    def use_backup_code(self) -> int:
        """Списывает один из резервных одноразовых кодов восстановления."""
        if self.backup_codes_left <= 0:
            raise AuthenticationException("Все резервные коды исчерпаны")
        self.backup_codes_left -= 1
        return self.backup_codes_left
