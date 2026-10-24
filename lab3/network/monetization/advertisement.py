# -*- coding: utf-8 -*-
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
