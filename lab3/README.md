# Лабораторная работа №3. Крупный ООП-проект
## Предметная область: Социальная сеть

### Описание проекта
Данный проект представляет собой детальную объектно-ориентированную модель масштабной платформы социальной сети (аналога ВКонтакте, Telegram, Facebook). Архитектура системы охватывает управление учетными записями, профилями и приватностью, публикацию текстового, мультимедийного контента, опросов, историй (Stories) и фотоальбомов, подсистемы личных сообщений и групповых чатов, голосовых и видеовызовов, социальные связи (дружба, подписки, группы, мероприятия, черный список), многоуровневую модерацию, систему жалоб и цензуры, монетизацию (платные подписки, виртуальные подарки, кошельки, рекламные кампании), новостные ленты и алгоритмы рекомендаций, аналитику вовлеченности аудитории, многофакторную безопасность и системное администрирование.

### Структура проекта и архитектурные правила
- Язык программирования: **Python 3**.
- **Строго 1 класс на 1 файл**: каждый класс доменной модели и каждое исключение вынесены в отдельный `.py`-файл.
- Все комментарии, документация и docstring выполнены на **русском языке**.
- Использована стандартная библиотека Python (запуск тестов через стандартный `unittest`).

## Таблица классов предметной области

Формат строки: `Класс | число полей | число методов | связанные классы`.

| Класс | Поля | Методы | Ассоциации (связанные классы) |
|---|---|---|---|
| AdCampaign | 6 | 4 | PaymentFailedException, UserAccount |
| Advertisement | 6 | 3 | AdCampaign |
| Album | 6 | 3 | MediaAttachment, UserAccount |
| Appeal | 6 | 4 | Sanction, UserAccount |
| AudioMessage | 5 | 3 | InvalidContentException |
| AuditLog | 5 | 3 | UserAccount |
| BannedWordFilter | 4 | 3 | InvalidContentException |
| BlockRecord | 5 | 3 | UserAccount |
| CallSession | 6 | 3 | UserAccount |
| Chat | 5 | 3 | — |
| ChatMember | 5 | 3 | UserAccount |
| ChatMessage | 6 | 3 | Chat, UserAccount |
| Comment | 6 | 4 | Post, Reaction, UserAccount |
| ContactInfo | 5 | 3 | InvalidContentException |
| ContentFilter | 5 | 3 | ContentBlockedException |
| DataBackup | 6 | 3 | — |
| DirectMessage | 6 | 3 | AccessDeniedException, UserAccount |
| EngagementMetrics | 6 | 3 | Post |
| Feed | 5 | 3 | FeedItem, UserAccount |
| FeedItem | 5 | 4 | Post |
| Follow | 4 | 3 | UserAccount |
| FriendRequest | 5 | 3 | Friendship, UserAccount |
| Friendship | 5 | 3 | UserAccount |
| GroupChat | 6 | 4 | Chat, ChatMember, GroupCapacityExceededException |
| GroupEvent | 6 | 3 | GroupCapacityExceededException, UserAccount |
| GroupMembership | 5 | 3 | InsufficientPrivilegesException, UserAccount |
| Hashtag | 4 | 3 | InvalidContentException |
| MediaAttachment | 6 | 4 | InvalidContentException |
| MediaPost | 6 | 3 | MediaAttachment, Post |
| ModerationReport | 6 | 4 | ReportAlreadyProcessedException, UserAccount |
| Moderator | 5 | 4 | InsufficientPrivilegesException, ModerationReport, UserAccount |
| Notification | 6 | 3 | UserAccount |
| NotificationBatch | 5 | 3 | Notification, UserAccount |
| NotificationChannel | 5 | 3 | Notification |
| PollOption | 4 | 3 | — |
| PollPost | 6 | 4 | InvalidContentException, PollOption, Post |
| Post | 6 | 4 | ContentBlockedException, InvalidContentException, UserAccount |
| Reaction | 4 | 3 | UserAccount |
| RecommendationEngine | 4 | 3 | Post, UserAccount |
| Sanction | 6 | 3 | UserAccount |
| SearchService | 5 | 3 | Hashtag, Post, UserAccount |
| SecurityLog | 6 | 3 | UserAccount |
| SessionToken | 6 | 3 | AuthenticationException, UserAccount |
| SocialNetworkSystem | 7 | 5 | Post, RateLimitExceededException, UserAccount, UserNotFoundException |
| Story | 6 | 4 | UserAccount |
| StoryViewer | 4 | 3 | UserAccount |
| Subscription | 6 | 4 | SubscriptionExpiredException, SubscriptionTier, UserAccount |
| SubscriptionTier | 5 | 3 | — |
| TextPost | 6 | 3 | Post |
| Transaction | 6 | 4 | PaymentFailedException, Wallet |
| TrendAnalyzer | 4 | 3 | Hashtag |
| TwoFactorAuth | 5 | 3 | AuthenticationException, UserAccount |
| UserAccount | 6 | 6 | AuthenticationException, UserProfile, UserSettings |
| UserActivity | 5 | 3 | UserAccount |
| UserGroup | 6 | 5 | GroupMembership, UserAccount |
| UserPrivacy | 5 | 3 | AccessDeniedException |
| UserProfile | 5 | 3 | ContactInfo, UserPrivacy |
| UserReputation | 5 | 4 | UserAccount |
| UserSettings | 5 | 3 | — |
| UserStatistic | 6 | 3 | UserAccount |
| VirtualGift | 5 | 3 | UserAccount, Wallet |
| Wallet | 5 | 5 | PaymentFailedException, UserAccount |

