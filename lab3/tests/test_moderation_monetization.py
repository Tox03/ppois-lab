# -*- coding: utf-8 -*-
"""Модульные тесты для подсистем moderation и monetization."""

import unittest
from lab3.network.core.user_account import UserAccount
from lab3.network.moderation.moderation_report import ModerationReport
from lab3.network.moderation.moderator import Moderator
from lab3.network.moderation.banned_word_filter import BannedWordFilter
from lab3.network.moderation.audit_log import AuditLog
from lab3.network.moderation.sanction import Sanction
from lab3.network.moderation.content_filter import ContentFilter
from lab3.network.moderation.appeal import Appeal
from lab3.network.monetization.subscription_tier import SubscriptionTier
from lab3.network.monetization.subscription import Subscription
from lab3.network.monetization.ad_campaign import AdCampaign
from lab3.network.monetization.advertisement import Advertisement
from lab3.network.monetization.wallet import Wallet
from lab3.network.monetization.transaction import Transaction
from lab3.network.monetization.virtual_gift import VirtualGift
from lab3.network.exceptions.payment_failed_exception import PaymentFailedException
from lab3.network.exceptions.subscription_expired_exception import SubscriptionExpiredException
from lab3.network.exceptions.content_blocked_exception import ContentBlockedException
from lab3.network.exceptions.report_already_processed_exception import ReportAlreadyProcessedException


class TestModerationAndMonetization(unittest.TestCase):
    """Тестирование модерации и монетизации."""

    def setUp(self):
        self.user = UserAccount("u1", "charlie", "hash", "charlie@site.com")
        self.recipient = UserAccount("u2", "david", "hash", "david@site.com")

    def test_moderation_workflow(self):
        report = ModerationReport("rep_1", "u1", "u2", "оскорбления")
        self.assertTrue(report.is_pending())
        moderator = Moderator("mod_1", is_head_moderator=True, permissions_level=3)
        self.assertTrue(moderator.can_ban_permanently())
        moderator.elevate_permissions(4)
        self.assertEqual(moderator.permissions_level, 4)
        moderator.review_report(report, "вынесено предупреждение")
        self.assertFalse(report.is_pending())
        with self.assertRaises(ReportAlreadyProcessedException):
            report.resolve("повторное решение")

        dismiss_rep = ModerationReport("rep_dismiss", "u1", "u2")
        dismiss_rep.dismiss()
        self.assertEqual(dismiss_rep.status, "dismissed")

    def test_banned_words_and_content_filter(self):
        word_filter = BannedWordFilter()
        words = ["казино", "рулетка"]
        self.assertTrue(word_filter.contains_banned_word("Привет, онлайн казино здесь", words))
        censored = word_filter.censor_text("Играй в казино", words)
        self.assertIn("******", censored)
        count = word_filter.add_keyword("покер")
        self.assertEqual(count, 1)

        cf = ContentFilter(spam_threshold=0.5)
        cf.update_threshold(0.7)
        self.assertEqual(cf.spam_threshold, 0.7)
        with self.assertRaises(ContentBlockedException):
            cf.inspect_text("скидка на крипта казино тут и казино", "post_bad")

    def test_sanctions_and_appeal(self):
        sanction = Sanction("sanc_1", "u1", "mute", 3, "спам")
        self.assertTrue(sanction.is_active_sanction(self.user))
        sanction.extend_duration(2)
        self.assertEqual(sanction.duration_days, 5)

        appeal = Appeal("app_1", "sanc_1", "u1", "Это была ошибка")
        self.assertTrue(appeal.is_under_review())
        appeal.approve(sanction, "Амнистия")
        self.assertFalse(sanction.is_active_sanction(self.user))

        appeal_rej = Appeal("app_2", "sanc_2", "u1", "Разбаньте")
        appeal_rej.reject("Отказано")
        self.assertEqual(appeal_rej.status, "rejected")

    def test_audit_log(self):
        log = AuditLog("log_1", "ban_user", "mod_1", "u1")
        self.assertTrue(log.is_action_critical())
        self.assertIn("ban_user", log.format_log_entry())
        self.assertFalse(log.matches_actor(self.user))

    def test_wallet_and_transactions(self):
        w1 = Wallet("w1", "u1", 500.0)
        w2 = Wallet("w2", "u2", 100.0)
        w1.deposit(200.0)
        self.assertEqual(w1.balance, 700.0)
        w1.withdraw(100.0)
        self.assertEqual(w1.balance, 600.0)
        w1.freeze()
        self.assertTrue(w1.is_frozen)
        with self.assertRaises(PaymentFailedException):
            w1.withdraw(50.0)
        w1.unfreeze()
        self.assertFalse(w1.is_frozen)

        tx = Transaction("tx_1", "w1", "w2", 200.0)
        tx.calculate_fee(2.0)
        self.assertEqual(tx.fee, 4.0)
        tx.execute(w1, w2)
        self.assertEqual(w1.balance, 396.0)
        self.assertEqual(w2.balance, 300.0)
        tx.refund(w1, w2)
        self.assertEqual(tx.status, "refunded")
        self.assertEqual(w1.balance, 596.0)
        self.assertEqual(w2.balance, 100.0)

        with self.assertRaises(PaymentFailedException):
            w1.withdraw(1000.0)

    def test_subscriptions_and_gifts(self):
        tier = SubscriptionTier("tier_1", "VIP", 299.0)
        self.assertTrue(tier.is_affordable(500.0))
        tier.add_benefit()
        self.assertIn("299.0", tier.format_price_tag())

        sub = Subscription("sub_1", "u1", "u2", "VIP", "2026-12-31")
        self.assertTrue(sub.is_valid("2026-06-01"))
        sub.renew(tier, "2027-06-01")
        self.assertEqual(sub.expires_at, "2027-06-01")
        sub.cancel_auto_renew()
        self.assertFalse(sub.auto_renew)
        with self.assertRaises(SubscriptionExpiredException):
            sub.is_valid("2028-01-01")

        gift = VirtualGift("gift_1", "Торт", price_coins=50)
        sender_wallet = Wallet("w_gift", "u1", 100.0)
        self.assertTrue(gift.send_gift(sender_wallet, self.recipient))
        self.assertEqual(sender_wallet.balance, 50.0)
        gift.apply_discount(20)
        self.assertEqual(gift.price_coins, 40)

    def test_ads(self):
        campaign = AdCampaign("camp_1", "u1", 100.0)
        campaign.pause()
        self.assertFalse(campaign.is_active)
        campaign.resume()
        self.assertTrue(campaign.is_active)

        ad = Advertisement("ad_1", "camp_1", "Курсы Python", "https://course.org")
        ad.record_impression(campaign)
        ad.record_click(campaign)
        self.assertGreater(ad.calculate_ctr(), 0.0)
        self.assertGreater(campaign.spent_amount, 0.0)


if __name__ == "__main__":
    unittest.main()
