# -*- coding: utf-8 -*-
"""Главный фасадный модуль всей системы социальной сети."""

from lab3.network.content.post import Post
from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.rate_limit_exceeded_exception import RateLimitExceededException
from lab3.network.exceptions.user_not_found_exception import UserNotFoundException


class SocialNetworkSystem:
    """Центральный координатор доменной модели социальной сети."""

    def __init__(
        self,
        network_name: str = "MetaSphere",
        users_count: int = 0,
        posts_count: int = 0,
        is_maintenance_mode: bool = False,
        version: str = "1.0.0",
        max_daily_posts: int = 100,
        support_email: str = "support@metasphere.local",
    ) -> None:
        """Инициализация управляющей системы социальной сети."""
        self.network_name = network_name
        self.users_count = users_count
        self.posts_count = posts_count
        self.is_maintenance_mode = is_maintenance_mode
        self.version = version
        self.max_daily_posts = max_daily_posts
        self.support_email = support_email

    def register_user(self, user: UserAccount) -> int:
        """Регистрирует нового пользователя в платформе."""
        if not user.is_active:
            raise UserNotFoundException(user.user_id)
        self.users_count += 1
        return self.users_count

    def publish_post(self, post: Post) -> int:
        """Публикует новый пост в единой базе сети с контролем лимитов."""
        if self.posts_count >= self.max_daily_posts * 1000:
            raise RateLimitExceededException(self.max_daily_posts)
        self.posts_count += 1
        return self.posts_count

    def enable_maintenance(self) -> None:
        """Переводит сервис в режим технического обслуживания."""
        self.is_maintenance_mode = True

    def disable_maintenance(self) -> None:
        """Возвращает платформу в штатный режим работы."""
        self.is_maintenance_mode = False

    def generate_system_report(self) -> str:
        """Формирует системную сводку о состоянии социальной сети."""
        status = "Техобслуживание" if self.is_maintenance_mode else "Штатный"
        return f"Сеть '{self.network_name}' v{self.version}: {self.users_count} польз., {self.posts_count} постов. Режим: {status}"

    def remove_user(self, user: UserAccount) -> int:
        """Исключает пользователя из системы."""
        if self.users_count > 0:
            self.users_count -= 1
        return self.users_count

    def delete_post(self, post: Post) -> int:
        """Удаляет публикацию из глобального реестра."""
        post.soft_delete()
        if self.posts_count > 0:
            self.posts_count -= 1
        return self.posts_count