### Исключения (16)

- **AccessDeniedException** — Вызывается при попытке доступа к приватному или заблокированному ресурсу.
- **AuthenticationException** — Вызывается при неверном пароле или недействительном токене.
- **ContentBlockedException** — Вызывается при обращении к материалу, заблокированному модератором.
- **ContentNotFoundException** — Вызывается при попытке найти несуществующую публикацию, историю или комментарий.
- **FriendshipAlreadyExistsException** — Вызывается при повторной отправке заявки в друзья или существующей дружбе.
- **GroupCapacityExceededException** — Вызывается при попытке вступить в переполненную группу или чат.
- **GroupNotFoundException** — Вызывается при поиске несуществующего сообщества или группы.
- **InsufficientPrivilegesException** — Вызывается при нехватке полномочий модератора или администратора.
- **InvalidContentException** — Вызывается при нарушении формата текста, длины или недопустимых символах.
- **NetworkBaseException** — Базовый класс для всех ошибок и исключений социальной сети.
- **PaymentFailedException** — Вызывается при неудачном списании средств или недостатке баланса.
- **RateLimitExceededException** — Вызывается при превышении допустимого лимита запросов или сообщений.
- **ReportAlreadyProcessedException** — Вызывается при попытке повторно вынести решение по закрытой жалобе.
- **SubscriptionExpiredException** — Вызывается при попытке доступа к премиум-функции с истекшей подпиской.
- **UserAlreadyBlockedException** — Вызывается при попытке повторно заблокировать пользователя.
- **UserNotFoundException** — Вызывается, если пользователь не найден в системе.

### Итоговая статистика проекта

| Показатель | Значение | Требование |
|---|---|---|
| Классы (всего) | 78 | не менее 50 |
| Доменные классы | 62 | — |
| Исключения | 16 | не менее 12 |
| Поля (суммарно) | 350 | не менее 150 |
| Поведения (методы) | 209 | не менее 100 |
| Ассоциации | 111 | не менее 30 |
| Файлов с >1 классом | 0 | 0 (запрещено) |

## Подробное описание подсистем социальной сети

### Ядро профилей и учетных записей (`network/core/`)

