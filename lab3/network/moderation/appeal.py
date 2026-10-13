# -*- coding: utf-8 -*-
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

    def submitted_by(self, user: UserAccount) -> bool:
        """Проверяет авторство апелляционного заявления."""
        return self.user_id == user.user_id
