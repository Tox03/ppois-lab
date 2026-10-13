# -*- coding: utf-8 -*-
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
