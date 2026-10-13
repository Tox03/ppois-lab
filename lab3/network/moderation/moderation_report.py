# -*- coding: utf-8 -*-
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

    def reported_by(self, user: UserAccount) -> bool:
        """Проверяет заявителя жалобы."""
        return self.reporter_id == user.user_id