#### Класс `ContactInfo`
*Хранит контактную информацию и геолокационные данные профиля.*
- **Поля (5)**: `city`, `country`, `is_phone_confirmed`, `phone`, `telegram_handle`
- **Методы (3)**: `confirm_phone()`, `format_location()`, `update_phone()`
- **Ассоциации**: InvalidContentException

#### Класс `UserAccount`
*Содержит учетные данные, логин, пароль и статус аккаунта.*
- **Поля (6)**: `created_at`, `email`, `is_active`, `password_hash`, `user_id`, `username`
- **Методы (6)**: `verify_password()`, `change_password()`, `deactivate()`, `activate()`, `bind_profile()`, `bind_settings()`
- **Ассоциации**: AuthenticationException, UserProfile, UserSettings

#### Класс `UserActivity`
*Отслеживает историю авторизаций, серию посещений и сетевой статус.*
- **Поля (5)**: `current_status`, `is_online`, `last_login_at`, `login_streak_days`, `total_sessions`
- **Методы (3)**: `record_login()`, `set_status()`, `go_offline()`
- **Ассоциации**: UserAccount

#### Класс `UserPrivacy`
*Определяет параметры видимости профиля и ограничения доступа.*
- **Поля (5)**: `allow_messages_from_strangers`, `blocked_users_count`, `profile_visibility`, `searchable_by_phone`, `show_online_status`
- **Методы (3)**: `set_visibility()`, `can_receive_message_from()`, `toggle_online_status()`
- **Ассоциации**: AccessDeniedException

#### Класс `UserProfile`
*Представляет публичный профиль участника социальной сети.*
- **Поля (5)**: `avatar_url`, `bio`, `birth_date`, `is_verified`, `website`
- **Методы (3)**: `update_bio()`, `verify_profile()`, `format_profile_card()`
- **Ассоциации**: ContactInfo, UserPrivacy

#### Класс `UserReputation`
*Управляет очками кармы, уровнем доверия и предупреждениями.*
- **Поля (5)**: `badge_title`, `is_shadow_banned`, `karma_points`, `trust_level`, `warnings_count`
- **Методы (4)**: `add_karma()`, `deduct_karma()`, `issue_warning()`, `calculate_trust_rank()`
- **Ассоциации**: UserAccount

#### Класс `UserSettings`
*Хранит персональные интерфейсные предпочтения и каналы уведомлений.*
- **Поля (5)**: `email_notifications`, `language`, `push_notifications`, `sound_enabled`, `theme`
- **Методы (3)**: `switch_theme()`, `toggle_push()`, `change_language()`

### Публикации, медиа и интерактивный контент (`network/content/`)

#### Класс `Album`
*Коллекция сохраненных фотографий и медиафайлов.*
- **Поля (6)**: `album_id`, `description`, `is_private`, `owner_id`, `photos_count`, `title`
- **Методы (3)**: `add_photo()`, `remove_photo()`, `toggle_privacy()`
- **Ассоциации**: MediaAttachment, UserAccount

#### Класс `Comment`
*Представляет комментарий пользователя под записью.*
- **Поля (6)**: `author_id`, `comment_id`, `is_hidden`, `likes_count`, `post_id`, `text`
- **Методы (4)**: `like()`, `hide()`, `edit_text()`, `belongs_to_post()`
- **Ассоциации**: Post, Reaction, UserAccount

#### Класс `Hashtag`
*Хранит информацию о поисковом хэштеге и частоте его использования.*
- **Поля (4)**: `is_blacklisted`, `tag_name`, `trending_score`, `usage_count`
- **Методы (3)**: `increment_usage()`, `update_trend_score()`, `validate_tag()`
- **Ассоциации**: InvalidContentException

