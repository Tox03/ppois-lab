# Подробный справочник всех классов системы «Социальная сеть» (Лабораторная работа №3)

Документ содержит подробный разбор архитектуры и исходного кода **всех 79 классов** проекта.
Для каждого класса приведены:
1. **Файл** — относительный путь в репозитории и прямая ссылка.
2. **Что делает** — семантическая роль в домене социальной сети, ответственность.
3. **Как работает** — состав атрибутов (состояние), инициализация, внутренняя алгоритмическая логика каждого метода и возможные исключения.
4. **С какими классами связан** — наследование, композиция, агрегация, зависимости в сигнатурах методов и бизнес-исключения.

---

## Пользовательский консольный интерфейс (CLI) (`lab3/cli/`)

### Класс `NetworkCli`
- **Файл:** [`lab3/cli/network_cli.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/cli/network_cli.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Консольный интерфейс для управления и демонстрации возможностей социальной сети.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self._input_gen: Optional[Iterator[str]]` — внутренний атрибут объекта.
- `self.system: Any` — внутренний атрибут объекта.
- `self.users: Any` — внутренний атрибут объекта.
- `self.posts: Any` — внутренний атрибут объекта.
- `self.wallets: Any` — внутренний атрибут объекта.
- `self.banned_filter: Any` — внутренний атрибут объекта.
- `self.search: Any` — внутренний атрибут объекта.
- `self.active_chat: Any` — внутренний атрибут объекта.
- `self.group_chat: Any` — внутренний атрибут объекта.
- `self.active_friendship: Optional[Friendship]` — внутренний атрибут объекта.
- `self.active_block: Optional[BlockRecord]` — внутренний атрибут объекта.
- `self.active_poll: Optional[PollPost]` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self) -> None`
  - *Поведение:* Инициализация демонстрационного стенда социальной сети.
- **Методы бизнес-логики (поведение):**
  - `_setup_demo_data(self) -> None`
    - *Описание:* Наполняет систему демонстрационными аккаунтами и записями.
  - `print_menu(self) -> None`
    - *Описание:* Выводит главное меню возможностей социальной сети с парными операциями.
  - `show_system_report(self) -> None`
    - *Описание:* Демонстрирует системный отчет и переключает режим техработ.
  - `manage_users(self) -> None`
    - *Описание:* Демонстрирует просмотр пользователей, деактивацию и повторную активацию.
  - `manage_posts(self) -> None`
    - *Описание:* Демонстрирует создание, удаление и восстановление публикации.
  - `manage_polls(self) -> None`
    - *Описание:* Демонстрирует создание, закрытие и повторное открытие опроса.
  - `manage_chats(self) -> None`
    - *Описание:* Демонстрирует отправку сообщений, архивацию чата и управление звуком.
  - `manage_friendship(self) -> None`
    - *Описание:* Демонстрирует принятие заявки в друзья и расторжение дружбы.
  - `manage_blocking(self) -> None`
    - *Описание:* Демонстрирует блокировку и последующую разблокировку пользователя.
  - `manage_finances(self) -> None`
    - *Описание:* Демонстрирует пополнение, перевод, заморозку и разморозку кошелька.
  - `manage_moderation(self) -> None`
    - *Описание:* Демонстрирует добавление/удаление стоп-слов, а также наложение и отзыв санкций.
  - `show_analytics_and_search(self) -> None`
    - *Описание:* Демонстрирует расчет вовлеченности (ER) и полнотекстовый поиск.
  - `run(self) -> None`
    - *Описание:* Главный цикл консольного приложения.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `BannedWordFilter`, `BlockRecord`, `Chat`, `Comment`, `ContentFilter`, `DirectMessage`, `EngagementMetrics`, `FriendRequest`, `Friendship`, `GroupChat`, `ModerationReport`, `Moderator`, `PollOption`, `PollPost`, `Post`, `Reaction`, `Sanction`, `SearchService`, `SocialNetworkSystem`, `Transaction`, `UserAccount`, `VirtualGift`, `Wallet`.

---

## Ядро профилей и учетных записей (`lab3/network/core/`)

### Класс `ContactInfo`
- **Файл:** [`lab3/network/core/contact_info.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/core/contact_info.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Хранит контактную информацию и геолокационные данные профиля.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.phone: str` — внутренний атрибут объекта.
- `self.city: str` — внутренний атрибут объекта.
- `self.country: str` — внутренний атрибут объекта.
- `self.telegram_handle: str` — внутренний атрибут объекта.
- `self.is_phone_confirmed: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, phone: str, city: str, country: str, telegram_handle: str, is_phone_confirmed: bool) -> None`
  - *Поведение:* Инициализация контактных реквизитов пользователя.
- **Методы бизнес-логики (поведение):**
  - `confirm_phone(self, code: str) -> bool`
    - *Описание:* Подтверждает телефонный номер проверочным SMS-кодом.
  - `format_location(self) -> str`
    - *Описание:* Формирует текстовое представление местоположения пользователя.
  - `update_phone(self, new_phone: str) -> None`
    - *Описание:* Обновляет телефонный номер с предварительной валидацией.
    - *Возбуждаемые исключения:* `InvalidContentException`

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `InvalidContentException`.

---

### Класс `UserAccount`
- **Файл:** [`lab3/network/core/user_account.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/core/user_account.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Содержит учетные данные, логин, пароль и статус аккаунта.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.user_id: str` — внутренний атрибут объекта.
- `self.username: str` — внутренний атрибут объекта.
- `self.password_hash: str` — внутренний атрибут объекта.
- `self.email: str` — внутренний атрибут объекта.
- `self.is_active: bool` — внутренний атрибут объекта.
- `self.created_at: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, user_id: str, username: str, password_hash: str, email: str, is_active: bool, created_at: str) -> None`
  - *Поведение:* Инициализация учетной записи пользователя.
- **Методы бизнес-логики (поведение):**
  - `verify_password(self, raw_password: str) -> bool`
    - *Описание:* Проверяет совпадение введенного пароля с хэшем.
    - *Возбуждаемые исключения:* `AuthenticationException`
  - `change_password(self, old_pwd: str, new_pwd: str) -> None`
    - *Описание:* Сменяет пароль учетной записи с валидацией текущего.
    - *Возбуждаемые исключения:* `AuthenticationException`
  - `deactivate(self) -> None`
    - *Описание:* Деактивирует учетную запись пользователя.
  - `activate(self) -> None`
    - *Описание:* Восстанавливает активность учетной записи пользователя.
  - `bind_profile(self, profile: UserProfile) -> str`
    - *Описание:* Связывает профиль с учетной записью пользователя.
  - `bind_settings(self, settings: UserSettings) -> str`
    - *Описание:* Применяет персональные настройки к учетной записи.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `AuthenticationException`, `UserProfile`, `UserSettings`.

---

### Класс `UserActivity`
- **Файл:** [`lab3/network/core/user_activity.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/core/user_activity.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Отслеживает историю авторизаций, серию посещений и сетевой статус.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.last_login_at: str` — внутренний атрибут объекта.
- `self.login_streak_days: int` — внутренний атрибут объекта.
- `self.total_sessions: int` — внутренний атрибут объекта.
- `self.current_status: str` — внутренний атрибут объекта.
- `self.is_online: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, last_login_at: str, login_streak_days: int, total_sessions: int, current_status: str, is_online: bool) -> None`
  - *Поведение:* Инициализация метрик пользовательской активности.
- **Методы бизнес-логики (поведение):**
  - `record_login(self, account: UserAccount, timestamp: str) -> None`
    - *Описание:* Регистрирует новый вход в социальную сеть и обновляет серию дней.
  - `set_status(self, custom_status: str) -> None`
    - *Описание:* Устанавливает произвольный текстовый статус присутствия.
  - `go_offline(self) -> None`
    - *Описание:* Переводит пользователя в режим офлайн.
  - `go_online(self) -> None`
    - *Описание:* Переводит пользователя в режим онлайн.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

### Класс `UserPrivacy`
- **Файл:** [`lab3/network/core/user_privacy.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/core/user_privacy.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Определяет параметры видимости профиля и ограничения доступа.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.profile_visibility: str` — внутренний атрибут объекта.
- `self.allow_messages_from_strangers: bool` — внутренний атрибут объекта.
- `self.show_online_status: bool` — внутренний атрибут объекта.
- `self.blocked_users_count: int` — внутренний атрибут объекта.
- `self.searchable_by_phone: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, profile_visibility: str, allow_messages_from_strangers: bool, show_online_status: bool, blocked_users_count: int, searchable_by_phone: bool) -> None`
  - *Поведение:* Инициализация настроек приватности.
- **Методы бизнес-логики (поведение):**
  - `set_visibility(self, visibility_level: str) -> None`
    - *Описание:* Устанавливает уровень видимости страницы (public, friends_only, private).
    - *Возбуждаемые исключения:* `AccessDeniedException`
  - `can_receive_message_from(self, is_friend: bool) -> bool`
    - *Описание:* Проверяет, разрешено ли получение входящего сообщения.
  - `toggle_online_status(self) -> bool`
    - *Описание:* Переключает видимость сетевого статуса (онлайн).

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `AccessDeniedException`.

---

### Класс `UserProfile`
- **Файл:** [`lab3/network/core/user_profile.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/core/user_profile.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет публичный профиль участника социальной сети.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.bio: str` — внутренний атрибут объекта.
- `self.website: str` — внутренний атрибут объекта.
- `self.birth_date: str` — внутренний атрибут объекта.
- `self.avatar_url: str` — внутренний атрибут объекта.
- `self.is_verified: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, bio: str, website: str, birth_date: str, avatar_url: str, is_verified: bool) -> None`
  - *Поведение:* Инициализация профиля пользователя.
- **Методы бизнес-логики (поведение):**
  - `update_bio(self, text: str, privacy: UserPrivacy) -> None`
    - *Описание:* Обновляет текст биографии с проверкой прав доступа.
  - `verify_profile(self, document_confirmed: bool) -> bool`
    - *Описание:* Присваивает официальную галочку верификации профилю.
  - `format_profile_card(self, contact: ContactInfo) -> str`
    - *Описание:* Формирует текстовую визитку профиля с контактными данными.
  - `unverify_profile(self) -> None`
    - *Описание:* Снимает галочку верификации профиля.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `ContactInfo`, `UserPrivacy`.

---

### Класс `UserReputation`
- **Файл:** [`lab3/network/core/user_reputation.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/core/user_reputation.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Управляет очками кармы, уровнем доверия и предупреждениями.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.karma_points: int` — внутренний атрибут объекта.
- `self.warnings_count: int` — внутренний атрибут объекта.
- `self.trust_level: str` — внутренний атрибут объекта.
- `self.is_shadow_banned: bool` — внутренний атрибут объекта.
- `self.badge_title: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, karma_points: int, warnings_count: int, trust_level: str, is_shadow_banned: bool, badge_title: str) -> None`
  - *Поведение:* Инициализация репутации пользователя.
- **Методы бизнес-логики (поведение):**
  - `add_karma(self, amount: int, account: UserAccount) -> int`
    - *Описание:* Начисляет очки кармы за полезную активность.
  - `deduct_karma(self, amount: int) -> int`
    - *Описание:* Списывает очки кармы за нарушения.
  - `issue_warning(self) -> int`
    - *Описание:* Выносит предупреждение пользователю и может назначить теневой бан.
  - `calculate_trust_rank(self) -> str`
    - *Описание:* Пересчитывает категорию благонадежности пользователя.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

### Класс `UserSettings`
- **Файл:** [`lab3/network/core/user_settings.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/core/user_settings.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Хранит персональные интерфейсные предпочтения и каналы уведомлений.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.language: str` — внутренний атрибут объекта.
- `self.theme: str` — внутренний атрибут объекта.
- `self.email_notifications: bool` — внутренний атрибут объекта.
- `self.push_notifications: bool` — внутренний атрибут объекта.
- `self.sound_enabled: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, language: str, theme: str, email_notifications: bool, push_notifications: bool, sound_enabled: bool) -> None`
  - *Поведение:* Инициализация настроек интерфейса пользователя.
- **Методы бизнес-логики (поведение):**
  - `switch_theme(self, new_theme: str) -> str`
    - *Описание:* Переключает цветовую схему оформления интерфейса.
  - `toggle_push(self) -> bool`
    - *Описание:* Инвертирует разрешение отправки push-уведомлений.
  - `change_language(self, lang_code: str) -> None`
    - *Описание:* Изменяет локаль пользовательского интерфейса.

#### Связи с другими классами:
- **Ассоциации:** Автономный класс.

---

## Публикации, медиаконтент, истории и опросы (`lab3/network/content/`)

### Класс `Album`
- **Файл:** [`lab3/network/content/album.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/content/album.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Коллекция сохраненных фотографий и медиафайлов.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.album_id: str` — внутренний атрибут объекта.
- `self.owner_id: str` — внутренний атрибут объекта.
- `self.title: str` — внутренний атрибут объекта.
- `self.description: str` — внутренний атрибут объекта.
- `self.photos_count: int` — внутренний атрибут объекта.
- `self.is_private: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, album_id: str, owner_id: str, title: str, description: str, photos_count: int, is_private: bool) -> None`
  - *Поведение:* Инициализация фотоальбома.
- **Методы бизнес-логики (поведение):**
  - `add_photo(self, photo: MediaAttachment, owner: UserAccount) -> int`
    - *Описание:* Добавляет фотоснимок в альбом с проверкой владельца.
  - `remove_photo(self) -> int`
    - *Описание:* Уменьшает счетчик снимков в альбоме.
  - `toggle_privacy(self) -> bool`
    - *Описание:* Переключает видимость альбома (публичный/скрытый).

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `MediaAttachment`, `UserAccount`.

---

### Класс `Comment`
- **Файл:** [`lab3/network/content/comment.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/content/comment.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет комментарий пользователя под записью.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.comment_id: str` — внутренний атрибут объекта.
- `self.post_id: str` — внутренний атрибут объекта.
- `self.author_id: str` — внутренний атрибут объекта.
- `self.text: str` — внутренний атрибут объекта.
- `self.likes_count: int` — внутренний атрибут объекта.
- `self.is_hidden: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, comment_id: str, post_id: str, author_id: str, text: str, likes_count: int, is_hidden: bool) -> None`
  - *Поведение:* Инициализация комментария.
- **Методы бизнес-логики (поведение):**
  - `like(self, reaction: Reaction) -> int`
    - *Описание:* Регистрирует положительную реакцию на комментарий.
  - `hide(self) -> None`
    - *Описание:* Скрывает комментарий модератором.
  - `edit_text(self, new_text: str, author: UserAccount) -> None`
    - *Описание:* Редактирует текст комментария автором.
  - `belongs_to_post(self, post: Post) -> bool`
    - *Описание:* Проверяет принадлежность комментария к конкретной записи.
  - `unhide(self) -> None`
    - *Описание:* Делает скрытый комментарий снова видимым.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `Post`, `Reaction`, `UserAccount`.

---

### Класс `Hashtag`
- **Файл:** [`lab3/network/content/hashtag.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/content/hashtag.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Хранит информацию о поисковом хэштеге и частоте его использования.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.tag_name: str` — внутренний атрибут объекта.
- `self.usage_count: int` — внутренний атрибут объекта.
- `self.trending_score: float` — внутренний атрибут объекта.
- `self.is_blacklisted: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, tag_name: str, usage_count: int, trending_score: float, is_blacklisted: bool) -> None`
  - *Поведение:* Инициализация хэштега.
- **Методы бизнес-логики (поведение):**
  - `increment_usage(self) -> int`
    - *Описание:* Увеличивает счетчик цитируемости хэштега.
    - *Возбуждаемые исключения:* `InvalidContentException`
  - `update_trend_score(self, new_posts_last_hour: int) -> float`
    - *Описание:* Пересчитывает показатель трендовости на основе динамики публикаций.
  - `validate_tag(self) -> bool`
    - *Описание:* Проверяет допустимость символов в названии тега.
    - *Возбуждаемые исключения:* `InvalidContentException`

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `InvalidContentException`.

---

### Класс `MediaAttachment`
- **Файл:** [`lab3/network/content/media_attachment.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/content/media_attachment.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Описывает прикрепленный медиафайл (фотография, видеоролик, документ).

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.attachment_id: str` — внутренний атрибут объекта.
- `self.file_url: str` — внутренний атрибут объекта.
- `self.file_size_bytes: int` — внутренний атрибут объекта.
- `self.mime_type: str` — внутренний атрибут объекта.
- `self.width: int` — внутренний атрибут объекта.
- `self.height: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, attachment_id: str, file_url: str, file_size_bytes: int, mime_type: str, width: int, height: int) -> None`
  - *Поведение:* Инициализация медиавложения.
- **Методы бизнес-логики (поведение):**
  - `is_image(self) -> bool`
    - *Описание:* Проверяет, является ли вложение изображением.
  - `is_video(self) -> bool`
    - *Описание:* Проверяет, является ли вложение видеозаписью.
  - `format_file_size(self) -> str`
    - *Описание:* Форматирует размер файла в удобочитаемый вид (КБ / МБ).
  - `validate_url(self) -> bool`
    - *Описание:* Проверяет корректность веб-ссылки на медиафайл.
    - *Возбуждаемые исключения:* `InvalidContentException`

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `InvalidContentException`.

---

### Класс `MediaPost`
- **Файл:** [`lab3/network/content/media_post.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/content/media_post.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Публикация, содержащая фотографии или видеогалерею.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.post_id: str` — внутренний атрибут объекта.
- `self.aspect_ratio: str` — внутренний атрибут объекта.
- `self.has_watermark: bool` — внутренний атрибут объекта.
- `self.media_count: int` — внутренний атрибут объекта.
- `self.alt_description: str` — внутренний атрибут объекта.
- `self.filter_preset: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, post_id: str, aspect_ratio: str, has_watermark: bool, media_count: int, alt_description: str, filter_preset: str) -> None`
  - *Поведение:* Инициализация медиа-поста.
- **Методы бизнес-логики (поведение):**
  - `add_media_item(self, media: MediaAttachment) -> int`
    - *Описание:* Добавляет медиа-элемент в публикацию и обновляет счетчик.
  - `apply_filter(self, preset_name: str) -> str`
    - *Описание:* Применяет цветовой фильтр ко всем прикрепленным изображениям.
  - `verify_attachments(self, base_post: Post) -> bool`
    - *Описание:* Проверяет корректность привязки медиа к базовой публикации.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `MediaAttachment`, `Post`.

---

### Класс `PollOption`
- **Файл:** [`lab3/network/content/poll_option.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/content/poll_option.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет отдельный вариант ответа в голосовании.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.option_id: str` — внутренний атрибут объекта.
- `self.option_text: str` — внутренний атрибут объекта.
- `self.votes_count: int` — внутренний атрибут объекта.
- `self.percentage: float` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, option_id: str, option_text: str, votes_count: int, percentage: float) -> None`
  - *Поведение:* Инициализация пункта опроса.
