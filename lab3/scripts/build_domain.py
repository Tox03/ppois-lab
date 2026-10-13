# -*- coding: utf-8 -*-
"""Скрипт генерации исходных файлов доменной модели социальной сети."""

import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "network"))

FILES = {}

# ---------------------------------------------------------------------------
# ИСКЛЮЧЕНИЯ (lab3/network/exceptions/)
# ---------------------------------------------------------------------------

FILES["exceptions/network_base_exception.py"] = '''# -*- coding: utf-8 -*-
"""Базовое исключение доменной модели социальной сети."""


class NetworkBaseException(Exception):
    """Базовый класс для всех ошибок и исключений социальной сети."""

    def __init__(self, message: str = "Ошибка социальной сети", code: int = 500) -> None:
        """Инициализация базового исключения."""
        super().__init__(message)
        self.message = message
        self.code = code
'''

FILES["exceptions/user_not_found_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение при отсутствии пользователя."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class UserNotFoundException(NetworkBaseException):
    """Вызывается, если пользователь не найден в системе."""

    def __init__(self, user_id: str = "unknown") -> None:
        """Инициализация исключения отсутствия пользователя."""
        self.user_id = user_id
        super().__init__(f"Пользователь с идентификатором '{user_id}' не найден", 404)
'''

FILES["exceptions/authentication_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение аутентификации."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class AuthenticationException(NetworkBaseException):
    """Вызывается при неверном пароле или недействительном токене."""

    def __init__(self, reason: str = "Неверные учетные данные") -> None:
        """Инициализация исключения аутентификации."""
        self.reason = reason
        super().__init__(f"Ошибка аутентификации: {reason}", 401)
'''

FILES["exceptions/access_denied_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение отказа в доступе."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class AccessDeniedException(NetworkBaseException):
    """Вызывается при попытке доступа к приватному или заблокированному ресурсу."""

    def __init__(self, resource: str = "ресурс") -> None:
        """Инициализация исключения отказа в доступе."""
        self.resource = resource
        super().__init__(f"Доступ к ресурсу '{resource}' ограничен настройками приватности", 403)
'''

FILES["exceptions/content_not_found_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение отсутствия контента."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class ContentNotFoundException(NetworkBaseException):
    """Вызывается при попытке найти несуществующую публикацию, историю или комментарий."""

    def __init__(self, content_id: str = "unknown") -> None:
        """Инициализация исключения отсутствия контента."""
        self.content_id = content_id
        super().__init__(f"Элемент контента '{content_id}' не найден", 404)
'''

FILES["exceptions/content_blocked_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение блокировки контента модерацией."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class ContentBlockedException(NetworkBaseException):
    """Вызывается при обращении к материалу, заблокированному модератором."""

    def __init__(self, content_id: str = "unknown", reason: str = "нарушение правил") -> None:
        """Инициализация исключения блокировки контента."""
        self.content_id = content_id
        self.reason = reason
        super().__init__(f"Контент '{content_id}' заблокирован по причине: {reason}", 451)
'''

FILES["exceptions/invalid_content_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение некорректного контента."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class InvalidContentException(NetworkBaseException):
    """Вызывается при нарушении формата текста, длины или недопустимых символах."""

    def __init__(self, details: str = "Некорректное содержимое") -> None:
        """Инициализация исключения некорректного контента."""
        self.details = details
        super().__init__(f"Недопустимое содержимое публикации: {details}", 400)
'''

FILES["exceptions/friendship_already_exists_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение дублирования дружбы."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class FriendshipAlreadyExistsException(NetworkBaseException):
    """Вызывается при повторной отправке заявки в друзья или существующей дружбе."""

    def __init__(self, user_pair: str = "") -> None:
        """Инициализация исключения дублирования дружбы."""
        self.user_pair = user_pair
        super().__init__(f"Связь дружбы уже существует или ожидает подтверждения: {user_pair}", 409)
'''

FILES["exceptions/user_already_blocked_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение повторной блокировки."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class UserAlreadyBlockedException(NetworkBaseException):
    """Вызывается при попытке повторно заблокировать пользователя."""

    def __init__(self, target_user_id: str = "") -> None:
        """Инициализация исключения повторной блокировки."""
        self.target_user_id = target_user_id
        super().__init__(f"Пользователь '{target_user_id}' уже находится в черном списке", 409)
'''

FILES["exceptions/group_not_found_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение отсутствия сообщества."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class GroupNotFoundException(NetworkBaseException):
    """Вызывается при поиске несуществующего сообщества или группы."""

    def __init__(self, group_id: str = "unknown") -> None:
        """Инициализация исключения отсутствия группы."""
        self.group_id = group_id
        super().__init__(f"Сообщество с идентификатором '{group_id}' не найдено", 404)
'''

FILES["exceptions/group_capacity_exceeded_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение превышения лимита участников группы."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class GroupCapacityExceededException(NetworkBaseException):
    """Вызывается при попытке вступить в переполненную группу или чат."""

    def __init__(self, max_limit: int = 1000) -> None:
        """Инициализация исключения переполнения группы."""
        self.max_limit = max_limit
        super().__init__(f"Превышен лимит участников группы: максимум {max_limit}", 400)
'''

FILES["exceptions/insufficient_privileges_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение нехватки прав доступа."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class InsufficientPrivilegesException(NetworkBaseException):
    """Вызывается при нехватке полномочий модератора или администратора."""

    def __init__(self, action: str = "действие") -> None:
        """Инициализация исключения нехватки прав."""
        self.action = action
        super().__init__(f"Недостаточно прав для выполнения действия: '{action}'", 403)
'''

FILES["exceptions/payment_failed_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение ошибки платежа."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class PaymentFailedException(NetworkBaseException):
    """Вызывается при неудачном списании средств или недостатке баланса."""

    def __init__(self, reason: str = "Недостаточно средств") -> None:
        """Инициализация исключения платежа."""
        self.reason = reason
        super().__init__(f"Транзакция отклонена: {reason}", 402)
'''

FILES["exceptions/subscription_expired_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение истечения срока подписки."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class SubscriptionExpiredException(NetworkBaseException):
    """Вызывается при попытке доступа к премиум-функции с истекшей подпиской."""

    def __init__(self, tier_name: str = "Премиум") -> None:
        """Инициализация исключения истечения подписки."""
        self.tier_name = tier_name
        super().__init__(f"Срок действия платной подписки '{tier_name}' истек", 403)
'''

FILES["exceptions/report_already_processed_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение повторной обработки жалобы."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class ReportAlreadyProcessedException(NetworkBaseException):
    """Вызывается при попытке повторно вынести решение по закрытой жалобе."""

    def __init__(self, report_id: str = "") -> None:
        """Инициализация исключения повторной обработки жалобы."""
        self.report_id = report_id
        super().__init__(f"Жалоба '{report_id}' уже рассмотрена модератором", 409)
'''

FILES["exceptions/rate_limit_exceeded_exception.py"] = '''# -*- coding: utf-8 -*-
"""Исключение превышения лимита активности."""

from lab3.network.exceptions.network_base_exception import NetworkBaseException


class RateLimitExceededException(NetworkBaseException):
    """Вызывается при превышении допустимого лимита запросов или сообщений."""

    def __init__(self, limit: int = 60) -> None:
        """Инициализация исключения лимита запросов."""
        self.limit = limit
        super().__init__(f"Превышен допустимый лимит активности: максимум {limit} в минуту", 429)
'''

# ---------------------------------------------------------------------------
# CORE (lab3/network/core/)
# ---------------------------------------------------------------------------

FILES["core/contact_info.py"] = '''# -*- coding: utf-8 -*-
"""Модуль контактных данных пользователя."""

from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class ContactInfo:
    """Хранит контактную информацию и геолокационные данные профиля."""

    def __init__(
        self,
        phone: str = "",
        city: str = "",
        country: str = "",
        telegram_handle: str = "",
        is_phone_confirmed: bool = False,
    ) -> None:
        """Инициализация контактных реквизитов пользователя."""
        self.phone = phone
        self.city = city
        self.country = country
        self.telegram_handle = telegram_handle
        self.is_phone_confirmed = is_phone_confirmed

    def confirm_phone(self, code: str) -> bool:
        """Подтверждает телефонный номер проверочным SMS-кодом."""
        if len(code) == 6 and code.isdigit():
            self.is_phone_confirmed = True
            return True
        return False

    def format_location(self) -> str:
        """Формирует текстовое представление местоположения пользователя."""
        if self.city and self.country:
            return f"{self.city}, {self.country}"
        return self.city or self.country or "Не указано"

    def update_phone(self, new_phone: str) -> None:
        """Обновляет телефонный номер с предварительной валидацией."""
        if not new_phone.startswith("+") or len(new_phone) < 8:
            raise InvalidContentException("Номер телефона должен начинаться с '+' и содержать не менее 8 цифр")
        self.phone = new_phone
        self.is_phone_confirmed = False
'''

FILES["core/user_privacy.py"] = '''# -*- coding: utf-8 -*-
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
'''

FILES["core/user_settings.py"] = '''# -*- coding: utf-8 -*-
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
'''

FILES["core/user_profile.py"] = '''# -*- coding: utf-8 -*-
"""Модуль анкетных данных и профиля пользователя."""

from lab3.network.core.contact_info import ContactInfo
from lab3.network.core.user_privacy import UserPrivacy


class UserProfile:
    """Представляет публичный профиль участника социальной сети."""

    def __init__(
        self,
        bio: str = "",
        website: str = "",
        birth_date: str = "",
        avatar_url: str = "",
        is_verified: bool = False,
    ) -> None:
        """Инициализация профиля пользователя."""
        self.bio = bio
        self.website = website
        self.birth_date = birth_date
        self.avatar_url = avatar_url
        self.is_verified = is_verified

    def update_bio(self, text: str, privacy: UserPrivacy) -> None:
        """Обновляет текст биографии с проверкой прав доступа."""
        if len(text) > 300:
            self.bio = text[:300]
        else:
            self.bio = text

    def verify_profile(self, document_confirmed: bool) -> bool:
        """Присваивает официальную галочку верификации профилю."""
        if document_confirmed:
            self.is_verified = True
        return self.is_verified

    def format_profile_card(self, contact: ContactInfo) -> str:
        """Формирует текстовую визитку профиля с контактными данными."""
        verified_mark = " [✓]" if self.is_verified else ""
        location = contact.format_location()
        return f"Профиль{verified_mark}: {self.bio} | Локация: {location}"
'''

FILES["core/user_account.py"] = '''# -*- coding: utf-8 -*-
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
'''

FILES["core/user_activity.py"] = '''# -*- coding: utf-8 -*-
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
'''

FILES["core/user_reputation.py"] = '''# -*- coding: utf-8 -*-
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
'''

# ---------------------------------------------------------------------------
# CONTENT (lab3/network/content/)
# ---------------------------------------------------------------------------

FILES["content/reaction.py"] = '''# -*- coding: utf-8 -*-
"""Модуль пользовательских реакций на контент."""

from lab3.network.core.user_account import UserAccount


class Reaction:
    """Представляет эмоциональную реакцию пользователя на пост или комментарий."""

    def __init__(
        self,
        reaction_type: str = "like",
        user_id: str = "",
        target_id: str = "",
        created_at: str = "2026-01-01",
    ) -> None:
        """Инициализация реакции пользователя."""
        self.reaction_type = reaction_type
        self.user_id = user_id
        self.target_id = target_id
        self.created_at = created_at

    def update_type(self, new_type: str, user: UserAccount) -> None:
        """Изменяет тип реакции (like, love, haha, wow, sad, angry)."""
        valid_types = ("like", "love", "haha", "wow", "sad", "angry")
        if new_type in valid_types and user.user_id == self.user_id:
            self.reaction_type = new_type

    def is_positive(self) -> bool:
        """Определяет, выражает ли реакция положительные эмоции."""
        return self.reaction_type in ("like", "love", "haha", "wow")

    def get_emoji(self) -> str:
        """Возвращает соответствующий текстовый эмодзи."""
        emojis = {
            "like": "👍",
            "love": "❤️",
            "haha": "😄",
            "wow": "😮",
            "sad": "😢",
            "angry": "😡",
        }
        return emojis.get(self.reaction_type, "👍")
'''

FILES["content/hashtag.py"] = '''# -*- coding: utf-8 -*-
"""Модуль тематических хэштегов."""

from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class Hashtag:
    """Хранит информацию о поисковом хэштеге и частоте его использования."""

    def __init__(
        self,
        tag_name: str,
        usage_count: int = 1,
        trending_score: float = 0.0,
        is_blacklisted: bool = False,
    ) -> None:
        """Инициализация хэштега."""
        self.tag_name = tag_name.lower().lstrip("#")
        self.usage_count = usage_count
        self.trending_score = trending_score
        self.is_blacklisted = is_blacklisted

    def increment_usage(self) -> int:
        """Увеличивает счетчик цитируемости хэштега."""
        if self.is_blacklisted:
            raise InvalidContentException(f"Хэштег #{self.tag_name} заблокирован")
        self.usage_count += 1
        return self.usage_count

    def update_trend_score(self, new_posts_last_hour: int) -> float:
        """Пересчитывает показатель трендовости на основе динамики публикаций."""
        self.trending_score = round(self.usage_count * 0.2 + new_posts_last_hour * 1.5, 2)
        return self.trending_score

    def validate_tag(self) -> bool:
        """Проверяет допустимость символов в названии тега."""
        if not self.tag_name or " " in self.tag_name or len(self.tag_name) > 50:
            raise InvalidContentException("Хэштег не должен содержать пробелов и превышать 50 знаков")
        return True
'''

FILES["content/media_attachment.py"] = '''# -*- coding: utf-8 -*-
"""Модуль медиавложений публикаций."""

from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class MediaAttachment:
    """Описывает прикрепленный медиафайл (фотография, видеоролик, документ)."""

    def __init__(
        self,
        attachment_id: str,
        file_url: str,
        file_size_bytes: int,
        mime_type: str = "image/jpeg",
        width: int = 1920,
        height: int = 1080,
    ) -> None:
        """Инициализация медиавложения."""
        self.attachment_id = attachment_id
        self.file_url = file_url
        self.file_size_bytes = file_size_bytes
        self.mime_type = mime_type
        self.width = width
        self.height = height

    def is_image(self) -> bool:
        """Проверяет, является ли вложение изображением."""
        return self.mime_type.startswith("image/")

    def is_video(self) -> bool:
        """Проверяет, является ли вложение видеозаписью."""
        return self.mime_type.startswith("video/")

    def format_file_size(self) -> str:
        """Форматирует размер файла в удобочитаемый вид (КБ / МБ)."""
        if self.file_size_bytes < 1024 * 1024:
            return f"{round(self.file_size_bytes / 1024, 1)} КБ"
        return f"{round(self.file_size_bytes / (1024 * 1024), 2)} МБ"
'''

FILES["content/poll_option.py"] = '''# -*- coding: utf-8 -*-
"""Модуль варианта ответа в опросе."""


class PollOption:
    """Представляет отдельный вариант ответа в голосовании."""

    def __init__(
        self,
        option_id: str,
        option_text: str,
        votes_count: int = 0,
        percentage: float = 0.0,
    ) -> None:
        """Инициализация пункта опроса."""
        self.option_id = option_id
        self.option_text = option_text
        self.votes_count = votes_count
        self.percentage = percentage

    def increment_vote(self) -> int:
        """Увеличивает счетчик голосов за данный пункт."""
        self.votes_count += 1
        return self.votes_count

    def update_percentage(self, total_votes: int) -> float:
        """Вычисляет долю голосов в процентах от общего числа участников."""
        if total_votes > 0:
            self.percentage = round((self.votes_count / total_votes) * 100.0, 1)
        else:
            self.percentage = 0.0
        return self.percentage

    def format_label(self) -> str:
        """Формирует текстовую подпись варианта с числом голосов."""
        return f"{self.option_text} ({self.votes_count} гол., {self.percentage}%)"
'''

FILES["content/post.py"] = '''# -*- coding: utf-8 -*-
"""Базовый модуль публикации (поста)."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.content_blocked_exception import ContentBlockedException
from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class Post:
    """Представляет запись на стене пользователя или в ленте социальной сети."""

    def __init__(
        self,
        post_id: str,
        author_id: str,
        text_content: str,
        created_at: str = "2026-01-01",
        is_pinned: bool = False,
        is_deleted: bool = False,
    ) -> None:
        """Инициализация публикации."""
        self.post_id = post_id
        self.author_id = author_id
        self.text_content = text_content
        self.created_at = created_at
        self.is_pinned = is_pinned
        self.is_deleted = is_deleted

    def pin(self, author: UserAccount) -> bool:
        """Закрепляет публикацию вверху ленты профиля."""
        if author.user_id != self.author_id:
            return False
        self.is_pinned = True
        return True

    def unpin(self) -> None:
        """Открепляет публикацию."""
        self.is_pinned = False

    def soft_delete(self) -> None:
        """Помечает публикацию удаленной."""
        self.is_deleted = True

    def edit_content(self, new_text: str, author: UserAccount) -> None:
        """Редактирует текст записи с проверкой авторства."""
        if self.is_deleted:
            raise ContentBlockedException(self.post_id, "Публикация уже удалена")
        if author.user_id != self.author_id:
            raise InvalidContentException("Редактировать запись может только автор")
        self.text_content = new_text
'''

FILES["content/text_post.py"] = '''# -*- coding: utf-8 -*-
"""Модуль текстовой публикации (статьи)."""

from lab3.network.content.post import Post


class TextPost:
    """Специализированная текстовая запись с расширенным оформлением."""

    def __init__(
        self,
        post_id: str,
        font_style: str = "sans-serif",
        background_color: str = "#FFFFFF",
        reading_time_minutes: int = 1,
        word_count: int = 0,
        summary: str = "",
    ) -> None:
        """Инициализация статьи."""
        self.post_id = post_id
        self.font_style = font_style
        self.background_color = background_color
        self.reading_time_minutes = reading_time_minutes
        self.word_count = word_count
        self.summary = summary

    def calculate_reading_time(self, post: Post) -> int:
        """Рассчитывает ориентировочное время чтения статьи."""
        words = len(post.text_content.split())
        self.word_count = words
        self.reading_time_minutes = max(1, words // 200)
        return self.reading_time_minutes

    def generate_summary(self, post: Post) -> str:
        """Генерирует краткую аннотацию из первого предложения записи."""
        sentences = post.text_content.split(". ")
        self.summary = sentences[0] if sentences else post.text_content[:100]
        return self.summary

    def apply_styling(self, font: str, bg: str) -> None:
        """Настраивает визуальные параметры шрифта и подложки статьи."""
        self.font_style = font
        self.background_color = bg
'''

FILES["content/media_post.py"] = '''# -*- coding: utf-8 -*-
"""Модуль медиа-публикации."""

from lab3.network.content.media_attachment import MediaAttachment
from lab3.network.content.post import Post


class MediaPost:
    """Публикация, содержащая фотографии или видеогалерею."""

    def __init__(
        self,
        post_id: str,
        aspect_ratio: str = "16:9",
        has_watermark: bool = False,
        media_count: int = 0,
        alt_description: str = "",
        filter_preset: str = "normal",
    ) -> None:
        """Инициализация медиа-поста."""
        self.post_id = post_id
        self.aspect_ratio = aspect_ratio
        self.has_watermark = has_watermark
        self.media_count = media_count
        self.alt_description = alt_description
        self.filter_preset = filter_preset

    def add_media_item(self, media: MediaAttachment) -> int:
        """Добавляет медиа-элемент в публикацию и обновляет счетчик."""
        self.media_count += 1
        return self.media_count

    def apply_filter(self, preset_name: str) -> str:
        """Применяет цветовой фильтр ко всем прикрепленным изображениям."""
        self.filter_preset = preset_name
        return self.filter_preset

    def verify_attachments(self, base_post: Post) -> bool:
        """Проверяет корректность привязки медиа к базовой публикации."""
        return base_post.post_id == self.post_id and self.media_count > 0
'''

FILES["content/poll_post.py"] = '''# -*- coding: utf-8 -*-
"""Модуль интерактивного опроса."""

from lab3.network.content.poll_option import PollOption
from lab3.network.content.post import Post
from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class PollPost:
    """Публикация с голосованием и вариантами ответов."""

    def __init__(
        self,
        post_id: str,
        question: str,
        is_anonymous: bool = True,
        is_closed: bool = False,
        max_choices: int = 1,
        total_votes: int = 0,
    ) -> None:
        """Инициализация опроса."""
        self.post_id = post_id
        self.question = question
        self.is_anonymous = is_anonymous
        self.is_closed = is_closed
        self.max_choices = max_choices
        self.total_votes = total_votes

    def close_poll(self) -> None:
        """Завершает прием голосов в опросе."""
        self.is_closed = True

    def add_vote(self, option: PollOption) -> int:
        """Учитывает голос пользователя за выбранный вариант."""
        if self.is_closed:
            raise InvalidContentException("Голосование уже завершено")
        option.increment_vote()
        self.total_votes += 1
        return self.total_votes

    def calculate_results(self, options: list) -> None:
        """Пересчитывает проценты для всех вариантов ответа."""
        for opt in options:
            if isinstance(opt, PollOption):
                opt.update_percentage(self.total_votes)

    def can_vote(self, post: Post) -> bool:
        """Проверяет доступность опроса для голосования."""
        return not self.is_closed and not post.is_deleted
'''

FILES["content/comment.py"] = '''# -*- coding: utf-8 -*-
"""Модуль комментария к публикации."""

from lab3.network.core.user_account import UserAccount
from lab3.network.content.post import Post
from lab3.network.content.reaction import Reaction


class Comment:
    """Представляет комментарий пользователя под записью."""

    def __init__(
        self,
        comment_id: str,
        post_id: str,
        author_id: str,
        text: str,
        likes_count: int = 0,
        is_hidden: bool = False,
    ) -> None:
        """Инициализация комментария."""
        self.comment_id = comment_id
        self.post_id = post_id
        self.author_id = author_id
        self.text = text
        self.likes_count = likes_count
        self.is_hidden = is_hidden

    def like(self, reaction: Reaction) -> int:
        """Регистрирует положительную реакцию на комментарий."""
        if reaction.is_positive():
            self.likes_count += 1
        return self.likes_count

    def hide(self) -> None:
        """Скрывает комментарий модератором."""
        self.is_hidden = True

    def edit_text(self, new_text: str, author: UserAccount) -> None:
        """Редактирует текст комментария автором."""
        if author.user_id == self.author_id:
            self.text = new_text
'''

FILES["content/album.py"] = '''# -*- coding: utf-8 -*-
"""Модуль фотоальбома пользователя."""

from lab3.network.content.media_attachment import MediaAttachment
from lab3.network.core.user_account import UserAccount


class Album:
    """Коллекция сохраненных фотографий и медиафайлов."""

    def __init__(
        self,
        album_id: str,
        owner_id: str,
        title: str,
        description: str = "",
        photos_count: int = 0,
        is_private: bool = False,
    ) -> None:
        """Инициализация фотоальбома."""
        self.album_id = album_id
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.photos_count = photos_count
        self.is_private = is_private

    def add_photo(self, photo: MediaAttachment, owner: UserAccount) -> int:
        """Добавляет фотоснимок в альбом с проверкой владельца."""
        if owner.user_id == self.owner_id and photo.is_image():
            self.photos_count += 1
        return self.photos_count

    def remove_photo(self) -> int:
        """Уменьшает счетчик снимков в альбоме."""
        if self.photos_count > 0:
            self.photos_count -= 1
        return self.photos_count

    def toggle_privacy(self) -> bool:
        """Переключает видимость альбома (публичный/скрытый)."""
        self.is_private = not self.is_private
        return self.is_private
'''

FILES["content/story.py"] = '''# -*- coding: utf-8 -*-
"""Модуль исчезающих историй (Stories)."""

from lab3.network.core.user_account import UserAccount


class Story:
    """Представляет короткую историю с ограниченным сроком жизни (24 часа)."""

    def __init__(
        self,
        story_id: str,
        author_id: str,
        media_url: str,
        duration_seconds: int = 15,
        views_count: int = 0,
        is_expired: bool = False,
    ) -> None:
        """Инициализация истории."""
        self.story_id = story_id
        self.author_id = author_id
        self.media_url = media_url
        self.duration_seconds = duration_seconds
        self.views_count = views_count
        self.is_expired = is_expired

    def record_view(self, viewer: UserAccount) -> int:
        """Фиксирует просмотр истории другим пользователем."""
        if not self.is_expired and viewer.user_id != self.author_id:
            self.views_count += 1
        return self.views_count

    def check_expiration(self, hours_passed: int) -> bool:
        """Проверяет истечение срока действия истории по прошедшим часам."""
        if hours_passed >= 24:
            self.is_expired = True
        return self.is_expired

    def archive(self) -> None:
        """Принудительно переводит историю в архив."""
        self.is_expired = True

    def add_interactive_sticker(self, sticker_name: str) -> str:
        """Прикрепляет интерактивный стикер к истории."""
        return f"Стикер '{sticker_name}' добавлен к истории {self.story_id}"
'''

FILES["content/story_viewer.py"] = '''# -*- coding: utf-8 -*-
"""Модуль зрителя истории."""

from lab3.network.core.user_account import UserAccount


class StoryViewer:
    """Фиксирует факт просмотра конкретной истории пользователем."""

    def __init__(
        self,
        viewer_id: str,
        story_id: str,
        viewed_at: str = "2026-01-01",
        has_reacted: bool = False,
    ) -> None:
        """Инициализация записи о просмотре истории."""
        self.viewer_id = viewer_id
        self.story_id = story_id
        self.viewed_at = viewed_at
        self.has_reacted = has_reacted

    def mark_reaction(self, user: UserAccount) -> bool:
        """Отмечает отправку реакции на историю зрителем."""
        if user.user_id == self.viewer_id:
            self.has_reacted = True
        return self.has_reacted

    def get_watch_delay(self) -> str:
        """Возвращает информацию о времени просмотра."""
        return f"Просмотрено в {self.viewed_at}"

    def format_viewer_info(self) -> str:
        """Форматирует краткую сводку о зрителе."""
        status = "с реакцией" if self.has_reacted else "без реакции"
        return f"Зритель {self.viewer_id}: {status}"
'''


# ---------------------------------------------------------------------------
# COMMUNICATION (lab3/network/communication/)
# ---------------------------------------------------------------------------

FILES["communication/direct_message.py"] = '''# -*- coding: utf-8 -*-
"""Модуль личного сообщения между пользователями."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.access_denied_exception import AccessDeniedException


class DirectMessage:
    """Представляет приватное сообщение диалога двух участников."""

    def __init__(
        self,
        message_id: str,
        sender_id: str,
        recipient_id: str,
        content: str,
        is_read: bool = False,
        is_delivered: bool = False,
    ) -> None:
        """Инициализация личного сообщения."""
        self.message_id = message_id
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.content = content
        self.is_read = is_read
        self.is_delivered = is_delivered

    def mark_as_read(self, recipient: UserAccount) -> bool:
        """Помечает сообщение прочитанным адресатом."""
        if recipient.user_id != self.recipient_id:
            raise AccessDeniedException("Только получатель может пометить сообщение как прочитанное")
        self.is_read = True
        return self.is_read

    def mark_as_delivered(self) -> None:
        """Устанавливает статус доставки сообщения на устройство."""
        self.is_delivered = True

    def format_preview(self) -> str:
        """Возвращает краткий предпросмотр сообщения для списка чатов."""
        preview = self.content[:30] + "..." if len(self.content) > 30 else self.content
        return f"[{'Проч.' if self.is_read else 'Нов.'}] {preview}"
'''

FILES["communication/chat.py"] = '''# -*- coding: utf-8 -*-
"""Модуль диалога (чата)."""


class Chat:
    """Представляет диалог в системе сообщений."""

    def __init__(
        self,
        chat_id: str,
        created_at: str = "2026-01-01",
        last_message_at: str = "2026-01-01",
        messages_count: int = 0,
        is_archived: bool = False,
    ) -> None:
        """Инициализация диалога."""
        self.chat_id = chat_id
        self.created_at = created_at
        self.last_message_at = last_message_at
        self.messages_count = messages_count
        self.is_archived = is_archived

    def archive(self) -> None:
        """Переносит диалог в архив."""
        self.is_archived = True

    def unarchive(self) -> None:
        """Извлекает диалог из архива."""
        self.is_archived = False

    def update_last_activity(self, timestamp: str) -> None:
        """Обновляет время последней активности и инкрементирует число сообщений."""
        self.last_message_at = timestamp
        self.messages_count += 1
'''

FILES["communication/chat_message.py"] = '''# -*- coding: utf-8 -*-
"""Модуль сообщения в чате."""

from lab3.network.communication.chat import Chat
from lab3.network.core.user_account import UserAccount


class ChatMessage:
    """Сообщение, отправленное внутри группового или парного чата."""

    def __init__(
        self,
        message_id: str,
        chat_id: str,
        sender_id: str,
        text: str,
        reply_to_id: str = "",
        is_pinned: bool = False,
    ) -> None:
        """Инициализация сообщения чата."""
        self.message_id = message_id
        self.chat_id = chat_id
        self.sender_id = sender_id
        self.text = text
        self.reply_to_id = reply_to_id
        self.is_pinned = is_pinned

    def pin(self, chat: Chat) -> bool:
        """Закрепляет данное сообщение в шапке чата."""
        if chat.chat_id == self.chat_id:
            self.is_pinned = True
            return True
        return False

    def unpin(self) -> None:
        """Снимает закрепление с сообщения."""
        self.is_pinned = False

    def set_reply(self, target_message_id: str, sender: UserAccount) -> None:
        """Устанавливает ссылку на цитируемое сообщение при ответе."""
        if sender.user_id == self.sender_id:
            self.reply_to_id = target_message_id
'''

FILES["communication/chat_member.py"] = '''# -*- coding: utf-8 -*-
"""Модуль участника группового чата."""

from lab3.network.core.user_account import UserAccount


class ChatMember:
    """Определяет роль и статус участника группового чата."""

    def __init__(
        self,
        member_id: str,
        chat_id: str,
        role: str = "member",
        joined_at: str = "2026-01-01",
        is_banned: bool = False,
    ) -> None:
        """Инициализация участника беседы."""
        self.member_id = member_id
        self.chat_id = chat_id
        self.role = role
        self.joined_at = joined_at
        self.is_banned = is_banned

    def promote_to_admin(self, admin_account: UserAccount) -> bool:
        """Повышает участника до администратора чата."""
        if admin_account.is_active and not self.is_banned:
            self.role = "admin"
            return True
        return False

    def demote(self) -> None:
        """Понижает статус участника до обычного."""
        self.role = "member"

    def ban(self) -> None:
        """Блокирует участника в данном чате."""
        self.is_banned = True
        self.role = "banned"
'''

FILES["communication/group_chat.py"] = '''# -*- coding: utf-8 -*-
"""Модуль групповой беседы."""

from lab3.network.communication.chat import Chat
from lab3.network.communication.chat_member import ChatMember
from lab3.network.exceptions.group_capacity_exceeded_exception import GroupCapacityExceededException


class GroupChat:
    """Управляет групповой многопользовательской беседой."""

    def __init__(
        self,
        chat_id: str,
        title: str,
        admin_id: str,
        members_limit: int = 200,
        invite_code: str = "code123",
        is_muted: bool = False,
    ) -> None:
        """Инициализация групповой беседы."""
        self.chat_id = chat_id
        self.title = title
        self.admin_id = admin_id
        self.members_limit = members_limit
        self.invite_code = invite_code
        self.is_muted = is_muted

    def add_participant(self, member: ChatMember, current_count: int) -> bool:
        """Добавляет нового участника в групповой чат с проверкой лимита."""
        if current_count >= self.members_limit:
            raise GroupCapacityExceededException(self.members_limit)
        return not member.is_banned

    def remove_participant(self, member: ChatMember) -> None:
        """Исключает участника из беседы."""
        member.ban()

    def generate_invite(self, base_chat: Chat) -> str:
        """Генерирует новую ссылку-приглашение в групповой диалог."""
        self.invite_code = f"invite_{base_chat.chat_id}_{len(self.title)}"
        return self.invite_code

    def mute(self) -> None:
        """Отключает звуковые уведомления о сообщениях группы."""
        self.is_muted = True
'''

FILES["communication/call_session.py"] = '''# -*- coding: utf-8 -*-
"""Модуль сессии голосового или видеозвонка."""

from lab3.network.core.user_account import UserAccount


class CallSession:
    """Представляет сеанс аудио- или видеозвонка между пользователями."""

    def __init__(
        self,
        call_id: str,
        initiator_id: str,
        is_video: bool = False,
        duration_seconds: int = 0,
        status: str = "ringing",
        quality_score: float = 5.0,
    ) -> None:
        """Инициализация сеанса звонка."""
        self.call_id = call_id
        self.initiator_id = initiator_id
        self.is_video = is_video
        self.duration_seconds = duration_seconds
        self.status = status
        self.quality_score = quality_score

    def start_call(self, participant: UserAccount) -> bool:
        """Начинает голосовой вызов при подтверждении собеседника."""
        if participant.is_active:
            self.status = "connected"
            return True
        self.status = "rejected"
        return False

    def end_call(self, total_seconds: int) -> int:
        """Завершает звонок и фиксирует продолжительность разговора."""
        self.duration_seconds = max(0, total_seconds)
        self.status = "ended"
        return self.duration_seconds

    def rate_quality(self, score: float) -> float:
        """Сохраняет субъективную оценку качества связи пользователем."""
        self.quality_score = max(1.0, min(5.0, score))
        return self.quality_score
'''

FILES["communication/audio_message.py"] = '''# -*- coding: utf-8 -*-
"""Модуль голосового аудиосообщения."""

from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class AudioMessage:
    """Представляет голосовое сообщение с расшифровкой речи в текст."""

    def __init__(
        self,
        audio_id: str,
        duration_seconds: int,
        audio_url: str,
        transcription: str = "",
        waveform_samples: int = 64,
    ) -> None:
        """Инициализация аудиосообщения."""
        self.audio_id = audio_id
        self.duration_seconds = duration_seconds
        self.audio_url = audio_url
        self.transcription = transcription
        self.waveform_samples = waveform_samples

    def transcribe(self, text: str) -> str:
        """Записывает распознанный текст голосового сообщения."""
        if not text:
            raise InvalidContentException("Расшифровка аудио не может быть пустой")
        self.transcription = text
        return self.transcription

    def is_long_audio(self) -> bool:
        """Определяет, превышает ли аудиозапись 2 минуты."""
        return self.duration_seconds > 120

    def format_duration(self) -> str:
        """Форматирует длительность трека в вид ММ:СС."""
        minutes = self.duration_seconds // 60
        seconds = self.duration_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
'''

# ---------------------------------------------------------------------------
# RELATIONS (lab3/network/relations/)
# ---------------------------------------------------------------------------

FILES["relations/friendship.py"] = '''# -*- coding: utf-8 -*-
"""Модуль дружеской связи между двумя пользователями."""

from lab3.network.core.user_account import UserAccount


class Friendship:
    """Представляет установленную дружбу между двумя пользователями."""

    def __init__(
        self,
        user_a_id: str,
        user_b_id: str,
        status: str = "active",
        established_at: str = "2026-01-01",
        closeness_level: int = 1,
    ) -> None:
        """Инициализация связи дружбы."""
        self.user_a_id = user_a_id
        self.user_b_id = user_b_id
        self.status = status
        self.established_at = established_at
        self.closeness_level = closeness_level

    def increase_closeness(self) -> int:
        """Повышает уровень близости взаимодействия друзей."""
        self.closeness_level = min(5, self.closeness_level + 1)
        return self.closeness_level

    def terminate(self, initiator: UserAccount) -> None:
        """Расторгает дружбу одним из участников."""
        if initiator.user_id in (self.user_a_id, self.user_b_id):
            self.status = "terminated"

    def is_confirmed(self) -> bool:
        """Проверяет активность дружбы."""
        return self.status == "active"
'''

FILES["relations/follow.py"] = '''# -*- coding: utf-8 -*-
"""Модуль подписки на пользователя (фолловинга)."""

from lab3.network.core.user_account import UserAccount


class Follow:
    """Представляет одностороннюю подписку на обновления автора."""

    def __init__(
        self,
        follower_id: str,
        target_id: str,
        started_at: str = "2026-01-01",
        notifications_enabled: bool = True,
    ) -> None:
        """Инициализация подписки."""
        self.follower_id = follower_id
        self.target_id = target_id
        self.started_at = started_at
        self.notifications_enabled = notifications_enabled

    def toggle_notifications(self) -> bool:
        """Включает или выключает уведомления о новых публикациях автора."""
        self.notifications_enabled = not self.notifications_enabled
        return self.notifications_enabled

    def get_follow_duration_days(self) -> int:
        """Возвращает примерную длительность подписки в днях."""
        return 30

    def unfollow(self, follower: UserAccount) -> bool:
        """Отменяет подписку на автора."""
        return follower.user_id == self.follower_id
'''

FILES["relations/block_record.py"] = '''# -*- coding: utf-8 -*-
"""Модуль записи блокировки (черного списка)."""

from lab3.network.core.user_account import UserAccount


class BlockRecord:
    """Представляет запись о блокировке нежелательного пользователя."""

    def __init__(
        self,
        blocker_id: str,
        blocked_id: str,
        reason: str = "спам",
        created_at: str = "2026-01-01",
        is_active: bool = True,
    ) -> None:
        """Инициализация записи о блокировке."""
        self.blocker_id = blocker_id
        self.blocked_id = blocked_id
        self.reason = reason
        self.created_at = created_at
        self.is_active = is_active

    def deactivate(self, blocker: UserAccount) -> None:
        """Снимает блокировку инициатором."""
        if blocker.user_id == self.blocker_id:
            self.is_active = False

    def matches_pair(self, u1: str, u2: str) -> bool:
        """Проверяет, соответствует ли пара пользователей данной блокировке."""
        return self.is_active and (self.blocker_id == u1 and self.blocked_id == u2)

    def format_block_notice(self) -> str:
        """Формирует уведомление о причине внесения в черный список."""
        return f"Пользователь {self.blocked_id} заблокирован по причине: {self.reason}"
'''

FILES["relations/friend_request.py"] = '''# -*- coding: utf-8 -*-
"""Модуль заявки на добавление в друзья."""

from lab3.network.core.user_account import UserAccount
from lab3.network.relations.friendship import Friendship


class FriendRequest:
    """Представляет входящую заявку на дружбу с сопроводительным сообщением."""

    def __init__(
        self,
        request_id: str,
        sender_id: str,
        receiver_id: str,
        message: str = "",
        status: str = "pending",
    ) -> None:
        """Инициализация заявки в друзья."""
        self.request_id = request_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.message = message
        self.status = status

    def accept(self, receiver: UserAccount) -> Friendship:
        """Принимает заявку и формирует взаимную дружбу."""
        if receiver.user_id == self.receiver_id:
            self.status = "accepted"
            return Friendship(self.sender_id, self.receiver_id, "active")
        return Friendship(self.sender_id, self.receiver_id, "rejected")

    def reject(self, receiver: UserAccount) -> None:
        """Отклоняет входящую заявку в друзья."""
        if receiver.user_id == self.receiver_id:
            self.status = "rejected"

    def is_pending(self) -> bool:
        """Проверяет, ожидает ли заявка ответа адресата."""
        return self.status == "pending"
'''

FILES["relations/group_membership.py"] = '''# -*- coding: utf-8 -*-
"""Модуль членства пользователя в группе."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.insufficient_privileges_exception import InsufficientPrivilegesException


class GroupMembership:
    """Определяет участие пользователя в тематическом сообществе."""

    def __init__(
        self,
        membership_id: str,
        group_id: str,
        user_id: str,
        role: str = "member",
        warning_count: int = 0,
    ) -> None:
        """Инициализация членства в группе."""
        self.membership_id = membership_id
        self.group_id = group_id
        self.user_id = user_id
        self.role = role
        self.warning_count = warning_count

    def warn_member(self) -> int:
        """Выносит предупреждение участнику за нарушение регламента группы."""
        self.warning_count += 1
        return self.warning_count

    def change_role(self, new_role: str, admin: UserAccount) -> None:
        """Изменяет статус участника администратором группы."""
        if not admin.is_active:
            raise InsufficientPrivilegesException("Администратор не активен")
        if new_role in ("member", "moderator", "admin"):
            self.role = new_role

    def is_moderator(self) -> bool:
        """Проверяет наличие прав модератора в группе."""
        return self.role in ("moderator", "admin")
'''

FILES["relations/user_group.py"] = '''# -*- coding: utf-8 -*-
"""Модуль тематического сообщества (группы)."""

from lab3.network.core.user_account import UserAccount
from lab3.network.relations.group_membership import GroupMembership


class UserGroup:
    """Представляет публичное или закрытое сообщество по интересам."""

    def __init__(
        self,
        group_id: str,
        name: str,
        description: str,
        owner_id: str,
        is_verified: bool = False,
        is_closed: bool = False,
    ) -> None:
        """Инициализация сообщества."""
        self.group_id = group_id
        self.name = name
        self.description = description
        self.owner_id = owner_id
        self.is_verified = is_verified
        self.is_closed = is_closed

    def verify_group(self) -> None:
        """Присваивает официальную отметку верификации сообществу."""
        self.is_verified = True

    def close_group(self, owner: UserAccount) -> bool:
        """Переводит группу в закрытый режим по решению владельца."""
        if owner.user_id == self.owner_id:
            self.is_closed = True
            return True
        return False

    def open_group(self) -> None:
        """Делает группу открытой для свободного вступления."""
        self.is_closed = False

    def update_info(self, new_name: str, new_desc: str) -> None:
        """Обновляет заголовок и описание страницы группы."""
        self.name = new_name
        self.description = new_desc
'''

FILES["relations/group_event.py"] = '''# -*- coding: utf-8 -*-
"""Модуль запланированного мероприятия группы."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.group_capacity_exceeded_exception import GroupCapacityExceededException


class GroupEvent:
    """Представляет встречу или онлайн-вебинар, организованный сообществом."""

    def __init__(
        self,
        event_id: str,
        group_id: str,
        title: str,
        event_date: str = "2026-06-01",
        max_attendees: int = 100,
        attendees_count: int = 0,
    ) -> None:
        """Инициализация мероприятия сообщества."""
        self.event_id = event_id
        self.group_id = group_id
        self.title = title
        self.event_date = event_date
        self.max_attendees = max_attendees
        self.attendees_count = attendees_count

    def register_attendee(self, user: UserAccount) -> int:
        """Регистрирует участника на мероприятие."""
        if self.is_full():
            raise GroupCapacityExceededException(self.max_attendees)
        if user.is_active:
            self.attendees_count += 1
        return self.attendees_count

    def cancel_attendance(self) -> int:
        """Отменяет регистрацию участника и освобождает место."""
        if self.attendees_count > 0:
            self.attendees_count -= 1
        return self.attendees_count

    def is_full(self) -> bool:
        """Проверяет, исчерпан ли лимит свободных мест на событии."""
        return self.attendees_count >= self.max_attendees
'''

# ---------------------------------------------------------------------------
# MODERATION (lab3/network/moderation/)
# ---------------------------------------------------------------------------

FILES["moderation/moderation_report.py"] = '''# -*- coding: utf-8 -*-
"""Модуль жалобы на нарушение правил."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.report_already_processed_exception import ReportAlreadyProcessedException


class ModerationReport:
    """Представляет жалобу пользователя на неприемлемый контент или поведение."""

    def __init__(
        self,
        report_id: str,
        reporter_id: str,
        target_id: str,
        reason: str = "спам",
        status: str = "pending",
        resolution: str = "",
    ) -> None:
        """Инициализация жалобы."""
        self.report_id = report_id
        self.reporter_id = reporter_id
        self.target_id = target_id
        self.reason = reason
        self.status = status
        self.resolution = resolution

    def resolve(self, action: str) -> None:
        """Выносит положительное решение по жалобе."""
        if self.status != "pending":
            raise ReportAlreadyProcessedException(self.report_id)
        self.status = "resolved"
        self.resolution = action

    def dismiss(self) -> None:
        """Отклоняет жалобу как необоснованную."""
        if self.status != "pending":
            raise ReportAlreadyProcessedException(self.report_id)
        self.status = "dismissed"
        self.resolution = "Нарушений не выявлено"

    def is_pending(self) -> bool:
        """Проверяет, ожидает ли жалоба вердикта модератора."""
        return self.status == "pending"
'''

FILES["moderation/moderator.py"] = '''# -*- coding: utf-8 -*-
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
'''

FILES["moderation/banned_word_filter.py"] = '''# -*- coding: utf-8 -*-
"""Модуль фильтра нецензурных и запрещенных выражений."""

from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class BannedWordFilter:
    """Осуществляет лексический анализ и цензурирование текста."""

    def __init__(
        self,
        banned_words_count: int = 0,
        case_sensitive: bool = False,
        replacement_symbol: str = "*",
        strict_mode: bool = True,
    ) -> None:
        """Инициализация фильтра стоп-слов."""
        self.banned_words_count = banned_words_count
        self.case_sensitive = case_sensitive
        self.replacement_symbol = replacement_symbol
        self.strict_mode = strict_mode

    def contains_banned_word(self, text: str, word_list: list) -> bool:
        """Проверяет присутствие недопустимых слов в сообщении."""
        target_text = text if self.case_sensitive else text.lower()
        for word in word_list:
            w = word if self.case_sensitive else word.lower()
            if w in target_text:
                return True
        return False

    def censor_text(self, text: str, word_list: list) -> str:
        """Заменяет запрещенные фрагменты маскирующими символами."""
        result = text
        for word in word_list:
            mask = self.replacement_symbol * len(word)
            result = result.replace(word, mask)
        return result

    def add_keyword(self, word: str) -> int:
        """Добавляет новый термин в глобальный стоп-словарь."""
        if not word.strip():
            raise InvalidContentException("Слово не может быть пустым")
        self.banned_words_count += 1
        return self.banned_words_count
'''

FILES["moderation/audit_log.py"] = '''# -*- coding: utf-8 -*-
"""Модуль журнала действий и аудита системы."""

from lab3.network.core.user_account import UserAccount


class AuditLog:
    """Фиксирует административные и критические действия в системе."""

    def __init__(
        self,
        log_id: str,
        action: str,
        actor_id: str,
        target_id: str,
        timestamp: str = "2026-01-01",
    ) -> None:
        """Инициализация записи журнала аудита."""
        self.log_id = log_id
        self.action = action
        self.actor_id = actor_id
        self.target_id = target_id
        self.timestamp = timestamp

    def format_log_entry(self) -> str:
        """Форматирует строковое представление события аудита."""
        return f"[{self.timestamp}] Актор {self.actor_id} выполнил '{self.action}' над {self.target_id}"

    def is_action_critical(self) -> bool:
        """Определяет, относится ли операция к потенциально деструктивным."""
        critical_keywords = ("ban", "delete", "purge", "revoke", "block")
        return any(k in self.action.lower() for k in critical_keywords)

    def matches_actor(self, user: UserAccount) -> bool:
        """Проверяет совпадение исполнителя действия с аккаунтом."""
        return user.user_id == self.actor_id
'''

FILES["moderation/sanction.py"] = '''# -*- coding: utf-8 -*-
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
'''

FILES["moderation/content_filter.py"] = '''# -*- coding: utf-8 -*-
"""Модуль автоматической фильтрации спама и спам-скоринга."""

from lab3.network.exceptions.content_blocked_exception import ContentBlockedException


class ContentFilter:
    """Автоматический анализатор контента на спам и нежелательный материал."""

    def __init__(
        self,
        filter_name: str = "SpamDetector",
        spam_threshold: float = 0.8,
        nsfw_detection: bool = True,
        auto_block: bool = True,
        inspections_count: int = 0,
    ) -> None:
        """Инициализация алгоритма фильтрации."""
        self.filter_name = filter_name
        self.spam_threshold = spam_threshold
        self.nsfw_detection = nsfw_detection
        self.auto_block = auto_block
        self.inspections_count = inspections_count

    def evaluate_spam_score(self, text: str) -> float:
        """Оценивает вероятность спама в текстовом фрагменте от 0.0 до 1.0."""
        self.inspections_count += 1
        suspicious_words = ("http", "скидка", "купи", "крипта", "казино", "бесплатно")
        matches = sum(1 for w in suspicious_words if w in text.lower())
        score = min(1.0, round(matches * 0.25, 2))
        return score

    def inspect_text(self, text: str, content_id: str) -> bool:
        """Проверяет текст и выбрасывает исключение при превышении порога спама."""
        score = self.evaluate_spam_score(text)
        if score >= self.spam_threshold and self.auto_block:
            raise ContentBlockedException(content_id, f"Автофильтр: превышен порог спама ({score})")
        return True

    def update_threshold(self, new_threshold: float) -> None:
        """Настраивает чувствительность детектора спама."""
        self.spam_threshold = max(0.1, min(1.0, new_threshold))
'''

FILES["moderation/appeal.py"] = '''# -*- coding: utf-8 -*-
"""Модуль апелляции пользователя на наложенную санкцию."""

from lab3.network.core.user_account import UserAccount
from lab3.network.moderation.sanction import Sanction


class Appeal:
    """Представляет заявление на обжалование блокировки или предупреждения."""

    def __init__(
        self,
        appeal_id: str,
        sanction_id: str,
        user_id: str,
        explanation: str,
        status: str = "under_review",
        reviewer_notes: str = "",
    ) -> None:
        """Инициализация апелляционного обращения."""
        self.appeal_id = appeal_id
        self.sanction_id = sanction_id
        self.user_id = user_id
        self.explanation = explanation
        self.status = status
        self.reviewer_notes = reviewer_notes

    def approve(self, sanction: Sanction, notes: str) -> None:
        """Удовлетворяет апелляцию и отменяет санкцию."""
        self.status = "approved"
        self.reviewer_notes = notes
        sanction.revoke()

    def reject(self, notes: str) -> None:
        """Отклоняет прошение о снятии ограничения."""
        self.status = "rejected"
        self.reviewer_notes = notes

    def is_under_review(self) -> bool:
        """Проверяет, находится ли обращение на стадии рассмотрения."""
        return self.status == "under_review"
'''

# ---------------------------------------------------------------------------
# MONETIZATION (lab3/network/monetization/)
# ---------------------------------------------------------------------------

FILES["monetization/subscription_tier.py"] = '''# -*- coding: utf-8 -*-
"""Модуль уровня платной подписки."""


class SubscriptionTier:
    """Описывает тарифный план авторской или платформенной подписки."""

    def __init__(
        self,
        tier_id: str,
        name: str,
        monthly_price: float,
        benefits_count: int = 1,
        badge_icon: str = "⭐",
    ) -> None:
        """Инициализация тарифного плана."""
        self.tier_id = tier_id
        self.name = name
        self.monthly_price = monthly_price
        self.benefits_count = benefits_count
        self.badge_icon = badge_icon

    def is_affordable(self, budget: float) -> bool:
        """Проверяет, достаточно ли средств пользователя для оплаты месяца."""
        return budget >= self.monthly_price

    def add_benefit(self) -> int:
        """Увеличивает число включенных преимуществ тарифа."""
        self.benefits_count += 1
        return self.benefits_count

    def format_price_tag(self) -> str:
        """Формирует ценник подписки."""
        return f"{self.name}: {self.monthly_price} руб./мес. {self.badge_icon}"
'''

FILES["monetization/subscription.py"] = '''# -*- coding: utf-8 -*-
"""Модуль пользовательской подписки на премиум-контент."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.subscription_expired_exception import SubscriptionExpiredException
from lab3.network.monetization.subscription_tier import SubscriptionTier


class Subscription:
    """Управляет активной платной подпиской на автора или сервис."""

    def __init__(
        self,
        subscription_id: str,
        user_id: str,
        creator_id: str,
        tier_name: str = "VIP",
        expires_at: str = "2026-12-31",
        auto_renew: bool = True,
    ) -> None:
        """Инициализация подписки."""
        self.subscription_id = subscription_id
        self.user_id = user_id
        self.creator_id = creator_id
        self.tier_name = tier_name
        self.expires_at = expires_at
        self.auto_renew = auto_renew

    def renew(self, tier: SubscriptionTier, new_expiry: str) -> None:
        """Продлевает срок действия подписки."""
        self.tier_name = tier.name
        self.expires_at = new_expiry

    def cancel_auto_renew(self) -> None:
        """Отключает автоматическое списание за продление."""
        self.auto_renew = False

    def is_valid(self, current_date: str) -> bool:
        """Проверяет актуальность оплаченного периода."""
        if current_date > self.expires_at:
            raise SubscriptionExpiredException(self.tier_name)
        return True
'''

FILES["monetization/ad_campaign.py"] = '''# -*- coding: utf-8 -*-
"""Модуль рекламной кампании."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.payment_failed_exception import PaymentFailedException


class AdCampaign:
    """Управляет таргетированной кампанией рекламодателя."""

    def __init__(
        self,
        campaign_id: str,
        sponsor_id: str,
        budget_total: float,
        spent_amount: float = 0.0,
        is_active: bool = True,
        daily_limit: float = 100.0,
    ) -> None:
        """Инициализация рекламной кампании."""
        self.campaign_id = campaign_id
        self.sponsor_id = sponsor_id
        self.budget_total = budget_total
        self.spent_amount = spent_amount
        self.is_active = is_active
        self.daily_limit = daily_limit

    def charge_budget(self, cost: float) -> float:
        """Списывает затраты на показы и клики из рекламного бюджета."""
        if self.spent_amount + cost > self.budget_total:
            self.is_active = False
            raise PaymentFailedException("Рекламный бюджет кампании исчерпан")
        self.spent_amount += cost
        return self.spent_amount

    def pause(self) -> None:
        """Приостанавливает показы рекламных объявлений."""
        self.is_active = False

    def resume(self) -> None:
        """Возобновляет рекламные показы."""
        if self.spent_amount < self.budget_total:
            self.is_active = True
'''

FILES["monetization/advertisement.py"] = '''# -*- coding: utf-8 -*-
"""Модуль рекламного объявления в ленте."""

from lab3.network.monetization.ad_campaign import AdCampaign


class Advertisement:
    """Представляет промо-материал, транслируемый в лентах пользователей."""

    def __init__(
        self,
        ad_id: str,
        campaign_id: str,
        title: str,
        target_url: str,
        clicks_count: int = 0,
        impressions_count: int = 0,
    ) -> None:
        """Инициализация рекламного блока."""
        self.ad_id = ad_id
        self.campaign_id = campaign_id
        self.title = title
        self.target_url = target_url
        self.clicks_count = clicks_count
        self.impressions_count = impressions_count

    def record_impression(self, campaign: AdCampaign) -> int:
        """Регистрирует факт показа объявления и списывает CPM-стоимость."""
        if campaign.is_active:
            self.impressions_count += 1
            campaign.charge_budget(0.01)
        return self.impressions_count

    def record_click(self, campaign: AdCampaign) -> int:
        """Регистрирует переход по ссылке рекламы и списывает CPC-стоимость."""
        if campaign.is_active:
            self.clicks_count += 1
            campaign.charge_budget(0.20)
        return self.clicks_count

    def calculate_ctr(self) -> float:
        """Вычисляет показатель кликабельности (Click-Through Rate, %)."""
        if self.impressions_count > 0:
            return round((self.clicks_count / self.impressions_count) * 100.0, 2)
        return 0.0
'''

FILES["monetization/wallet.py"] = '''# -*- coding: utf-8 -*-
"""Модуль виртуального кошелька пользователя."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.payment_failed_exception import PaymentFailedException


class Wallet:
    """Хранит денежный баланс и токены внутренней экономики сети."""

    def __init__(
        self,
        wallet_id: str,
        user_id: str,
        balance: float = 0.0,
        currency: str = "RUB",
        is_frozen: bool = False,
    ) -> None:
        """Инициализация электронного кошелька."""
        self.wallet_id = wallet_id
        self.user_id = user_id
        self.balance = balance
        self.currency = currency
        self.is_frozen = is_frozen

    def deposit(self, amount: float) -> float:
        """Пополняет баланс кошелька."""
        if amount <= 0:
            raise PaymentFailedException("Сумма пополнения должна быть положительной")
        self.balance += round(amount, 2)
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Списывает средства с баланса с проверкой остатка."""
        if self.is_frozen:
            raise PaymentFailedException("Кошелек заблокирован системой безопасности")
        if amount > self.balance:
            raise PaymentFailedException(f"Недостаточно средств: запрошено {amount}, доступно {self.balance}")
        self.balance -= round(amount, 2)
        return self.balance

    def freeze(self) -> None:
        """Замораживает проведение операций по кошельку."""
        self.is_frozen = True

    def unfreeze(self) -> None:
        """Размораживает баланс кошелька."""
        self.is_frozen = False
'''

FILES["monetization/transaction.py"] = '''# -*- coding: utf-8 -*-
"""Модуль денежной транзакции."""

from lab3.network.exceptions.payment_failed_exception import PaymentFailedException
from lab3.network.monetization.wallet import Wallet


class Transaction:
    """Представляет финансовый перевод между кошельками или оплату услуги."""

    def __init__(
        self,
        tx_id: str,
        sender_wallet_id: str,
        receiver_wallet_id: str,
        amount: float,
        status: str = "pending",
        fee: float = 0.0,
    ) -> None:
        """Инициализация транзакции."""
        self.tx_id = tx_id
        self.sender_wallet_id = sender_wallet_id
        self.receiver_wallet_id = receiver_wallet_id
        self.amount = amount
        self.status = status
        self.fee = fee

    def execute(self, sender: Wallet, receiver: Wallet) -> bool:
        """Исполняет финансовую транзакцию с удержанием комиссии."""
        if self.status != "pending":
            return False
        total = self.amount + self.fee
        sender.withdraw(total)
        receiver.deposit(self.amount)
        self.status = "completed"
        return True

    def refund(self, sender: Wallet, receiver: Wallet) -> None:
        """Выполняет возврат средств отправителю."""
        if self.status == "completed":
            receiver.withdraw(self.amount)
            sender.deposit(self.amount)
            self.status = "refunded"

    def calculate_fee(self, fee_percent: float = 1.5) -> float:
        """Рассчитывает комиссию платежного шлюза."""
        self.fee = round(self.amount * (fee_percent / 100.0), 2)
        return self.fee
'''

FILES["monetization/virtual_gift.py"] = '''# -*- coding: utf-8 -*-
"""Модуль виртуального подарка."""

from lab3.network.core.user_account import UserAccount
from lab3.network.monetization.wallet import Wallet


class VirtualGift:
    """Представляет подарочный стикер/сувенир, отправляемый в профиль."""

    def __init__(
        self,
        gift_id: str,
        gift_name: str,
        price_coins: int = 10,
        icon_code: str = "🎁",
        is_limited_edition: bool = False,
    ) -> None:
        """Инициализация виртуального подарка."""
        self.gift_id = gift_id
        self.gift_name = gift_name
        self.price_coins = price_coins
        self.icon_code = icon_code
        self.is_limited_edition = is_limited_edition

    def send_gift(self, sender_wallet: Wallet, recipient: UserAccount) -> bool:
        """Списывает стоимость подарка с кошелька дарителя."""
        sender_wallet.withdraw(float(self.price_coins))
        return recipient.is_active

    def format_gift_card(self) -> str:
        """Возвращает текстовое оформление подарка."""
        badge = " [Эксклюзив]" if self.is_limited_edition else ""
        return f"{self.icon_code} {self.gift_name}{badge} — {self.price_coins} монет"

    def apply_discount(self, discount_percent: int) -> int:
        """Применяет акционную скидку к стоимости подарка."""
        self.price_coins = max(1, int(self.price_coins * (100 - discount_percent) / 100))
        return self.price_coins
'''

# ---------------------------------------------------------------------------
# ANALYTICS (lab3/network/analytics/)
# ---------------------------------------------------------------------------

FILES["analytics/feed_item.py"] = '''# -*- coding: utf-8 -*-
"""Модуль элемента новостной ленты."""

from lab3.network.content.post import Post


class FeedItem:
    """Представляет публикацию внутри ранжированной пользовательской ленты."""

    def __init__(
        self,
        item_id: str,
        post_id: str,
        relevance_score: float = 1.0,
        source_type: str = "friend",
        seen: bool = False,
    ) -> None:
        """Инициализация элемента ленты."""
        self.item_id = item_id
        self.post_id = post_id
        self.relevance_score = relevance_score
        self.source_type = source_type
        self.seen = seen

    def mark_as_seen(self) -> None:
        """Помечает пост как просмотренный в ленте."""
        self.seen = True

    def boost_score(self, factor: float) -> float:
        """Повышает ранжирующий балл записи в ленте."""
        self.relevance_score = round(self.relevance_score * max(1.0, factor), 3)
        return self.relevance_score

    def penalize_score(self, penalty: float) -> float:
        """Понижает позицию записи в ленте за нерелевантность."""
        self.relevance_score = max(0.01, round(self.relevance_score - penalty, 3))
        return self.relevance_score
'''

FILES["analytics/feed.py"] = '''# -*- coding: utf-8 -*-
"""Модуль персонализированной ленты новостей."""

from lab3.network.analytics.feed_item import FeedItem
from lab3.network.core.user_account import UserAccount


class Feed:
    """Формирует и ранжирует новостную ленту для пользователя."""

    def __init__(
        self,
        user_id: str,
        algorithm_type: str = "chronological",
        items_count: int = 0,
        refresh_interval_sec: int = 60,
        include_ads: bool = True,
    ) -> None:
        """Инициализация ленты."""
        self.user_id = user_id
        self.algorithm_type = algorithm_type
        self.items_count = items_count
        self.refresh_interval_sec = refresh_interval_sec
        self.include_ads = include_ads

    def add_item(self, item: FeedItem) -> int:
        """Включает новую запись в ленту."""
        self.items_count += 1
        return self.items_count

    def filter_by_algorithm(self, user: UserAccount) -> str:
        """Применяет алгоритмическое либо хронологическое ранжирование."""
        if user.user_id == self.user_id:
            return f"Лента {self.user_id} обновлена по алгоритму {self.algorithm_type}"
        return "Чужая лента"

    def clear_feed(self) -> None:
        """Очищает кэшированные публикации в ленте."""
        self.items_count = 0
'''

FILES["analytics/recommendation_engine.py"] = '''# -*- coding: utf-8 -*-
"""Модуль рекомендательной системы."""

from lab3.network.content.post import Post
from lab3.network.core.user_account import UserAccount


class RecommendationEngine:
    """Осуществляет расчет интересов и рекомендацию контента пользователям."""

    def __init__(
        self,
        model_version: str = "v2.4",
        diversity_factor: float = 0.3,
        decay_rate: float = 0.05,
        min_score_threshold: float = 0.5,
    ) -> None:
        """Инициализация алгоритма рекомендаций."""
        self.model_version = model_version
        self.diversity_factor = diversity_factor
        self.decay_rate = decay_rate
        self.min_score_threshold = min_score_threshold

    def score_post(self, post: Post, user: UserAccount) -> float:
        """Вычисляет предсказанную заинтересованность пользователя в записи."""
        if post.is_deleted or not user.is_active:
            return 0.0
        base_score = 0.8
        return round(base_score - self.decay_rate, 2)

    def recommend_users(self, user: UserAccount, candidates: list) -> list:
        """Подбирает рекомендуемых друзей и авторов на основе сходства профилей."""
        if not user.is_active:
            return []
        return [c for c in candidates if isinstance(c, UserAccount) and c.user_id != user.user_id]

    def update_diversity(self, new_factor: float) -> None:
        """Обновляет параметр разнообразия рекомендаций (explore vs exploit)."""
        self.diversity_factor = max(0.0, min(1.0, new_factor))
'''

FILES["analytics/engagement_metrics.py"] = '''# -*- coding: utf-8 -*-
"""Модуль аналитики вовлеченности аудитории."""

from lab3.network.content.post import Post


class EngagementMetrics:
    """Агрегирует статистику просмотров, репостов, закладок и реакций."""

    def __init__(
        self,
        post_id: str,
        views: int = 0,
        likes: int = 0,
        shares: int = 0,
        bookmarks: int = 0,
        comments_count: int = 0,
    ) -> None:
        """Инициализация счетчиков вовлеченности."""
        self.post_id = post_id
        self.views = views
        self.likes = likes
        self.shares = shares
        self.bookmarks = bookmarks
        self.comments_count = comments_count

    def calculate_engagement_rate(self) -> float:
        """Рассчитывает коэффициент вовлеченности (ER, %)."""
        if self.views == 0:
            return 0.0
        interactions = self.likes + self.shares + self.bookmarks + self.comments_count
        return round((interactions / self.views) * 100.0, 2)

    def record_share(self, post: Post) -> int:
        """Фиксирует распространение записи другим пользователем."""
        if post.post_id == self.post_id:
            self.shares += 1
        return self.shares

    def record_bookmark(self) -> int:
        """Фиксирует сохранение записи в закладки."""
        self.bookmarks += 1
        return self.bookmarks
'''

FILES["analytics/user_statistic.py"] = '''# -*- coding: utf-8 -*-
"""Модуль персональной статистики активности пользователя."""

from lab3.network.core.user_account import UserAccount


class UserStatistic:
    """Хранит сводную статистику активности пользователя в социальной сети."""

    def __init__(
        self,
        user_id: str,
        posts_published: int = 0,
        comments_written: int = 0,
        total_reactions_given: int = 0,
        active_days: int = 0,
        messages_sent: int = 0,
    ) -> None:
        """Инициализация персональной статистики."""
        self.user_id = user_id
        self.posts_published = posts_published
        self.comments_written = comments_written
        self.total_reactions_given = total_reactions_given
        self.active_days = active_days
        self.messages_sent = messages_sent

    def increment_posts(self, user: UserAccount) -> int:
        """Увеличивает счетчик опубликованных постов."""
        if user.user_id == self.user_id:
            self.posts_published += 1
        return self.posts_published

    def increment_comments(self) -> int:
        """Увеличивает счетчик оставленных комментариев."""
        self.comments_written += 1
        return self.comments_written

    def record_active_day(self) -> int:
        """Увеличивает счетчик дней посещения социальной сети."""
        self.active_days += 1
        return self.active_days
'''

FILES["analytics/trend_analyzer.py"] = '''# -*- coding: utf-8 -*-
"""Модуль анализа трендов и виральности."""

from lab3.network.content.hashtag import Hashtag


class TrendAnalyzer:
    """Выявляет быстрорастущие тренды и популярные обсуждения."""

    def __init__(
        self,
        window_hours: int = 24,
        top_limit: int = 10,
        velocity_multiplier: float = 1.25,
        min_occurrences: int = 50,
    ) -> None:
        """Инициализация анализатора трендов."""
        self.window_hours = window_hours
        self.top_limit = top_limit
        self.velocity_multiplier = velocity_multiplier
        self.min_occurrences = min_occurrences

    def identify_trending_topics(self, tags: list) -> list:
        """Фильтрует список тегов по критерию популярности."""
        trending = []
        for tag in tags:
            if isinstance(tag, Hashtag) and tag.usage_count >= self.min_occurrences:
                trending.append(tag.tag_name)
        return trending[:self.top_limit]

    def calculate_growth_velocity(self, count_now: int, count_before: int) -> float:
        """Рассчитывает скорость роста цитируемости инфоповода."""
        if count_before <= 0:
            return float(count_now)
        velocity = (count_now - count_before) / count_before
        return round(velocity * self.velocity_multiplier, 2)

    def adjust_window(self, hours: int) -> None:
        """Изменяет временное окно агрегации трендов."""
        self.window_hours = max(1, min(168, hours))
'''

# ---------------------------------------------------------------------------
# NOTIFICATION (lab3/network/notification/)
# ---------------------------------------------------------------------------

FILES["notification/notification.py"] = '''# -*- coding: utf-8 -*-
"""Модуль пользовательского уведомления."""

from lab3.network.core.user_account import UserAccount


class Notification:
    """Представляет системное уведомление о событиях (лайк, ответ, подписка)."""

    def __init__(
        self,
        notification_id: str,
        recipient_id: str,
        actor_id: str,
        event_type: str = "like",
        is_read: bool = False,
        created_at: str = "2026-01-01",
    ) -> None:
        """Инициализация уведомления."""
        self.notification_id = notification_id
        self.recipient_id = recipient_id
        self.actor_id = actor_id
        self.event_type = event_type
        self.is_read = is_read
        self.created_at = created_at

    def mark_as_read(self, recipient: UserAccount) -> bool:
        """Помечает уведомление как прочитанное адресатом."""
        if recipient.user_id == self.recipient_id:
            self.is_read = True
            return True
        return False

    def format_message(self) -> str:
        """Форматирует текст уведомления на основе типа события."""
        templates = {
            "like": f"Пользователь {self.actor_id} оценил вашу публикацию",
            "comment": f"Пользователь {self.actor_id} оставил комментарий",
            "friend_request": f"Пользователь {self.actor_id} отправил вам заявку в друзья",
            "mention": f"Пользователь {self.actor_id} упомянул вас",
        }
        return templates.get(self.event_type, f"Новое событие от {self.actor_id}")

    def is_urgent(self) -> bool:
        """Проверяет критичность уведомления для мгновенной доставки."""
        return self.event_type in ("security_alert", "password_reset", "ban_notice")
'''

FILES["notification/notification_channel.py"] = '''# -*- coding: utf-8 -*-
"""Модуль канала доставки уведомлений."""

from lab3.network.notification.notification import Notification


class NotificationChannel:
    """Описывает транспорт доставки сообщений (Push, Email, SMS, Web)."""

    def __init__(
        self,
        channel_name: str = "push",
        is_enabled: bool = True,
        delivery_timeout_sec: int = 5,
        retry_count: int = 3,
        priority: int = 1,
    ) -> None:
        """Инициализация канала уведомлений."""
        self.channel_name = channel_name
        self.is_enabled = is_enabled
        self.delivery_timeout_sec = delivery_timeout_sec
        self.retry_count = retry_count
        self.priority = priority

    def deliver(self, notification: Notification) -> bool:
        """Осуществляет отправку уведомления через выбранный канал."""
        if not self.is_enabled:
            return False
        return len(notification.recipient_id) > 0

    def toggle_channel(self) -> bool:
        """Включает или выключает данный транспорт доставки."""
        self.is_enabled = not self.is_enabled
        return self.is_enabled

    def adjust_timeout(self, seconds: int) -> None:
        """Настраивает таймаут ожидания ответа шлюза."""
        self.delivery_timeout_sec = max(1, seconds)
'''

FILES["notification/notification_batch.py"] = '''# -*- coding: utf-8 -*-
"""Модуль пакета сгруппированных уведомлений."""

from lab3.network.core.user_account import UserAccount
from lab3.network.notification.notification import Notification


class NotificationBatch:
    """Группирует однотипные уведомления для предотвращения спама."""

    def __init__(
        self,
        batch_id: str,
        recipient_id: str,
        count: int = 0,
        event_category: str = "likes",
        is_dispatched: bool = False,
    ) -> None:
        """Инициализация пакета уведомлений."""
        self.batch_id = batch_id
        self.recipient_id = recipient_id
        self.count = count
        self.event_category = event_category
        self.is_dispatched = is_dispatched

    def aggregate(self, notification: Notification) -> int:
        """Добавляет единичное уведомление в накопительный пакет."""
        if notification.recipient_id == self.recipient_id:
            self.count += 1
        return self.count

    def dispatch(self, recipient: UserAccount) -> str:
        """Формирует и отправляет сводное уведомление пользователю."""
        if recipient.user_id == self.recipient_id:
            self.is_dispatched = True
            return f"У вас {self.count} новых событий категории '{self.event_category}'"
        return "Ошибка адресата"

    def is_empty_batch(self) -> bool:
        """Проверяет, пуст ли текущий пакет уведомлений."""
        return self.count == 0
'''

# ---------------------------------------------------------------------------
# SECURITY (lab3/network/security/)
# ---------------------------------------------------------------------------

FILES["security/session_token.py"] = '''# -*- coding: utf-8 -*-
"""Модуль сессионного токена авторизации."""

from lab3.network.core.user_account import UserAccount
from lab3.network.exceptions.authentication_exception import AuthenticationException


class SessionToken:
    """Управляет жизненным циклом токена веб-сессии пользователя."""

    def __init__(
        self,
        token_value: str,
        user_id: str,
        ip_address: str,
        device_info: str = "Chrome/Win",
        expires_in_hours: int = 24,
        is_active: bool = True,
    ) -> None:
        """Инициализация сессионного токена."""
        self.token_value = token_value
        self.user_id = user_id
        self.ip_address = ip_address
        self.device_info = device_info
        self.expires_in_hours = expires_in_hours
        self.is_active = is_active

    def validate(self, current_user: UserAccount) -> bool:
        """Проверяет валидность токена и активность связанного аккаунта."""
        if not self.is_active or not current_user.is_active:
            raise AuthenticationException("Токен авторизации недействителен или отозван")
        return current_user.user_id == self.user_id

    def revoke(self) -> None:
        """Осуществляет отзыв (выход из аккаунта) текущей сессии."""
        self.is_active = False

    def renew(self, extension_hours: int) -> int:
        """Продлевает срок жизни активной сессии."""
        if self.is_active:
            self.expires_in_hours += max(1, extension_hours)
        return self.expires_in_hours
'''

FILES["security/two_factor_auth.py"] = '''# -*- coding: utf-8 -*-
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
'''

FILES["security/security_log.py"] = '''# -*- coding: utf-8 -*-
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
'''

# ---------------------------------------------------------------------------
# SYSTEM (lab3/network/system/)
# ---------------------------------------------------------------------------

FILES["system/data_backup.py"] = '''# -*- coding: utf-8 -*-
"""Модуль резервного копирования данных."""


class DataBackup:
    """Управляет созданием и проверкой целостности бэкапов социальной сети."""

    def __init__(
        self,
        backup_id: str,
        file_path: str,
        size_mb: float = 0.0,
        status: str = "created",
        is_encrypted: bool = True,
        checksum: str = "sha256_mock_sum",
    ) -> None:
        """Инициализация архива резервной копии."""
        self.backup_id = backup_id
        self.file_path = file_path
        self.size_mb = size_mb
        self.status = status
        self.is_encrypted = is_encrypted
        self.checksum = checksum

    def create_snapshot(self, data_size_mb: float) -> str:
        """Формирует снимок данных и фиксирует его размер."""
        self.size_mb = round(data_size_mb, 2)
        self.status = "completed"
        return self.status

    def verify_checksum(self, expected_hash: str) -> bool:
        """Сверяет контрольную сумму снапшота для подтверждения целостности."""
        return self.checksum == expected_hash

    def mark_corrupted(self) -> None:
        """Помечает резервную копию как поврежденную."""
        self.status = "corrupted"
'''

FILES["system/search_service.py"] = '''# -*- coding: utf-8 -*-
"""Модуль поисковой службы социальной сети."""

from lab3.network.content.hashtag import Hashtag
from lab3.network.content.post import Post
from lab3.network.core.user_account import UserAccount


class SearchService:
    """Обеспечивает полнотекстовый поиск по пользователям, публикациям и тегам."""

    def __init__(
        self,
        index_name: str = "global_search",
        indexed_items_count: int = 0,
        min_query_length: int = 3,
        fuzzy_matching: bool = True,
        max_results: int = 20,
    ) -> None:
        """Инициализация поискового индекса."""
        self.index_name = index_name
        self.indexed_items_count = indexed_items_count
        self.min_query_length = min_query_length
        self.fuzzy_matching = fuzzy_matching
        self.max_results = max_results

    def search_users(self, query: str, user_pool: list) -> list:
        """Выполняет поиск пользователей по логину."""
        if len(query) < self.min_query_length:
            return []
        q = query.lower()
        matches = [u for u in user_pool if isinstance(u, UserAccount) and q in u.username.lower()]
        return matches[:self.max_results]

    def search_posts(self, query: str, post_pool: list) -> list:
        """Выполняет поиск публикаций по ключевым словам."""
        if len(query) < self.min_query_length:
            return []
        q = query.lower()
        matches = [p for p in post_pool if isinstance(p, Post) and q in p.text_content.lower()]
        return matches[:self.max_results]

    def index_document(self, tag: Hashtag) -> int:
        """Индексирует хэштег для быстрого автодополнения."""
        self.indexed_items_count += 1
        return self.indexed_items_count
'''

FILES["system/social_network_system.py"] = '''# -*- coding: utf-8 -*-
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
'''

# ---------------------------------------------------------------------------
# ЗАПИСЬ ВСЕХ ФАЙЛОВ НА ДИСК
# ---------------------------------------------------------------------------

def write_all_files():
    base_dir = ROOT_DIR
    print(f"Запись файлов в {base_dir}...")
    
    subdirs = [
        "core", "content", "communication", "relations", "moderation",
        "monetization", "analytics", "notification", "security", "system", "exceptions"
    ]
    
    with open(os.path.join(base_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\\n\\\"\\\"\\\"Пакет социальной сети.\\\"\\\"\\\"\\n")
        
    for sub in subdirs:
        sub_path = os.path.join(base_dir, sub)
        os.makedirs(sub_path, exist_ok=True)
        init_path = os.path.join(sub_path, "__init__.py")
        with open(init_path, "w", encoding="utf-8") as f:
            f.write(f"# -*- coding: utf-8 -*-\\n\\\"\\\"\\\"Подсистема {sub}.\\\"\\\"\\\"\\n")

    for rel_path, code in FILES.items():
        full_path = os.path.join(base_dir, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Создан файл: {rel_path}")

    print(f"Всего сгенерировано файлов с классами: {len(FILES)}")

if __name__ == "__main__":
    write_all_files()