#### Класс `MediaAttachment`
*Описывает прикрепленный медиафайл (фотография, видеоролик, документ).*
- **Поля (6)**: `attachment_id`, `file_size_bytes`, `file_url`, `height`, `mime_type`, `width`
- **Методы (4)**: `is_image()`, `is_video()`, `format_file_size()`, `validate_url()`
- **Ассоциации**: InvalidContentException

#### Класс `MediaPost`
*Публикация, содержащая фотографии или видеогалерею.*
- **Поля (6)**: `alt_description`, `aspect_ratio`, `filter_preset`, `has_watermark`, `media_count`, `post_id`
- **Методы (3)**: `add_media_item()`, `apply_filter()`, `verify_attachments()`
- **Ассоциации**: MediaAttachment, Post

#### Класс `PollOption`
*Представляет отдельный вариант ответа в голосовании.*
- **Поля (4)**: `option_id`, `option_text`, `percentage`, `votes_count`
- **Методы (3)**: `increment_vote()`, `update_percentage()`, `format_label()`

#### Класс `PollPost`
*Публикация с голосованием и вариантами ответов.*
- **Поля (6)**: `is_anonymous`, `is_closed`, `max_choices`, `post_id`, `question`, `total_votes`
- **Методы (4)**: `close_poll()`, `add_vote()`, `calculate_results()`, `can_vote()`
- **Ассоциации**: InvalidContentException, PollOption, Post

#### Класс `Post`
*Представляет запись на стене пользователя или в ленте социальной сети.*
- **Поля (6)**: `author_id`, `created_at`, `is_deleted`, `is_pinned`, `post_id`, `text_content`
- **Методы (4)**: `pin()`, `unpin()`, `soft_delete()`, `edit_content()`
- **Ассоциации**: ContentBlockedException, InvalidContentException, UserAccount

#### Класс `Reaction`
*Представляет эмоциональную реакцию пользователя на пост или комментарий.*
- **Поля (4)**: `created_at`, `reaction_type`, `target_id`, `user_id`
- **Методы (3)**: `update_type()`, `is_positive()`, `get_emoji()`
- **Ассоциации**: UserAccount

#### Класс `Story`
*Представляет короткую историю с ограниченным сроком жизни (24 часа).*
- **Поля (6)**: `author_id`, `duration_seconds`, `is_expired`, `media_url`, `story_id`, `views_count`
- **Методы (4)**: `record_view()`, `check_expiration()`, `archive()`, `add_interactive_sticker()`
- **Ассоциации**: UserAccount

#### Класс `StoryViewer`
*Фиксирует факт просмотра конкретной истории пользователем.*
- **Поля (4)**: `has_reacted`, `story_id`, `viewed_at`, `viewer_id`
- **Методы (3)**: `mark_reaction()`, `get_watch_delay()`, `format_viewer_info()`
- **Ассоциации**: UserAccount

#### Класс `TextPost`
*Специализированная текстовая запись с расширенным оформлением.*
- **Поля (6)**: `background_color`, `font_style`, `post_id`, `reading_time_minutes`, `summary`, `word_count`
- **Методы (3)**: `calculate_reading_time()`, `generate_summary()`, `apply_styling()`
- **Ассоциации**: Post

### Обмен сообщениями, чаты и звонки (`network/communication/`)

#### Класс `AudioMessage`
*Представляет голосовое сообщение с расшифровкой речи в текст.*
- **Поля (5)**: `audio_id`, `audio_url`, `duration_seconds`, `transcription`, `waveform_samples`
- **Методы (3)**: `transcribe()`, `is_long_audio()`, `format_duration()`
- **Ассоциации**: InvalidContentException

#### Класс `CallSession`
*Представляет сеанс аудио- или видеозвонка между пользователями.*
- **Поля (6)**: `call_id`, `duration_seconds`, `initiator_id`, `is_video`, `quality_score`, `status`
- **Методы (3)**: `start_call()`, `end_call()`, `rate_quality()`
- **Ассоциации**: UserAccount