- **Методы бизнес-логики (поведение):**
  - `increment_vote(self) -> int`
    - *Описание:* Увеличивает счетчик голосов за данный пункт.
  - `update_percentage(self, total_votes: int) -> float`
    - *Описание:* Вычисляет долю голосов в процентах от общего числа участников.
  - `format_label(self) -> str`
    - *Описание:* Формирует текстовую подпись варианта с числом голосов.

#### Связи с другими классами:
- **Ассоциации:** Автономный класс.

---

### Класс `PollPost`
- **Файл:** [`lab3/network/content/poll_post.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/content/poll_post.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Публикация с голосованием и вариантами ответов.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.post_id: str` — внутренний атрибут объекта.
- `self.question: str` — внутренний атрибут объекта.
- `self.is_anonymous: bool` — внутренний атрибут объекта.
- `self.is_closed: bool` — внутренний атрибут объекта.
- `self.max_choices: int` — внутренний атрибут объекта.
- `self.total_votes: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, post_id: str, question: str, is_anonymous: bool, is_closed: bool, max_choices: int, total_votes: int) -> None`
  - *Поведение:* Инициализация опроса.
- **Методы бизнес-логики (поведение):**
  - `close_poll(self) -> None`
    - *Описание:* Завершает прием голосов в опросе.
  - `add_vote(self, option: PollOption) -> int`
    - *Описание:* Учитывает голос пользователя за выбранный вариант.
    - *Возбуждаемые исключения:* `InvalidContentException`
  - `calculate_results(self, options: list) -> None`
    - *Описание:* Пересчитывает проценты для всех вариантов ответа.
  - `can_vote(self, post: Post) -> bool`
    - *Описание:* Проверяет доступность опроса для голосования.
  - `reopen_poll(self) -> None`
    - *Описание:* Возобновляет прием голосов в опросе.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `InvalidContentException`, `PollOption`, `Post`.

---

### Класс `Post`
- **Файл:** [`lab3/network/content/post.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/content/post.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет запись на стене пользователя или в ленте социальной сети.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.post_id: str` — внутренний атрибут объекта.
- `self.author_id: str` — внутренний атрибут объекта.
- `self.text_content: str` — внутренний атрибут объекта.
- `self.created_at: str` — внутренний атрибут объекта.
- `self.is_pinned: bool` — внутренний атрибут объекта.
- `self.is_deleted: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, post_id: str, author_id: str, text_content: str, created_at: str, is_pinned: bool, is_deleted: bool) -> None`
  - *Поведение:* Инициализация публикации.
- **Методы бизнес-логики (поведение):**
  - `pin(self, author: UserAccount) -> bool`
    - *Описание:* Закрепляет публикацию вверху ленты профиля.
  - `unpin(self) -> None`
    - *Описание:* Открепляет публикацию.
  - `soft_delete(self) -> None`
    - *Описание:* Помечает публикацию удаленной.
  - `edit_content(self, new_text: str, author: UserAccount) -> None`
    - *Описание:* Редактирует текст записи с проверкой авторства.
    - *Возбуждаемые исключения:* `ContentBlockedException`, `InvalidContentException`
  - `restore(self) -> None`
    - *Описание:* Восстанавливает ранее удаленную публикацию.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `ContentBlockedException`, `InvalidContentException`, `UserAccount`.

---

### Класс `Reaction`
- **Файл:** [`lab3/network/content/reaction.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/content/reaction.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет эмоциональную реакцию пользователя на пост или комментарий.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.reaction_type: str` — внутренний атрибут объекта.
- `self.user_id: str` — внутренний атрибут объекта.
- `self.target_id: str` — внутренний атрибут объекта.
- `self.created_at: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, reaction_type: str, user_id: str, target_id: str, created_at: str) -> None`
  - *Поведение:* Инициализация реакции пользователя.
- **Методы бизнес-логики (поведение):**
  - `update_type(self, new_type: str, user: UserAccount) -> None`
    - *Описание:* Изменяет тип реакции (like, love, haha, wow, sad, angry).
  - `is_positive(self) -> bool`
    - *Описание:* Определяет, выражает ли реакция положительные эмоции.
  - `get_emoji(self) -> str`
    - *Описание:* Возвращает соответствующий текстовый эмодзи.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

### Класс `Story`
- **Файл:** [`lab3/network/content/story.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/content/story.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет короткую историю с ограниченным сроком жизни (24 часа).

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.story_id: str` — внутренний атрибут объекта.
- `self.author_id: str` — внутренний атрибут объекта.
- `self.media_url: str` — внутренний атрибут объекта.
- `self.duration_seconds: int` — внутренний атрибут объекта.
- `self.views_count: int` — внутренний атрибут объекта.
- `self.is_expired: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, story_id: str, author_id: str, media_url: str, duration_seconds: int, views_count: int, is_expired: bool) -> None`
  - *Поведение:* Инициализация истории.
- **Методы бизнес-логики (поведение):**
  - `record_view(self, viewer: UserAccount) -> int`
    - *Описание:* Фиксирует просмотр истории другим пользователем.
  - `check_expiration(self, hours_passed: int) -> bool`
    - *Описание:* Проверяет истечение срока действия истории по прошедшим часам.
  - `archive(self) -> None`
    - *Описание:* Принудительно переводит историю в архив.
  - `add_interactive_sticker(self, sticker_name: str) -> str`
    - *Описание:* Прикрепляет интерактивный стикер к истории.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

### Класс `StoryViewer`
- **Файл:** [`lab3/network/content/story_viewer.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/content/story_viewer.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Фиксирует факт просмотра конкретной истории пользователем.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.viewer_id: str` — внутренний атрибут объекта.
- `self.story_id: str` — внутренний атрибут объекта.
- `self.viewed_at: str` — внутренний атрибут объекта.
- `self.has_reacted: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, viewer_id: str, story_id: str, viewed_at: str, has_reacted: bool) -> None`
  - *Поведение:* Инициализация записи о просмотре истории.
- **Методы бизнес-логики (поведение):**
  - `mark_reaction(self, user: UserAccount) -> bool`
    - *Описание:* Отмечает отправку реакции на историю зрителем.
  - `get_watch_delay(self) -> str`
    - *Описание:* Возвращает информацию о времени просмотра.
  - `format_viewer_info(self) -> str`
    - *Описание:* Форматирует краткую сводку о зрителе.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

### Класс `TextPost`
- **Файл:** [`lab3/network/content/text_post.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/content/text_post.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Специализированная текстовая запись с расширенным оформлением.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.post_id: str` — внутренний атрибут объекта.
- `self.font_style: str` — внутренний атрибут объекта.
- `self.background_color: str` — внутренний атрибут объекта.
- `self.reading_time_minutes: int` — внутренний атрибут объекта.
- `self.word_count: int` — внутренний атрибут объекта.
- `self.summary: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, post_id: str, font_style: str, background_color: str, reading_time_minutes: int, word_count: int, summary: str) -> None`
  - *Поведение:* Инициализация статьи.
- **Методы бизнес-логики (поведение):**
  - `calculate_reading_time(self, post: Post) -> int`
    - *Описание:* Рассчитывает ориентировочное время чтения статьи.
  - `generate_summary(self, post: Post) -> str`
    - *Описание:* Генерирует краткую аннотацию из первого предложения записи.
  - `apply_styling(self, font: str, bg: str) -> None`
    - *Описание:* Настраивает визуальные параметры шрифта и подложки статьи.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `Post`.

---

## Обмен сообщениями, чаты и звонки (`lab3/network/communication/`)

### Класс `AudioMessage`
- **Файл:** [`lab3/network/communication/audio_message.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/communication/audio_message.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет голосовое сообщение с расшифровкой речи в текст.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.audio_id: str` — внутренний атрибут объекта.
- `self.duration_seconds: int` — внутренний атрибут объекта.
- `self.audio_url: str` — внутренний атрибут объекта.
- `self.transcription: str` — внутренний атрибут объекта.
- `self.waveform_samples: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, audio_id: str, duration_seconds: int, audio_url: str, transcription: str, waveform_samples: int) -> None`
  - *Поведение:* Инициализация аудиосообщения.
- **Методы бизнес-логики (поведение):**
  - `transcribe(self, text: str) -> str`
    - *Описание:* Записывает распознанный текст голосового сообщения.
    - *Возбуждаемые исключения:* `InvalidContentException`
  - `is_long_audio(self) -> bool`
    - *Описание:* Определяет, превышает ли аудиозапись 2 минуты.
  - `format_duration(self) -> str`
    - *Описание:* Форматирует длительность трека в вид ММ:СС.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `InvalidContentException`.

---

### Класс `CallSession`
- **Файл:** [`lab3/network/communication/call_session.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/communication/call_session.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет сеанс аудио- или видеозвонка между пользователями.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.call_id: str` — внутренний атрибут объекта.
- `self.initiator_id: str` — внутренний атрибут объекта.
- `self.is_video: bool` — внутренний атрибут объекта.
- `self.duration_seconds: int` — внутренний атрибут объекта.
- `self.status: str` — внутренний атрибут объекта.
- `self.quality_score: float` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, call_id: str, initiator_id: str, is_video: bool, duration_seconds: int, status: str, quality_score: float) -> None`
  - *Поведение:* Инициализация сеанса звонка.
- **Методы бизнес-логики (поведение):**
  - `start_call(self, participant: UserAccount) -> bool`
    - *Описание:* Начинает голосовой вызов при подтверждении собеседника.
  - `end_call(self, total_seconds: int) -> int`
    - *Описание:* Завершает звонок и фиксирует продолжительность разговора.
  - `rate_quality(self, score: float) -> float`
    - *Описание:* Сохраняет субъективную оценку качества связи пользователем.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

### Класс `Chat`
- **Файл:** [`lab3/network/communication/chat.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/communication/chat.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет диалог в системе сообщений.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.chat_id: str` — внутренний атрибут объекта.
- `self.created_at: str` — внутренний атрибут объекта.
- `self.last_message_at: str` — внутренний атрибут объекта.
- `self.messages_count: int` — внутренний атрибут объекта.
- `self.is_archived: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, chat_id: str, created_at: str, last_message_at: str, messages_count: int, is_archived: bool) -> None`
  - *Поведение:* Инициализация диалога.
- **Методы бизнес-логики (поведение):**
  - `archive(self) -> None`
    - *Описание:* Переносит диалог в архив.
  - `unarchive(self) -> None`
    - *Описание:* Извлекает диалог из архива.
  - `update_last_activity(self, timestamp: str) -> None`
    - *Описание:* Обновляет время последней активности и инкрементирует число сообщений.

#### Связи с другими классами:
- **Ассоциации:** Автономный класс.

---

### Класс `ChatMember`
- **Файл:** [`lab3/network/communication/chat_member.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/communication/chat_member.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Определяет роль и статус участника группового чата.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.member_id: str` — внутренний атрибут объекта.
- `self.chat_id: str` — внутренний атрибут объекта.
- `self.role: str` — внутренний атрибут объекта.
- `self.joined_at: str` — внутренний атрибут объекта.
- `self.is_banned: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, member_id: str, chat_id: str, role: str, joined_at: str, is_banned: bool) -> None`
  - *Поведение:* Инициализация участника беседы.
- **Методы бизнес-логики (поведение):**
  - `promote_to_admin(self, admin_account: UserAccount) -> bool`
    - *Описание:* Повышает участника до администратора чата.
  - `demote(self) -> None`
    - *Описание:* Понижает статус участника до обычного.
  - `ban(self) -> None`
    - *Описание:* Блокирует участника в данном чате.
  - `unban(self) -> None`
    - *Описание:* Снимает блокировку с участника чата.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

### Класс `ChatMessage`
- **Файл:** [`lab3/network/communication/chat_message.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/communication/chat_message.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Сообщение, отправленное внутри группового или парного чата.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.message_id: str` — внутренний атрибут объекта.
- `self.chat_id: str` — внутренний атрибут объекта.
- `self.sender_id: str` — внутренний атрибут объекта.
- `self.text: str` — внутренний атрибут объекта.
- `self.reply_to_id: str` — внутренний атрибут объекта.
- `self.is_pinned: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, message_id: str, chat_id: str, sender_id: str, text: str, reply_to_id: str, is_pinned: bool) -> None`
  - *Поведение:* Инициализация сообщения чата.
- **Методы бизнес-логики (поведение):**
  - `pin(self, chat: Chat) -> bool`
    - *Описание:* Закрепляет данное сообщение в шапке чата.
  - `unpin(self) -> None`
    - *Описание:* Снимает закрепление с сообщения.
  - `set_reply(self, target_message_id: str, sender: UserAccount) -> None`
    - *Описание:* Устанавливает ссылку на цитируемое сообщение при ответе.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `Chat`, `UserAccount`.

---

### Класс `DirectMessage`
- **Файл:** [`lab3/network/communication/direct_message.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/communication/direct_message.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет приватное сообщение диалога двух участников.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.message_id: str` — внутренний атрибут объекта.
- `self.sender_id: str` — внутренний атрибут объекта.
- `self.recipient_id: str` — внутренний атрибут объекта.
- `self.content: str` — внутренний атрибут объекта.
- `self.is_read: bool` — внутренний атрибут объекта.
- `self.is_delivered: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, message_id: str, sender_id: str, recipient_id: str, content: str, is_read: bool, is_delivered: bool) -> None`
  - *Поведение:* Инициализация личного сообщения.
- **Методы бизнес-логики (поведение):**
  - `mark_as_read(self, recipient: UserAccount) -> bool`
    - *Описание:* Помечает сообщение прочитанным адресатом.
    - *Возбуждаемые исключения:* `AccessDeniedException`
  - `mark_as_delivered(self) -> None`
    - *Описание:* Устанавливает статус доставки сообщения на устройство.
  - `format_preview(self) -> str`
    - *Описание:* Возвращает краткий предпросмотр сообщения для списка чатов.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `AccessDeniedException`, `UserAccount`.

---

### Класс `GroupChat`
- **Файл:** [`lab3/network/communication/group_chat.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/communication/group_chat.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Управляет групповой многопользовательской беседой.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.chat_id: str` — внутренний атрибут объекта.
- `self.title: str` — внутренний атрибут объекта.
- `self.admin_id: str` — внутренний атрибут объекта.
- `self.members_limit: int` — внутренний атрибут объекта.
- `self.invite_code: str` — внутренний атрибут объекта.
- `self.is_muted: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, chat_id: str, title: str, admin_id: str, members_limit: int, invite_code: str, is_muted: bool) -> None`
  - *Поведение:* Инициализация групповой беседы.
- **Методы бизнес-логики (поведение):**
  - `add_participant(self, member: ChatMember, current_count: int) -> bool`
    - *Описание:* Добавляет нового участника в групповой чат с проверкой лимита.
    - *Возбуждаемые исключения:* `GroupCapacityExceededException`
  - `remove_participant(self, member: ChatMember) -> None`
    - *Описание:* Исключает участника из беседы.
  - `generate_invite(self, base_chat: Chat) -> str`
    - *Описание:* Генерирует новую ссылку-приглашение в групповой диалог.
  - `mute(self) -> None`
    - *Описание:* Отключает звуковые уведомления о сообщениях группы.
  - `unmute(self) -> None`
    - *Описание:* Включает звуковые уведомления о сообщениях группы.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `Chat`, `ChatMember`, `GroupCapacityExceededException`.

---

## Социальный граф, дружба, подписки и сообщества (`lab3/network/relations/`)

### Класс `BlockRecord`
- **Файл:** [`lab3/network/relations/block_record.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/relations/block_record.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет запись о блокировке нежелательного пользователя.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.blocker_id: str` — внутренний атрибут объекта.
- `self.blocked_id: str` — внутренний атрибут объекта.
- `self.reason: str` — внутренний атрибут объекта.
- `self.created_at: str` — внутренний атрибут объекта.
- `self.is_active: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, blocker_id: str, blocked_id: str, reason: str, created_at: str, is_active: bool) -> None`
  - *Поведение:* Инициализация записи о блокировке.
- **Методы бизнес-логики (поведение):**
  - `deactivate(self, blocker: UserAccount) -> None`
    - *Описание:* Снимает блокировку инициатором.
  - `matches_pair(self, u1: str, u2: str) -> bool`
    - *Описание:* Проверяет, соответствует ли пара пользователей данной блокировке.
  - `format_block_notice(self) -> str`
    - *Описание:* Формирует уведомление о причине внесения в черный список.
  - `activate(self, blocker: UserAccount) -> None`
    - *Описание:* Повторно активирует блокировку инициатором.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

### Класс `Follow`
- **Файл:** [`lab3/network/relations/follow.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/relations/follow.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет одностороннюю подписку на обновления автора.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.follower_id: str` — внутренний атрибут объекта.
- `self.target_id: str` — внутренний атрибут объекта.
- `self.started_at: str` — внутренний атрибут объекта.
- `self.notifications_enabled: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, follower_id: str, target_id: str, started_at: str, notifications_enabled: bool) -> None`
  - *Поведение:* Инициализация подписки.
- **Методы бизнес-логики (поведение):**
  - `toggle_notifications(self) -> bool`
    - *Описание:* Включает или выключает уведомления о новых публикациях автора.
  - `get_follow_duration_days(self) -> int`
    - *Описание:* Возвращает примерную длительность подписки в днях.
  - `unfollow(self, follower: UserAccount) -> bool`
    - *Описание:* Отменяет подписку на автора.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

### Класс `FriendRequest`
- **Файл:** [`lab3/network/relations/friend_request.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/relations/friend_request.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет входящую заявку на дружбу с сопроводительным сообщением.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.request_id: str` — внутренний атрибут объекта.
- `self.sender_id: str` — внутренний атрибут объекта.
- `self.receiver_id: str` — внутренний атрибут объекта.
- `self.message: str` — внутренний атрибут объекта.
- `self.status: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, request_id: str, sender_id: str, receiver_id: str, message: str, status: str) -> None`
  - *Поведение:* Инициализация заявки в друзья.
- **Методы бизнес-логики (поведение):**
  - `accept(self, receiver: UserAccount) -> Friendship`
    - *Описание:* Принимает заявку и формирует взаимную дружбу.
  - `reject(self, receiver: UserAccount) -> None`
    - *Описание:* Отклоняет входящую заявку в друзья.
  - `is_pending(self) -> bool`
    - *Описание:* Проверяет, ожидает ли заявка ответа адресата.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `Friendship`, `UserAccount`.

---

### Класс `Friendship`
- **Файл:** [`lab3/network/relations/friendship.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/relations/friendship.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет установленную дружбу между двумя пользователями.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.user_a_id: str` — внутренний атрибут объекта.
- `self.user_b_id: str` — внутренний атрибут объекта.
- `self.status: str` — внутренний атрибут объекта.
- `self.established_at: str` — внутренний атрибут объекта.
- `self.closeness_level: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, user_a_id: str, user_b_id: str, status: str, established_at: str, closeness_level: int) -> None`
  - *Поведение:* Инициализация связи дружбы.
- **Методы бизнес-логики (поведение):**
  - `increase_closeness(self) -> int`
    - *Описание:* Повышает уровень близости взаимодействия друзей.
  - `terminate(self, initiator: UserAccount) -> None`
    - *Описание:* Расторгает дружбу одним из участников.
  - `is_confirmed(self) -> bool`
    - *Описание:* Проверяет активность дружбы.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

### Класс `GroupEvent`
- **Файл:** [`lab3/network/relations/group_event.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/relations/group_event.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет встречу или онлайн-вебинар, организованный сообществом.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.event_id: str` — внутренний атрибут объекта.
- `self.group_id: str` — внутренний атрибут объекта.
- `self.title: str` — внутренний атрибут объекта.
- `self.event_date: str` — внутренний атрибут объекта.
- `self.max_attendees: int` — внутренний атрибут объекта.
- `self.attendees_count: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, event_id: str, group_id: str, title: str, event_date: str, max_attendees: int, attendees_count: int) -> None`
  - *Поведение:* Инициализация мероприятия сообщества.
- **Методы бизнес-логики (поведение):**
  - `register_attendee(self, user: UserAccount) -> int`
    - *Описание:* Регистрирует участника на мероприятие.
    - *Возбуждаемые исключения:* `GroupCapacityExceededException`
  - `cancel_attendance(self) -> int`
    - *Описание:* Отменяет регистрацию участника и освобождает место.
  - `is_full(self) -> bool`
    - *Описание:* Проверяет, исчерпан ли лимит свободных мест на событии.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `GroupCapacityExceededException`, `UserAccount`.

---

### Класс `GroupMembership`
- **Файл:** [`lab3/network/relations/group_membership.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/relations/group_membership.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Определяет участие пользователя в тематическом сообществе.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.membership_id: str` — внутренний атрибут объекта.
- `self.group_id: str` — внутренний атрибут объекта.
- `self.user_id: str` — внутренний атрибут объекта.
- `self.role: str` — внутренний атрибут объекта.
- `self.warning_count: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, membership_id: str, group_id: str, user_id: str, role: str, warning_count: int) -> None`
  - *Поведение:* Инициализация членства в группе.
- **Методы бизнес-логики (поведение):**
  - `warn_member(self) -> int`
    - *Описание:* Выносит предупреждение участнику за нарушение регламента группы.
  - `change_role(self, new_role: str, admin: UserAccount) -> None`
    - *Описание:* Изменяет статус участника администратором группы.
    - *Возбуждаемые исключения:* `InsufficientPrivilegesException`
  - `is_moderator(self) -> bool`
    - *Описание:* Проверяет наличие прав модератора в группе.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `InsufficientPrivilegesException`, `UserAccount`.

---

### Класс `UserGroup`
- **Файл:** [`lab3/network/relations/user_group.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/relations/user_group.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет публичное или закрытое сообщество по интересам.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.group_id: str` — внутренний атрибут объекта.
- `self.name: str` — внутренний атрибут объекта.
- `self.description: str` — внутренний атрибут объекта.
- `self.owner_id: str` — внутренний атрибут объекта.
- `self.is_verified: bool` — внутренний атрибут объекта.
- `self.is_closed: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, group_id: str, name: str, description: str, owner_id: str, is_verified: bool, is_closed: bool) -> None`
  - *Поведение:* Инициализация сообщества.
- **Методы бизнес-логики (поведение):**
  - `verify_group(self) -> None`
    - *Описание:* Присваивает официальную отметку верификации сообществу.
  - `close_group(self, owner: UserAccount) -> bool`
    - *Описание:* Переводит группу в закрытый режим по решению владельца.
  - `open_group(self) -> None`
    - *Описание:* Делает группу открытой для свободного вступления.
  - `update_info(self, new_name: str, new_desc: str) -> None`
    - *Описание:* Обновляет заголовок и описание страницы группы.
  - `has_member(self, membership: GroupMembership) -> bool`
    - *Описание:* Проверяет принадлежность членства к данной группе.
  - `unverify_group(self) -> None`
    - *Описание:* Снимает отметку официальной верификации сообщества.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `GroupMembership`, `UserAccount`.

---

## Служба модерации, цензура, жалобы и санкции (`lab3/network/moderation/`)

### Класс `Appeal`
- **Файл:** [`lab3/network/moderation/appeal.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/moderation/appeal.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет заявление на обжалование блокировки или предупреждения.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.appeal_id: str` — внутренний атрибут объекта.
- `self.sanction_id: str` — внутренний атрибут объекта.
- `self.user_id: str` — внутренний атрибут объекта.
- `self.explanation: str` — внутренний атрибут объекта.
- `self.status: str` — внутренний атрибут объекта.
- `self.reviewer_notes: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, appeal_id: str, sanction_id: str, user_id: str, explanation: str, status: str, reviewer_notes: str) -> None`
  - *Поведение:* Инициализация апелляционного обращения.
- **Методы бизнес-логики (поведение):**
  - `approve(self, sanction: Sanction, notes: str) -> None`
    - *Описание:* Удовлетворяет апелляцию и отменяет санкцию.
  - `reject(self, notes: str) -> None`
    - *Описание:* Отклоняет прошение о снятии ограничения.
  - `is_under_review(self) -> bool`
    - *Описание:* Проверяет, находится ли обращение на стадии рассмотрения.
  - `submitted_by(self, user: UserAccount) -> bool`
    - *Описание:* Проверяет авторство апелляционного заявления.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `Sanction`, `UserAccount`.

---

### Класс `AuditLog`
- **Файл:** [`lab3/network/moderation/audit_log.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/moderation/audit_log.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Фиксирует административные и критические действия в системе.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.log_id: str` — внутренний атрибут объекта.
- `self.action: str` — внутренний атрибут объекта.
- `self.actor_id: str` — внутренний атрибут объекта.
- `self.target_id: str` — внутренний атрибут объекта.
- `self.timestamp: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, log_id: str, action: str, actor_id: str, target_id: str, timestamp: str) -> None`
  - *Поведение:* Инициализация записи журнала аудита.
- **Методы бизнес-логики (поведение):**
  - `format_log_entry(self) -> str`
    - *Описание:* Форматирует строковое представление события аудита.
  - `is_action_critical(self) -> bool`
    - *Описание:* Определяет, относится ли операция к потенциально деструктивным.
  - `matches_actor(self, user: UserAccount) -> bool`
    - *Описание:* Проверяет совпадение исполнителя действия с аккаунтом.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

### Класс `BannedWordFilter`
- **Файл:** [`lab3/network/moderation/banned_word_filter.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/moderation/banned_word_filter.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Осуществляет лексический анализ и цензурирование текста.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.banned_words_count: int` — внутренний атрибут объекта.
- `self.case_sensitive: bool` — внутренний атрибут объекта.
- `self.replacement_symbol: str` — внутренний атрибут объекта.
- `self.strict_mode: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, banned_words_count: int, case_sensitive: bool, replacement_symbol: str, strict_mode: bool) -> None`
  - *Поведение:* Инициализация фильтра стоп-слов.
- **Методы бизнес-логики (поведение):**
  - `contains_banned_word(self, text: str, word_list: list) -> bool`
    - *Описание:* Проверяет присутствие недопустимых слов в сообщении.
  - `censor_text(self, text: str, word_list: list) -> str`
    - *Описание:* Заменяет запрещенные фрагменты маскирующими символами.
  - `add_keyword(self, word: str) -> int`
    - *Описание:* Добавляет новый термин в глобальный стоп-словарь.
    - *Возбуждаемые исключения:* `InvalidContentException`
  - `remove_keyword(self, word: str) -> int`
    - *Описание:* Удаляет термин из стоп-словаря.
    - *Возбуждаемые исключения:* `InvalidContentException`

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `InvalidContentException`.

---

### Класс `ContentFilter`
- **Файл:** [`lab3/network/moderation/content_filter.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/moderation/content_filter.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Автоматический анализатор контента на спам и нежелательный материал.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.filter_name: str` — внутренний атрибут объекта.
- `self.spam_threshold: float` — внутренний атрибут объекта.
- `self.nsfw_detection: bool` — внутренний атрибут объекта.
- `self.auto_block: bool` — внутренний атрибут объекта.
- `self.inspections_count: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, filter_name: str, spam_threshold: float, nsfw_detection: bool, auto_block: bool, inspections_count: int) -> None`
  - *Поведение:* Инициализация алгоритма фильтрации.
- **Методы бизнес-логики (поведение):**
  - `evaluate_spam_score(self, text: str) -> float`
    - *Описание:* Оценивает вероятность спама в текстовом фрагменте от 0.0 до 1.0.
  - `inspect_text(self, text: str, content_id: str) -> bool`
    - *Описание:* Проверяет текст и выбрасывает исключение при превышении порога спама.
    - *Возбуждаемые исключения:* `ContentBlockedException`
  - `update_threshold(self, new_threshold: float) -> None`
    - *Описание:* Настраивает чувствительность детектора спама.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `ContentBlockedException`.

---

### Класс `ModerationReport`
- **Файл:** [`lab3/network/moderation/moderation_report.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/moderation/moderation_report.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет жалобу пользователя на неприемлемый контент или поведение.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.report_id: str` — внутренний атрибут объекта.
- `self.reporter_id: str` — внутренний атрибут объекта.
- `self.target_id: str` — внутренний атрибут объекта.
- `self.reason: str` — внутренний атрибут объекта.
- `self.status: str` — внутренний атрибут объекта.
- `self.resolution: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, report_id: str, reporter_id: str, target_id: str, reason: str, status: str, resolution: str) -> None`
  - *Поведение:* Инициализация жалобы.
- **Методы бизнес-логики (поведение):**
  - `resolve(self, action: str) -> None`
    - *Описание:* Выносит положительное решение по жалобе.
    - *Возбуждаемые исключения:* `ReportAlreadyProcessedException`
  - `dismiss(self) -> None`
    - *Описание:* Отклоняет жалобу как необоснованную.
    - *Возбуждаемые исключения:* `ReportAlreadyProcessedException`
  - `is_pending(self) -> bool`
    - *Описание:* Проверяет, ожидает ли жалоба вердикта модератора.
  - `reported_by(self, user: UserAccount) -> bool`
    - *Описание:* Проверяет заявителя жалобы.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `ReportAlreadyProcessedException`, `UserAccount`.

---

### Класс `Moderator`
- **Файл:** [`lab3/network/moderation/moderator.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/moderation/moderator.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Сотрудник службы безопасности и модерации контента.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.moderator_id: str` — внутренний атрибут объекта.
- `self.badge_name: str` — внутренний атрибут объекта.
- `self.reports_reviewed: int` — внутренний атрибут объекта.
- `self.is_head_moderator: bool` — внутренний атрибут объекта.
- `self.permissions_level: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, moderator_id: str, badge_name: str, reports_reviewed: int, is_head_moderator: bool, permissions_level: int) -> None`
  - *Поведение:* Инициализация профиля модератора.
- **Методы бизнес-логики (поведение):**
  - `review_report(self, report: ModerationReport, verdict: str) -> bool`
    - *Описание:* Рассматривает инцидент и закрывает жалобу вердиктом.
  - `elevate_permissions(self, new_level: int) -> None`
    - *Описание:* Повышает уровень полномочий модератора.
    - *Возбуждаемые исключения:* `InsufficientPrivilegesException`
  - `can_ban_permanently(self) -> bool`
    - *Описание:* Проверяет право на бессрочную блокировку пользователя.
  - `assign_badge(self, user: UserAccount, title: str) -> str`
    - *Описание:* Назначает почетный или служебный бейдж пользователю.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `InsufficientPrivilegesException`, `ModerationReport`, `UserAccount`.

---

### Класс `Sanction`
- **Файл:** [`lab3/network/moderation/sanction.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/moderation/sanction.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет ограничение (бан, мут, предупреждение), наложенное на аккаунт.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.sanction_id: str` — внутренний атрибут объекта.
- `self.user_id: str` — внутренний атрибут объекта.
- `self.sanction_type: str` — внутренний атрибут объекта.
- `self.duration_days: int` — внутренний атрибут объекта.
- `self.reason: str` — внутренний атрибут объекта.
- `self.is_revoked: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, sanction_id: str, user_id: str, sanction_type: str, duration_days: int, reason: str, is_revoked: bool) -> None`
  - *Поведение:* Инициализация наложенной санкции.
- **Методы бизнес-логики (поведение):**
  - `revoke(self) -> None`
    - *Описание:* Досрочно аннулирует действующую санкцию.
  - `is_active_sanction(self, user: UserAccount) -> bool`
    - *Описание:* Проверяет актуальность санкции в отношении конкретного пользователя.
  - `extend_duration(self, extra_days: int) -> int`
    - *Описание:* Продлевает срок действия наложенного ограничения.
  - `apply_sanction(self) -> None`
    - *Описание:* Повторно активирует ранее снятую санкцию.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

## Экономика платформы, реклама и подписки (`lab3/network/monetization/`)

### Класс `AdCampaign`
- **Файл:** [`lab3/network/monetization/ad_campaign.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/monetization/ad_campaign.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Управляет таргетированной кампанией рекламодателя.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.campaign_id: str` — внутренний атрибут объекта.
- `self.sponsor_id: str` — внутренний атрибут объекта.
- `self.budget_total: float` — внутренний атрибут объекта.
- `self.spent_amount: float` — внутренний атрибут объекта.
- `self.is_active: bool` — внутренний атрибут объекта.
- `self.daily_limit: float` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, campaign_id: str, sponsor_id: str, budget_total: float, spent_amount: float, is_active: bool, daily_limit: float) -> None`
  - *Поведение:* Инициализация рекламной кампании.
