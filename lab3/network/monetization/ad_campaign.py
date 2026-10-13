# -*- coding: utf-8 -*-
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

    def is_owned_by(self, sponsor: UserAccount) -> bool:
        """Проверяет принадлежность кампании рекламодателю."""
        return self.sponsor_id == sponsor.user_id