#### Класс `Chat`
*Представляет диалог в системе сообщений.*
- **Поля (5)**: `chat_id`, `created_at`, `is_archived`, `last_message_at`, `messages_count`
- **Методы (3)**: `archive()`, `unarchive()`, `update_last_activity()`

#### Класс `ChatMember`
*Определяет роль и статус участника группового чата.*
- **Поля (5)**: `chat_id`, `is_banned`, `joined_at`, `member_id`, `role`
- **Методы (3)**: `promote_to_admin()`, `demote()`, `ban()`
- **Ассоциации**: UserAccount

#### Класс `ChatMessage`
*Сообщение, отправленное внутри группового или парного чата.*
- **Поля (6)**: `chat_id`, `is_pinned`, `message_id`, `reply_to_id`, `sender_id`, `text`
- **Методы (3)**: `pin()`, `unpin()`, `set_reply()`
- **Ассоциации**: Chat, UserAccount

#### Класс `DirectMessage`
*Представляет приватное сообщение диалога двух участников.*
- **Поля (6)**: `content`, `is_delivered`, `is_read`, `message_id`, `recipient_id`, `sender_id`
- **Методы (3)**: `mark_as_read()`, `mark_as_delivered()`, `format_preview()`
- **Ассоциации**: AccessDeniedException, UserAccount

#### Класс `GroupChat`
*Управляет групповой многопользовательской беседой.*
- **Поля (6)**: `admin_id`, `chat_id`, `invite_code`, `is_muted`, `members_limit`, `title`
- **Методы (4)**: `add_participant()`, `remove_participant()`, `generate_invite()`, `mute()`
- **Ассоциации**: Chat, ChatMember, GroupCapacityExceededException

### Социальный граф, дружба и сообщества (`network/relations/`)

#### Класс `BlockRecord`
*Представляет запись о блокировке нежелательного пользователя.*
- **Поля (5)**: `blocked_id`, `blocker_id`, `created_at`, `is_active`, `reason`
- **Методы (3)**: `deactivate()`, `matches_pair()`, `format_block_notice()`
- **Ассоциации**: UserAccount

#### Класс `Follow`
*Представляет одностороннюю подписку на обновления автора.*
- **Поля (4)**: `follower_id`, `notifications_enabled`, `started_at`, `target_id`
- **Методы (3)**: `toggle_notifications()`, `get_follow_duration_days()`, `unfollow()`
- **Ассоциации**: UserAccount

#### Класс `FriendRequest`
*Представляет входящую заявку на дружбу с сопроводительным сообщением.*
- **Поля (5)**: `message`, `receiver_id`, `request_id`, `sender_id`, `status`
- **Методы (3)**: `accept()`, `reject()`, `is_pending()`
- **Ассоциации**: Friendship, UserAccount

#### Класс `Friendship`
*Представляет установленную дружбу между двумя пользователями.*
- **Поля (5)**: `closeness_level`, `established_at`, `status`, `user_a_id`, `user_b_id`
- **Методы (3)**: `increase_closeness()`, `terminate()`, `is_confirmed()`
- **Ассоциации**: UserAccount

#### Класс `GroupEvent`
*Представляет встречу или онлайн-вебинар, организованный сообществом.*
- **Поля (6)**: `attendees_count`, `event_date`, `event_id`, `group_id`, `max_attendees`, `title`
- **Методы (3)**: `register_attendee()`, `cancel_attendance()`, `is_full()`
- **Ассоциации**: GroupCapacityExceededException, UserAccount

#### Класс `GroupMembership`
*Определяет участие пользователя в тематическом сообществе.*
- **Поля (5)**: `group_id`, `membership_id`, `role`, `user_id`, `warning_count`
- **Методы (3)**: `warn_member()`, `change_role()`, `is_moderator()`
- **Ассоциации**: InsufficientPrivilegesException, UserAccount