- **Методы бизнес-логики (поведение):**
  - `charge_budget(self, cost: float) -> float`
    - *Описание:* Списывает затраты на показы и клики из рекламного бюджета.
    - *Возбуждаемые исключения:* `PaymentFailedException`
  - `pause(self) -> None`
    - *Описание:* Приостанавливает показы рекламных объявлений.
  - `resume(self) -> None`
    - *Описание:* Возобновляет рекламные показы.
  - `is_owned_by(self, sponsor: UserAccount) -> bool`
    - *Описание:* Проверяет принадлежность кампании рекламодателю.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `PaymentFailedException`, `UserAccount`.

---

### Класс `Advertisement`
- **Файл:** [`lab3/network/monetization/advertisement.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/monetization/advertisement.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет промо-материал, транслируемый в лентах пользователей.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.ad_id: str` — внутренний атрибут объекта.
- `self.campaign_id: str` — внутренний атрибут объекта.
- `self.title: str` — внутренний атрибут объекта.
- `self.target_url: str` — внутренний атрибут объекта.
- `self.clicks_count: int` — внутренний атрибут объекта.
- `self.impressions_count: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, ad_id: str, campaign_id: str, title: str, target_url: str, clicks_count: int, impressions_count: int) -> None`
  - *Поведение:* Инициализация рекламного блока.
- **Методы бизнес-логики (поведение):**
  - `record_impression(self, campaign: AdCampaign) -> int`
    - *Описание:* Регистрирует факт показа объявления и списывает CPM-стоимость.
  - `record_click(self, campaign: AdCampaign) -> int`
    - *Описание:* Регистрирует переход по ссылке рекламы и списывает CPC-стоимость.
  - `calculate_ctr(self) -> float`
    - *Описание:* Вычисляет показатель кликабельности (Click-Through Rate, %).

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `AdCampaign`.

---

### Класс `Subscription`
- **Файл:** [`lab3/network/monetization/subscription.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/monetization/subscription.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Управляет активной платной подпиской на автора или сервис.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.subscription_id: str` — внутренний атрибут объекта.
- `self.user_id: str` — внутренний атрибут объекта.
- `self.creator_id: str` — внутренний атрибут объекта.
- `self.tier_name: str` — внутренний атрибут объекта.
- `self.expires_at: str` — внутренний атрибут объекта.
- `self.auto_renew: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, subscription_id: str, user_id: str, creator_id: str, tier_name: str, expires_at: str, auto_renew: bool) -> None`
  - *Поведение:* Инициализация подписки.
- **Методы бизнес-логики (поведение):**
  - `renew(self, tier: SubscriptionTier, new_expiry: str) -> None`
    - *Описание:* Продлевает срок действия подписки.
  - `cancel_auto_renew(self) -> None`
    - *Описание:* Отключает автоматическое списание за продление.
  - `is_valid(self, current_date: str) -> bool`
    - *Описание:* Проверяет актуальность оплаченного периода.
    - *Возбуждаемые исключения:* `SubscriptionExpiredException`
  - `belongs_to_subscriber(self, user: UserAccount) -> bool`
    - *Описание:* Проверяет принадлежность подписки пользователю.
  - `enable_auto_renew(self) -> None`
    - *Описание:* Включает автоматическое списание за продление.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `SubscriptionExpiredException`, `SubscriptionTier`, `UserAccount`.

---

### Класс `SubscriptionTier`
- **Файл:** [`lab3/network/monetization/subscription_tier.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/monetization/subscription_tier.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Описывает тарифный план авторской или платформенной подписки.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.tier_id: str` — внутренний атрибут объекта.
- `self.name: str` — внутренний атрибут объекта.
- `self.monthly_price: float` — внутренний атрибут объекта.
- `self.benefits_count: int` — внутренний атрибут объекта.
- `self.badge_icon: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, tier_id: str, name: str, monthly_price: float, benefits_count: int, badge_icon: str) -> None`
  - *Поведение:* Инициализация тарифного плана.
- **Методы бизнес-логики (поведение):**
  - `is_affordable(self, budget: float) -> bool`
    - *Описание:* Проверяет, достаточно ли средств пользователя для оплаты месяца.
  - `add_benefit(self) -> int`
    - *Описание:* Увеличивает число включенных преимуществ тарифа.
  - `format_price_tag(self) -> str`
    - *Описание:* Формирует ценник подписки.

#### Связи с другими классами:
- **Ассоциации:** Автономный класс.

---

### Класс `Transaction`
- **Файл:** [`lab3/network/monetization/transaction.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/monetization/transaction.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет финансовый перевод между кошельками или оплату услуги.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.tx_id: str` — внутренний атрибут объекта.
- `self.sender_wallet_id: str` — внутренний атрибут объекта.
- `self.receiver_wallet_id: str` — внутренний атрибут объекта.
- `self.amount: float` — внутренний атрибут объекта.
- `self.status: str` — внутренний атрибут объекта.
- `self.fee: float` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, tx_id: str, sender_wallet_id: str, receiver_wallet_id: str, amount: float, status: str, fee: float) -> None`
  - *Поведение:* Инициализация транзакции.
- **Методы бизнес-логики (поведение):**
  - `execute(self, sender: Wallet, receiver: Wallet) -> bool`
    - *Описание:* Исполняет финансовую транзакцию с удержанием комиссии.
  - `refund(self, sender: Wallet, receiver: Wallet) -> None`
    - *Описание:* Выполняет возврат средств отправителю.
  - `calculate_fee(self, fee_percent: float) -> float`
    - *Описание:* Рассчитывает комиссию платежного шлюза.
  - `validate_amount(self) -> bool`
    - *Описание:* Проверяет корректность суммы платежа.
    - *Возбуждаемые исключения:* `PaymentFailedException`

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `PaymentFailedException`, `Wallet`.

---

### Класс `VirtualGift`
- **Файл:** [`lab3/network/monetization/virtual_gift.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/monetization/virtual_gift.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет подарочный стикер/сувенир, отправляемый в профиль.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.gift_id: str` — внутренний атрибут объекта.
- `self.gift_name: str` — внутренний атрибут объекта.
- `self.price_coins: int` — внутренний атрибут объекта.
- `self.icon_code: str` — внутренний атрибут объекта.
- `self.is_limited_edition: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, gift_id: str, gift_name: str, price_coins: int, icon_code: str, is_limited_edition: bool) -> None`
  - *Поведение:* Инициализация виртуального подарка.
- **Методы бизнес-логики (поведение):**
  - `send_gift(self, sender_wallet: Wallet, recipient: UserAccount) -> bool`
    - *Описание:* Списывает стоимость подарка с кошелька дарителя.
  - `format_gift_card(self) -> str`
    - *Описание:* Возвращает текстовое оформление подарка.
  - `apply_discount(self, discount_percent: int) -> int`
    - *Описание:* Применяет акционную скидку к стоимости подарка.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`, `Wallet`.

---

### Класс `Wallet`
- **Файл:** [`lab3/network/monetization/wallet.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/monetization/wallet.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Хранит денежный баланс и токены внутренней экономики сети.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.wallet_id: str` — внутренний атрибут объекта.
- `self.user_id: str` — внутренний атрибут объекта.
- `self.balance: float` — внутренний атрибут объекта.
- `self.currency: str` — внутренний атрибут объекта.
- `self.is_frozen: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, wallet_id: str, user_id: str, balance: float, currency: str, is_frozen: bool) -> None`
  - *Поведение:* Инициализация электронного кошелька.
- **Методы бизнес-логики (поведение):**
  - `deposit(self, amount: float) -> float`
    - *Описание:* Пополняет баланс кошелька.
    - *Возбуждаемые исключения:* `PaymentFailedException`
  - `withdraw(self, amount: float) -> float`
    - *Описание:* Списывает средства с баланса с проверкой остатка.
    - *Возбуждаемые исключения:* `PaymentFailedException`
  - `freeze(self) -> None`
    - *Описание:* Замораживает проведение операций по кошельку.
  - `unfreeze(self) -> None`
    - *Описание:* Размораживает баланс кошелька.
  - `belongs_to_user(self, user: UserAccount) -> bool`
    - *Описание:* Проверяет принадлежность кошелька владельцу.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `PaymentFailedException`, `UserAccount`.

---

## Новостные ленты, рекомендации и метрики (`lab3/network/analytics/`)

### Класс `EngagementMetrics`
- **Файл:** [`lab3/network/analytics/engagement_metrics.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/analytics/engagement_metrics.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Агрегирует статистику просмотров, репостов, закладок и реакций.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.post_id: str` — внутренний атрибут объекта.
- `self.views: int` — внутренний атрибут объекта.
- `self.likes: int` — внутренний атрибут объекта.
- `self.shares: int` — внутренний атрибут объекта.
- `self.bookmarks: int` — внутренний атрибут объекта.
- `self.comments_count: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, post_id: str, views: int, likes: int, shares: int, bookmarks: int, comments_count: int) -> None`
  - *Поведение:* Инициализация счетчиков вовлеченности.
- **Методы бизнес-логики (поведение):**
  - `calculate_engagement_rate(self) -> float`
    - *Описание:* Рассчитывает коэффициент вовлеченности (ER, %).
  - `record_share(self, post: Post) -> int`
    - *Описание:* Фиксирует распространение записи другим пользователем.
  - `record_bookmark(self) -> int`
    - *Описание:* Фиксирует сохранение записи в закладки.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `Post`.

---

### Класс `Feed`
- **Файл:** [`lab3/network/analytics/feed.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/analytics/feed.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Формирует и ранжирует новостную ленту для пользователя.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.user_id: str` — внутренний атрибут объекта.
- `self.algorithm_type: str` — внутренний атрибут объекта.
- `self.items_count: int` — внутренний атрибут объекта.
- `self.refresh_interval_sec: int` — внутренний атрибут объекта.
- `self.include_ads: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, user_id: str, algorithm_type: str, items_count: int, refresh_interval_sec: int, include_ads: bool) -> None`
  - *Поведение:* Инициализация ленты.
- **Методы бизнес-логики (поведение):**
  - `add_item(self, item: FeedItem) -> int`
    - *Описание:* Включает новую запись в ленту.
  - `filter_by_algorithm(self, user: UserAccount) -> str`
    - *Описание:* Применяет алгоритмическое либо хронологическое ранжирование.
  - `clear_feed(self) -> None`
    - *Описание:* Очищает кэшированные публикации в ленте.
  - `remove_item(self) -> int`
    - *Описание:* Удаляет элемент из ленты.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `FeedItem`, `UserAccount`.

---

### Класс `FeedItem`
- **Файл:** [`lab3/network/analytics/feed_item.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/analytics/feed_item.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет публикацию внутри ранжированной пользовательской ленты.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.item_id: str` — внутренний атрибут объекта.
- `self.post_id: str` — внутренний атрибут объекта.
- `self.relevance_score: float` — внутренний атрибут объекта.
- `self.source_type: str` — внутренний атрибут объекта.
- `self.seen: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, item_id: str, post_id: str, relevance_score: float, source_type: str, seen: bool) -> None`
  - *Поведение:* Инициализация элемента ленты.
- **Методы бизнес-логики (поведение):**
  - `mark_as_seen(self) -> None`
    - *Описание:* Помечает пост как просмотренный в ленте.
  - `boost_score(self, factor: float) -> float`
    - *Описание:* Повышает ранжирующий балл записи в ленте.
  - `penalize_score(self, penalty: float) -> float`
    - *Описание:* Понижает позицию записи в ленте за нерелевантность.
  - `matches_post(self, post: Post) -> bool`
    - *Описание:* Проверяет соответствие элемента конкретной публикации.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `Post`.

---

### Класс `RecommendationEngine`
- **Файл:** [`lab3/network/analytics/recommendation_engine.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/analytics/recommendation_engine.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Осуществляет расчет интересов и рекомендацию контента пользователям.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.model_version: str` — внутренний атрибут объекта.
- `self.diversity_factor: float` — внутренний атрибут объекта.
- `self.decay_rate: float` — внутренний атрибут объекта.
- `self.min_score_threshold: float` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, model_version: str, diversity_factor: float, decay_rate: float, min_score_threshold: float) -> None`
  - *Поведение:* Инициализация алгоритма рекомендаций.
- **Методы бизнес-логики (поведение):**
  - `score_post(self, post: Post, user: UserAccount) -> float`
    - *Описание:* Вычисляет предсказанную заинтересованность пользователя в записи.
  - `recommend_users(self, user: UserAccount, candidates: list) -> list`
    - *Описание:* Подбирает рекомендуемых друзей и авторов на основе сходства профилей.
  - `update_diversity(self, new_factor: float) -> None`
    - *Описание:* Обновляет параметр разнообразия рекомендаций (explore vs exploit).

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `Post`, `UserAccount`.

---

### Класс `TrendAnalyzer`
- **Файл:** [`lab3/network/analytics/trend_analyzer.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/analytics/trend_analyzer.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Выявляет быстрорастущие тренды и популярные обсуждения.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.window_hours: int` — внутренний атрибут объекта.
- `self.top_limit: int` — внутренний атрибут объекта.
- `self.velocity_multiplier: float` — внутренний атрибут объекта.
- `self.min_occurrences: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, window_hours: int, top_limit: int, velocity_multiplier: float, min_occurrences: int) -> None`
  - *Поведение:* Инициализация анализатора трендов.
- **Методы бизнес-логики (поведение):**
  - `identify_trending_topics(self, tags: list) -> list`
    - *Описание:* Фильтрует список тегов по критерию популярности.
  - `calculate_growth_velocity(self, count_now: int, count_before: int) -> float`
    - *Описание:* Рассчитывает скорость роста цитируемости инфоповода.
  - `adjust_window(self, hours: int) -> None`
    - *Описание:* Изменяет временное окно агрегации трендов.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `Hashtag`.

---

### Класс `UserStatistic`
- **Файл:** [`lab3/network/analytics/user_statistic.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/analytics/user_statistic.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Хранит сводную статистику активности пользователя в социальной сети.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.user_id: str` — внутренний атрибут объекта.
- `self.posts_published: int` — внутренний атрибут объекта.
- `self.comments_written: int` — внутренний атрибут объекта.
- `self.total_reactions_given: int` — внутренний атрибут объекта.
- `self.active_days: int` — внутренний атрибут объекта.
- `self.messages_sent: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, user_id: str, posts_published: int, comments_written: int, total_reactions_given: int, active_days: int, messages_sent: int) -> None`
  - *Поведение:* Инициализация персональной статистики.
- **Методы бизнес-логики (поведение):**
  - `increment_posts(self, user: UserAccount) -> int`
    - *Описание:* Увеличивает счетчик опубликованных постов.
  - `increment_comments(self) -> int`
    - *Описание:* Увеличивает счетчик оставленных комментариев.
  - `record_active_day(self) -> int`
    - *Описание:* Увеличивает счетчик дней посещения социальной сети.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

## Шлюзы и агрегация уведомлений (`lab3/network/notification/`)

### Класс `Notification`
- **Файл:** [`lab3/network/notification/notification.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/notification/notification.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Представляет системное уведомление о событиях (лайк, ответ, подписка).

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.notification_id: str` — внутренний атрибут объекта.
- `self.recipient_id: str` — внутренний атрибут объекта.
- `self.actor_id: str` — внутренний атрибут объекта.
- `self.event_type: str` — внутренний атрибут объекта.
- `self.is_read: bool` — внутренний атрибут объекта.
- `self.created_at: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, notification_id: str, recipient_id: str, actor_id: str, event_type: str, is_read: bool, created_at: str) -> None`
  - *Поведение:* Инициализация уведомления.
- **Методы бизнес-логики (поведение):**
  - `mark_as_read(self, recipient: UserAccount) -> bool`
    - *Описание:* Помечает уведомление как прочитанное адресатом.
  - `format_message(self) -> str`
    - *Описание:* Форматирует текст уведомления на основе типа события.
  - `is_urgent(self) -> bool`
    - *Описание:* Проверяет критичность уведомления для мгновенной доставки.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

### Класс `NotificationBatch`
- **Файл:** [`lab3/network/notification/notification_batch.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/notification/notification_batch.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Группирует однотипные уведомления для предотвращения спама.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.batch_id: str` — внутренний атрибут объекта.
- `self.recipient_id: str` — внутренний атрибут объекта.
- `self.count: int` — внутренний атрибут объекта.
- `self.event_category: str` — внутренний атрибут объекта.
- `self.is_dispatched: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, batch_id: str, recipient_id: str, count: int, event_category: str, is_dispatched: bool) -> None`
  - *Поведение:* Инициализация пакета уведомлений.
- **Методы бизнес-логики (поведение):**
  - `aggregate(self, notification: Notification) -> int`
    - *Описание:* Добавляет единичное уведомление в накопительный пакет.
  - `dispatch(self, recipient: UserAccount) -> str`
    - *Описание:* Формирует и отправляет сводное уведомление пользователю.
  - `is_empty_batch(self) -> bool`
    - *Описание:* Проверяет, пуст ли текущий пакет уведомлений.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `Notification`, `UserAccount`.

---

### Класс `NotificationChannel`
- **Файл:** [`lab3/network/notification/notification_channel.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/notification/notification_channel.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Описывает транспорт доставки сообщений (Push, Email, SMS, Web).

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.channel_name: str` — внутренний атрибут объекта.
- `self.is_enabled: bool` — внутренний атрибут объекта.
- `self.delivery_timeout_sec: int` — внутренний атрибут объекта.
- `self.retry_count: int` — внутренний атрибут объекта.
- `self.priority: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, channel_name: str, is_enabled: bool, delivery_timeout_sec: int, retry_count: int, priority: int) -> None`
  - *Поведение:* Инициализация канала уведомлений.
- **Методы бизнес-логики (поведение):**
  - `deliver(self, notification: Notification) -> bool`
    - *Описание:* Осуществляет отправку уведомления через выбранный канал.
  - `toggle_channel(self) -> bool`
    - *Описание:* Включает или выключает данный транспорт доставки.
  - `adjust_timeout(self, seconds: int) -> None`
    - *Описание:* Настраивает таймаут ожидания ответа шлюза.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `Notification`.

---

## Аутентификация, токены и защита (`lab3/network/security/`)

### Класс `SecurityLog`
- **Файл:** [`lab3/network/security/security_log.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/security/security_log.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Регистрирует попытки входа, смены паролей и потенциальные угрозы.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.event_id: str` — внутренний атрибут объекта.
- `self.user_id: str` — внутренний атрибут объекта.
- `self.ip_address: str` — внутренний атрибут объекта.
- `self.event_name: str` — внутренний атрибут объекта.
- `self.status: str` — внутренний атрибут объекта.
- `self.timestamp: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, event_id: str, user_id: str, ip_address: str, event_name: str, status: str, timestamp: str) -> None`
  - *Поведение:* Инициализация записи журнала безопасности.
- **Методы бизнес-логики (поведение):**
  - `is_suspicious(self) -> bool`
    - *Описание:* Выявляет признаки вредоносной активности (подбор пароля, брутфорс).
  - `format_audit_string(self) -> str`
    - *Описание:* Форматирует строку отчета для офицера ИБ.
  - `flag_failed_attempt(self, user: UserAccount) -> None`
    - *Описание:* Фиксирует неудачную попытку доступа к аккаунту.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `UserAccount`.

---

### Класс `SessionToken`
- **Файл:** [`lab3/network/security/session_token.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/security/session_token.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Управляет жизненным циклом токена веб-сессии пользователя.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.token_value: str` — внутренний атрибут объекта.
- `self.user_id: str` — внутренний атрибут объекта.
- `self.ip_address: str` — внутренний атрибут объекта.
- `self.device_info: str` — внутренний атрибут объекта.
- `self.expires_in_hours: int` — внутренний атрибут объекта.
- `self.is_active: bool` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, token_value: str, user_id: str, ip_address: str, device_info: str, expires_in_hours: int, is_active: bool) -> None`
  - *Поведение:* Инициализация сессионного токена.