#### Класс `UserGroup`
*Представляет публичное или закрытое сообщество по интересам.*
- **Поля (6)**: `description`, `group_id`, `is_closed`, `is_verified`, `name`, `owner_id`
- **Методы (5)**: `verify_group()`, `close_group()`, `open_group()`, `update_info()`, `has_member()`
- **Ассоциации**: GroupMembership, UserAccount

### Служба модерации, цензура и безопасность (`network/moderation/`)

#### Класс `Appeal`
*Представляет заявление на обжалование блокировки или предупреждения.*
- **Поля (6)**: `appeal_id`, `explanation`, `reviewer_notes`, `sanction_id`, `status`, `user_id`
- **Методы (4)**: `approve()`, `reject()`, `is_under_review()`, `submitted_by()`
- **Ассоциации**: Sanction, UserAccount

#### Класс `AuditLog`
*Фиксирует административные и критические действия в системе.*
- **Поля (5)**: `action`, `actor_id`, `log_id`, `target_id`, `timestamp`
- **Методы (3)**: `format_log_entry()`, `is_action_critical()`, `matches_actor()`
- **Ассоциации**: UserAccount

#### Класс `BannedWordFilter`
*Осуществляет лексический анализ и цензурирование текста.*
- **Поля (4)**: `banned_words_count`, `case_sensitive`, `replacement_symbol`, `strict_mode`
- **Методы (3)**: `contains_banned_word()`, `censor_text()`, `add_keyword()`
- **Ассоциации**: InvalidContentException

#### Класс `ContentFilter`
*Автоматический анализатор контента на спам и нежелательный материал.*
- **Поля (5)**: `auto_block`, `filter_name`, `inspections_count`, `nsfw_detection`, `spam_threshold`
- **Методы (3)**: `evaluate_spam_score()`, `inspect_text()`, `update_threshold()`
- **Ассоциации**: ContentBlockedException

#### Класс `ModerationReport`
*Представляет жалобу пользователя на неприемлемый контент или поведение.*
- **Поля (6)**: `reason`, `report_id`, `reporter_id`, `resolution`, `status`, `target_id`
- **Методы (4)**: `resolve()`, `dismiss()`, `is_pending()`, `reported_by()`
- **Ассоциации**: ReportAlreadyProcessedException, UserAccount

#### Класс `Moderator`
*Сотрудник службы безопасности и модерации контента.*
- **Поля (5)**: `badge_name`, `is_head_moderator`, `moderator_id`, `permissions_level`, `reports_reviewed`
- **Методы (4)**: `review_report()`, `elevate_permissions()`, `can_ban_permanently()`, `assign_badge()`
- **Ассоциации**: InsufficientPrivilegesException, ModerationReport, UserAccount

#### Класс `Sanction`
*Представляет ограничение (бан, мут, предупреждение), наложенное на аккаунт.*
- **Поля (6)**: `duration_days`, `is_revoked`, `reason`, `sanction_id`, `sanction_type`, `user_id`
- **Методы (3)**: `revoke()`, `is_active_sanction()`, `extend_duration()`
- **Ассоциации**: UserAccount

### Экономика платформы, реклама и подписки (`network/monetization/`)

#### Класс `AdCampaign`
*Управляет таргетированной кампанией рекламодателя.*
- **Поля (6)**: `budget_total`, `campaign_id`, `daily_limit`, `is_active`, `spent_amount`, `sponsor_id`
- **Методы (4)**: `charge_budget()`, `pause()`, `resume()`, `is_owned_by()`
- **Ассоциации**: PaymentFailedException, UserAccount

#### Класс `Advertisement`
*Представляет промо-материал, транслируемый в лентах пользователей.*
- **Поля (6)**: `ad_id`, `campaign_id`, `clicks_count`, `impressions_count`, `target_url`, `title`
- **Методы (3)**: `record_impression()`, `record_click()`, `calculate_ctr()`
- **Ассоциации**: AdCampaign

#### Класс `Subscription`
*Управляет активной платной подпиской на автора или сервис.*
- **Поля (6)**: `auto_renew`, `creator_id`, `expires_at`, `subscription_id`, `tier_name`, `user_id`
- **Методы (4)**: `renew()`, `cancel_auto_renew()`, `is_valid()`, `belongs_to_subscriber()`
- **Ассоциации**: SubscriptionExpiredException, SubscriptionTier, UserAccount

#### Класс `SubscriptionTier`
*Описывает тарифный план авторской или платформенной подписки.*
- **Поля (5)**: `badge_icon`, `benefits_count`, `monthly_price`, `name`, `tier_id`
- **Методы (3)**: `is_affordable()`, `add_benefit()`, `format_price_tag()`

#### Класс `Transaction`
*Представляет финансовый перевод между кошельками или оплату услуги.*
- **Поля (6)**: `amount`, `fee`, `receiver_wallet_id`, `sender_wallet_id`, `status`, `tx_id`
- **Методы (4)**: `execute()`, `refund()`, `calculate_fee()`, `validate_amount()`
- **Ассоциации**: PaymentFailedException, Wallet

#### Класс `VirtualGift`
*Представляет подарочный стикер/сувенир, отправляемый в профиль.*
- **Поля (5)**: `gift_id`, `gift_name`, `icon_code`, `is_limited_edition`, `price_coins`
- **Методы (3)**: `send_gift()`, `format_gift_card()`, `apply_discount()`
- **Ассоциации**: UserAccount, Wallet

#### Класс `Wallet`
*Хранит денежный баланс и токены внутренней экономики сети.*
- **Поля (5)**: `balance`, `currency`, `is_frozen`, `user_id`, `wallet_id`
- **Методы (5)**: `deposit()`, `withdraw()`, `freeze()`, `unfreeze()`, `belongs_to_user()`
- **Ассоциации**: PaymentFailedException, UserAccount

### Новостные ленты, рекомендации и метрики (`network/analytics/`)

#### Класс `EngagementMetrics`
*Агрегирует статистику просмотров, репостов, закладок и реакций.*
- **Поля (6)**: `bookmarks`, `comments_count`, `likes`, `post_id`, `shares`, `views`
- **Методы (3)**: `calculate_engagement_rate()`, `record_share()`, `record_bookmark()`
- **Ассоциации**: Post

#### Класс `Feed`
*Формирует и ранжирует новостную ленту для пользователя.*
- **Поля (5)**: `algorithm_type`, `include_ads`, `items_count`, `refresh_interval_sec`, `user_id`
- **Методы (3)**: `add_item()`, `filter_by_algorithm()`, `clear_feed()`
- **Ассоциации**: FeedItem, UserAccount

#### Класс `FeedItem`
*Представляет публикацию внутри ранжированной пользовательской ленты.*
- **Поля (5)**: `item_id`, `post_id`, `relevance_score`, `seen`, `source_type`
- **Методы (4)**: `mark_as_seen()`, `boost_score()`, `penalize_score()`, `matches_post()`
- **Ассоциации**: Post

#### Класс `RecommendationEngine`
*Осуществляет расчет интересов и рекомендацию контента пользователям.*
- **Поля (4)**: `decay_rate`, `diversity_factor`, `min_score_threshold`, `model_version`
- **Методы (3)**: `score_post()`, `recommend_users()`, `update_diversity()`
- **Ассоциации**: Post, UserAccount

#### Класс `TrendAnalyzer`
*Выявляет быстрорастущие тренды и популярные обсуждения.*
- **Поля (4)**: `min_occurrences`, `top_limit`, `velocity_multiplier`, `window_hours`
- **Методы (3)**: `identify_trending_topics()`, `calculate_growth_velocity()`, `adjust_window()`
- **Ассоциации**: Hashtag