- **Методы бизнес-логики (поведение):**
  - `validate(self, current_user: UserAccount) -> bool`
    - *Описание:* Проверяет валидность токена и активность связанного аккаунта.
    - *Возбуждаемые исключения:* `AuthenticationException`
  - `revoke(self) -> None`
    - *Описание:* Осуществляет отзыв (выход из аккаунта) текущей сессии.
  - `renew(self, extension_hours: int) -> int`
    - *Описание:* Продлевает срок жизни активной сессии.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `AuthenticationException`, `UserAccount`.

---

### Класс `TwoFactorAuth`
- **Файл:** [`lab3/network/security/two_factor_auth.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/security/two_factor_auth.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Управляет подтверждением входа через TOTP-коды или резервные ключи.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.user_id: str` — внутренний атрибут объекта.
- `self.method: str` — внутренний атрибут объекта.
- `self.secret_hash: str` — внутренний атрибут объекта.
- `self.is_enabled: bool` — внутренний атрибут объекта.
- `self.backup_codes_left: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, user_id: str, method: str, secret_hash: str, is_enabled: bool, backup_codes_left: int) -> None`
  - *Поведение:* Инициализация параметров 2FA.
- **Методы бизнес-логики (поведение):**
  - `verify_otp(self, code: str) -> bool`
    - *Описание:* Верифицирует введенный одноразовый шестизначный пароль.
    - *Возбуждаемые исключения:* `AuthenticationException`
  - `enable_2fa(self, user: UserAccount) -> None`
    - *Описание:* Активирует двухфакторную защиту для учетной записи.
  - `use_backup_code(self) -> int`
    - *Описание:* Списывает один из резервных одноразовых кодов восстановления.
    - *Возбуждаемые исключения:* `AuthenticationException`
  - `disable_2fa(self, user: UserAccount) -> None`
    - *Описание:* Деактивирует двухфакторную защиту для учетной записи.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `AuthenticationException`, `UserAccount`.

---

## Системный фасад и поисковые индексы (`lab3/network/system/`)

### Класс `DataBackup`
- **Файл:** [`lab3/network/system/data_backup.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/system/data_backup.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Управляет созданием и проверкой целостности бэкапов социальной сети.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.backup_id: str` — внутренний атрибут объекта.
- `self.file_path: str` — внутренний атрибут объекта.
- `self.size_mb: float` — внутренний атрибут объекта.
- `self.status: str` — внутренний атрибут объекта.
- `self.is_encrypted: bool` — внутренний атрибут объекта.
- `self.checksum: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, backup_id: str, file_path: str, size_mb: float, status: str, is_encrypted: bool, checksum: str) -> None`
  - *Поведение:* Инициализация архива резервной копии.
- **Методы бизнес-логики (поведение):**
  - `create_snapshot(self, data_size_mb: float) -> str`
    - *Описание:* Формирует снимок данных и фиксирует его размер.
  - `verify_checksum(self, expected_hash: str) -> bool`
    - *Описание:* Сверяет контрольную сумму снапшота для подтверждения целостности.
  - `mark_corrupted(self) -> None`
    - *Описание:* Помечает резервную копию как поврежденную.
  - `restore_snapshot(self) -> str`
    - *Описание:* Восстанавливает статус резервной копии как готовой к использованию.

#### Связи с другими классами:
- **Ассоциации:** Автономный класс.

---

### Класс `SearchService`
- **Файл:** [`lab3/network/system/search_service.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/system/search_service.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Обеспечивает полнотекстовый поиск по пользователям, публикациям и тегам.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.index_name: str` — внутренний атрибут объекта.
- `self.indexed_items_count: int` — внутренний атрибут объекта.
- `self.min_query_length: int` — внутренний атрибут объекта.
- `self.fuzzy_matching: bool` — внутренний атрибут объекта.
- `self.max_results: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, index_name: str, indexed_items_count: int, min_query_length: int, fuzzy_matching: bool, max_results: int) -> None`
  - *Поведение:* Инициализация поискового индекса.
- **Методы бизнес-логики (поведение):**
  - `search_users(self, query: str, user_pool: list) -> list`
    - *Описание:* Выполняет поиск пользователей по логину.
  - `search_posts(self, query: str, post_pool: list) -> list`
    - *Описание:* Выполняет поиск публикаций по ключевым словам.
  - `index_document(self, tag: Hashtag) -> int`
    - *Описание:* Индексирует хэштег для быстрого автодополнения.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `Hashtag`, `Post`, `UserAccount`.

---

### Класс `SocialNetworkSystem`
- **Файл:** [`lab3/network/system/social_network_system.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/system/social_network_system.py)
- **Базовый класс:** `object` (корневой объект Python)
- **Что делает:** Центральный координатор доменной модели социальной сети.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.network_name: str` — внутренний атрибут объекта.
- `self.users_count: int` — внутренний атрибут объекта.
- `self.posts_count: int` — внутренний атрибут объекта.
- `self.is_maintenance_mode: bool` — внутренний атрибут объекта.
- `self.version: str` — внутренний атрибут объекта.
- `self.max_daily_posts: int` — внутренний атрибут объекта.
- `self.support_email: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, network_name: str, users_count: int, posts_count: int, is_maintenance_mode: bool, version: str, max_daily_posts: int, support_email: str) -> None`
  - *Поведение:* Инициализация управляющей системы социальной сети.
- **Методы бизнес-логики (поведение):**
  - `register_user(self, user: UserAccount) -> int`
    - *Описание:* Регистрирует нового пользователя в платформе.
    - *Возбуждаемые исключения:* `UserNotFoundException`
  - `publish_post(self, post: Post) -> int`
    - *Описание:* Публикует новый пост в единой базе сети с контролем лимитов.
    - *Возбуждаемые исключения:* `RateLimitExceededException`
  - `enable_maintenance(self) -> None`
    - *Описание:* Переводит сервис в режим технического обслуживания.
  - `disable_maintenance(self) -> None`
    - *Описание:* Возвращает платформу в штатный режим работы.
  - `generate_system_report(self) -> str`
    - *Описание:* Формирует системную сводку о состоянии социальной сети.
  - `remove_user(self, user: UserAccount) -> int`
    - *Описание:* Исключает пользователя из системы.
  - `delete_post(self, post: Post) -> int`
    - *Описание:* Удаляет публикацию из глобального реестра.

#### Связи с другими классами:
- **Ассоциации и коллаборации:** Взаимодействует с `Post`, `RateLimitExceededException`, `UserAccount`, `UserNotFoundException`.

---

## Иерархия исключений предметной области (`lab3/network/exceptions/`)

### Класс `AccessDeniedException`
- **Файл:** [`lab3/network/exceptions/access_denied_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/access_denied_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается при попытке доступа к приватному или заблокированному ресурсу.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.resource: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, resource: str) -> None`
  - *Поведение:* Инициализация исключения отказа в доступе.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---

### Класс `AuthenticationException`
- **Файл:** [`lab3/network/exceptions/authentication_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/authentication_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается при неверном пароле или недействительном токене.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.reason: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, reason: str) -> None`
  - *Поведение:* Инициализация исключения аутентификации.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---

### Класс `ContentBlockedException`
- **Файл:** [`lab3/network/exceptions/content_blocked_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/content_blocked_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается при обращении к материалу, заблокированному модератором.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.content_id: str` — внутренний атрибут объекта.
- `self.reason: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, content_id: str, reason: str) -> None`
  - *Поведение:* Инициализация исключения блокировки контента.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---

### Класс `ContentNotFoundException`
- **Файл:** [`lab3/network/exceptions/content_not_found_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/content_not_found_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается при попытке найти несуществующую публикацию, историю или комментарий.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.content_id: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, content_id: str) -> None`
  - *Поведение:* Инициализация исключения отсутствия контента.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---

### Класс `FriendshipAlreadyExistsException`
- **Файл:** [`lab3/network/exceptions/friendship_already_exists_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/friendship_already_exists_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается при повторной отправке заявки в друзья или существующей дружбе.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.user_pair: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, user_pair: str) -> None`
  - *Поведение:* Инициализация исключения дублирования дружбы.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---

### Класс `GroupCapacityExceededException`
- **Файл:** [`lab3/network/exceptions/group_capacity_exceeded_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/group_capacity_exceeded_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается при попытке вступить в переполненную группу или чат.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.max_limit: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, max_limit: int) -> None`
  - *Поведение:* Инициализация исключения переполнения группы.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---

### Класс `GroupNotFoundException`
- **Файл:** [`lab3/network/exceptions/group_not_found_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/group_not_found_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается при поиске несуществующего сообщества или группы.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.group_id: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, group_id: str) -> None`
  - *Поведение:* Инициализация исключения отсутствия группы.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---

### Класс `InsufficientPrivilegesException`
- **Файл:** [`lab3/network/exceptions/insufficient_privileges_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/insufficient_privileges_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается при нехватке полномочий модератора или администратора.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.action: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, action: str) -> None`
  - *Поведение:* Инициализация исключения нехватки прав.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---

### Класс `InvalidContentException`
- **Файл:** [`lab3/network/exceptions/invalid_content_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/invalid_content_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается при нарушении формата текста, длины или недопустимых символах.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.details: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, details: str) -> None`
  - *Поведение:* Инициализация исключения некорректного контента.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---

### Класс `NetworkBaseException`
- **Файл:** [`lab3/network/exceptions/network_base_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/network_base_exception.py)
- **Базовый класс:** `Exception`
- **Что делает:** Базовый класс для всех ошибок и исключений социальной сети.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.message: str` — внутренний атрибут объекта.
- `self.code: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, message: str, code: int) -> None`
  - *Поведение:* Инициализация базового исключения.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `Exception`.
- **Ассоциации:** Автономный класс.

---

### Класс `PaymentFailedException`
- **Файл:** [`lab3/network/exceptions/payment_failed_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/payment_failed_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается при неудачном списании средств или недостатке баланса.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.reason: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, reason: str) -> None`
  - *Поведение:* Инициализация исключения платежа.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---

### Класс `RateLimitExceededException`
- **Файл:** [`lab3/network/exceptions/rate_limit_exceeded_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/rate_limit_exceeded_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается при превышении допустимого лимита запросов или сообщений.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.limit: int` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, limit: int) -> None`
  - *Поведение:* Инициализация исключения лимита запросов.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---

### Класс `ReportAlreadyProcessedException`
- **Файл:** [`lab3/network/exceptions/report_already_processed_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/report_already_processed_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается при попытке повторно вынести решение по закрытой жалобе.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.report_id: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, report_id: str) -> None`
  - *Поведение:* Инициализация исключения повторной обработки жалобы.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---

### Класс `SubscriptionExpiredException`
- **Файл:** [`lab3/network/exceptions/subscription_expired_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/subscription_expired_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается при попытке доступа к премиум-функции с истекшей подпиской.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.tier_name: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, tier_name: str) -> None`
  - *Поведение:* Инициализация исключения истечения подписки.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---

### Класс `UserAlreadyBlockedException`
- **Файл:** [`lab3/network/exceptions/user_already_blocked_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/user_already_blocked_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается при попытке повторно заблокировать пользователя.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.target_user_id: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, target_user_id: str) -> None`
  - *Поведение:* Инициализация исключения повторной блокировки.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---

### Класс `UserNotFoundException`
- **Файл:** [`lab3/network/exceptions/user_not_found_exception.py`](file:///C:/Users/hxtxf/source/repos/ppois-lab/lab3/network/exceptions/user_not_found_exception.py)
- **Базовый класс:** `NetworkBaseException`
- **Что делает:** Вызывается, если пользователь не найден в системе.

#### Как работает:
**Поля экземпляра (структура состояния):**
- `self.user_id: str` — внутренний атрибут объекта.

- **Конструктор:** `__init__(self, user_id: str) -> None`
  - *Поведение:* Инициализация исключения отсутствия пользователя.
- **Методы:** Только конструктор и унаследованное поведение.

#### Связи с другими классами:
- **Наследование:** Расширяет поведение базового класса `NetworkBaseException`.
- **Ассоциации и коллаборации:** Взаимодействует с `NetworkBaseException`.

---