#### Класс `UserStatistic`
*Хранит сводную статистику активности пользователя в социальной сети.*
- **Поля (6)**: `active_days`, `comments_written`, `messages_sent`, `posts_published`, `total_reactions_given`, `user_id`
- **Методы (3)**: `increment_posts()`, `increment_comments()`, `record_active_day()`
- **Ассоциации**: UserAccount

### Шлюзы и агрегация уведомлений (`network/notification/`)

#### Класс `Notification`
*Представляет системное уведомление о событиях (лайк, ответ, подписка).*
- **Поля (6)**: `actor_id`, `created_at`, `event_type`, `is_read`, `notification_id`, `recipient_id`
- **Методы (3)**: `mark_as_read()`, `format_message()`, `is_urgent()`
- **Ассоциации**: UserAccount

#### Класс `NotificationBatch`
*Группирует однотипные уведомления для предотвращения спама.*
- **Поля (5)**: `batch_id`, `count`, `event_category`, `is_dispatched`, `recipient_id`
- **Методы (3)**: `aggregate()`, `dispatch()`, `is_empty_batch()`
- **Ассоциации**: Notification, UserAccount

#### Класс `NotificationChannel`
*Описывает транспорт доставки сообщений (Push, Email, SMS, Web).*
- **Поля (5)**: `channel_name`, `delivery_timeout_sec`, `is_enabled`, `priority`, `retry_count`
- **Методы (3)**: `deliver()`, `toggle_channel()`, `adjust_timeout()`
- **Ассоциации**: Notification

### Аутентификация, токены и защита (`network/security/`)

#### Класс `SecurityLog`
*Регистрирует попытки входа, смены паролей и потенциальные угрозы.*
- **Поля (6)**: `event_id`, `event_name`, `ip_address`, `status`, `timestamp`, `user_id`
- **Методы (3)**: `is_suspicious()`, `format_audit_string()`, `flag_failed_attempt()`
- **Ассоциации**: UserAccount

#### Класс `SessionToken`
*Управляет жизненным циклом токена веб-сессии пользователя.*
- **Поля (6)**: `device_info`, `expires_in_hours`, `ip_address`, `is_active`, `token_value`, `user_id`
- **Методы (3)**: `validate()`, `revoke()`, `renew()`
- **Ассоциации**: AuthenticationException, UserAccount

#### Класс `TwoFactorAuth`
*Управляет подтверждением входа через TOTP-коды или резервные ключи.*
- **Поля (5)**: `backup_codes_left`, `is_enabled`, `method`, `secret_hash`, `user_id`
- **Методы (3)**: `verify_otp()`, `enable_2fa()`, `use_backup_code()`
- **Ассоциации**: AuthenticationException, UserAccount

### Системный фасад и поисковые индексы (`network/system/`)

#### Класс `DataBackup`
*Управляет созданием и проверкой целостности бэкапов социальной сети.*
- **Поля (6)**: `backup_id`, `checksum`, `file_path`, `is_encrypted`, `size_mb`, `status`
- **Методы (3)**: `create_snapshot()`, `verify_checksum()`, `mark_corrupted()`

#### Класс `SearchService`
*Обеспечивает полнотекстовый поиск по пользователям, публикациям и тегам.*
- **Поля (5)**: `fuzzy_matching`, `index_name`, `indexed_items_count`, `max_results`, `min_query_length`
- **Методы (3)**: `search_users()`, `search_posts()`, `index_document()`
- **Ассоциации**: Hashtag, Post, UserAccount

#### Класс `SocialNetworkSystem`
*Центральный координатор доменной модели социальной сети.*
- **Поля (7)**: `is_maintenance_mode`, `max_daily_posts`, `network_name`, `posts_count`, `support_email`, `users_count`, `version`
- **Методы (5)**: `register_user()`, `publish_post()`, `enable_maintenance()`, `disable_maintenance()`, `generate_system_report()`
- **Ассоциации**: Post, RateLimitExceededException, UserAccount, UserNotFoundException

