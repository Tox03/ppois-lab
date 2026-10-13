# -*- coding: utf-8 -*-
"""Модульные тесты для подсистем analytics, notification, security и system."""

import unittest
from lab3.network.core.user_account import UserAccount
from lab3.network.content.post import Post
from lab3.network.content.hashtag import Hashtag
from lab3.network.analytics.feed import Feed
from lab3.network.analytics.feed_item import FeedItem
from lab3.network.analytics.recommendation_engine import RecommendationEngine
from lab3.network.analytics.engagement_metrics import EngagementMetrics
from lab3.network.analytics.user_statistic import UserStatistic
from lab3.network.analytics.trend_analyzer import TrendAnalyzer
from lab3.network.notification.notification import Notification
from lab3.network.notification.notification_channel import NotificationChannel
from lab3.network.notification.notification_batch import NotificationBatch
from lab3.network.security.session_token import SessionToken
from lab3.network.security.two_factor_auth import TwoFactorAuth
from lab3.network.security.security_log import SecurityLog
from lab3.network.system.data_backup import DataBackup
from lab3.network.system.search_service import SearchService
from lab3.network.system.social_network_system import SocialNetworkSystem
from lab3.network.exceptions.authentication_exception import AuthenticationException
from lab3.network.exceptions.user_not_found_exception import UserNotFoundException


class TestAnalyticsSecuritySystem(unittest.TestCase):
    """Тестирование аналитики, уведомлений, безопасности и ядра системы."""

    def setUp(self):
        self.user = UserAccount("u1", "eva", "hash", "eva@network.com")
        self.user2 = UserAccount("u2", "frank", "hash", "frank@network.com")
        self.post = Post("p_1", "u1", "Интересная статья про алгоритмы")

    def test_feed_and_recommendations(self):
        feed = Feed("u1")
        item = FeedItem("item_1", "p_1", 1.5)
        feed.add_item(item)
        self.assertEqual(feed.items_count, 1)
        item.mark_as_seen()
        self.assertTrue(item.seen)
        boosted = item.boost_score(1.2)
        self.assertGreater(boosted, 1.5)
        penalized = item.penalize_score(0.5)
        self.assertLess(penalized, boosted)
        feed_status = feed.filter_by_algorithm(self.user)
        self.assertIn("обновлена", feed_status)
        other_status = feed.filter_by_algorithm(self.user2)
        self.assertEqual(other_status, "Чужая лента")
        feed.clear_feed()
        self.assertEqual(feed.items_count, 0)

        engine = RecommendationEngine()
        score = engine.score_post(self.post, self.user)
        self.assertGreater(score, 0)
        recs = engine.recommend_users(self.user, [self.user, self.user2])
        self.assertEqual(len(recs), 1)
        engine.update_diversity(0.8)
        self.assertEqual(engine.diversity_factor, 0.8)

    def test_engagement_and_stats(self):
        eng = EngagementMetrics("p_1", views=100, likes=20, shares=5, comments_count=5)
        self.assertEqual(eng.calculate_engagement_rate(), 30.0)
        eng.record_share(self.post)
        self.assertEqual(eng.shares, 6)
        eng.record_bookmark()
        self.assertEqual(eng.bookmarks, 1)
        zero_eng = EngagementMetrics("p_zero", views=0)
        self.assertEqual(zero_eng.calculate_engagement_rate(), 0.0)

        stats = UserStatistic("u1")
        self.assertEqual(stats.increment_posts(self.user), 1)
        self.assertEqual(stats.increment_comments(), 1)
        self.assertEqual(stats.record_active_day(), 1)

        analyzer = TrendAnalyzer(min_occurrences=2)
        tag = Hashtag("ai", usage_count=5)
        trending = analyzer.identify_trending_topics([tag])
        self.assertIn("ai", trending)
        vel = analyzer.calculate_growth_velocity(100, 50)
        self.assertGreater(vel, 0)
        analyzer.adjust_window(48)
        self.assertEqual(analyzer.window_hours, 48)

    def test_notifications(self):
        notif = Notification("n_1", "u1", "u2", "like")
        self.assertIn("оценил", notif.format_message())
        self.assertTrue(notif.mark_as_read(self.user))
        self.assertFalse(notif.mark_as_read(self.user2))
        self.assertFalse(notif.is_urgent())
        sec_notif = Notification("n_2", "u1", "u2", "security_alert")
        self.assertTrue(sec_notif.is_urgent())

        channel = NotificationChannel("push")
        self.assertTrue(channel.deliver(notif))
        channel.toggle_channel()
        self.assertFalse(channel.deliver(notif))
        channel.adjust_timeout(10)
        self.assertEqual(channel.delivery_timeout_sec, 10)

        batch = NotificationBatch("b_1", "u1")
        self.assertTrue(batch.is_empty_batch())
        batch.aggregate(notif)
        self.assertEqual(batch.count, 1)
        self.assertFalse(batch.is_empty_batch())
        msg = batch.dispatch(self.user)
        self.assertIn("1 новых событий", msg)
        err_msg = batch.dispatch(self.user2)
        self.assertEqual(err_msg, "Ошибка адресата")

    def test_security_subsystem(self):
        token = SessionToken("tok_123", "u1", "127.0.0.1")
        self.assertTrue(token.validate(self.user))
        token.renew(5)
        self.assertGreaterEqual(token.expires_in_hours, 29)
        token.revoke()
        with self.assertRaises(AuthenticationException):
            token.validate(self.user)

        two_fa = TwoFactorAuth("u1", is_enabled=False)
        self.assertTrue(two_fa.verify_otp("123"))
        two_fa.enable_2fa(self.user)
        self.assertTrue(two_fa.is_enabled)
        self.assertTrue(two_fa.verify_otp("123456"))
        with self.assertRaises(AuthenticationException):
            two_fa.verify_otp("bad")
        left = two_fa.use_backup_code()
        self.assertEqual(left, 9)

        sec_log = SecurityLog("sl_1", "u1", "192.168.1.1", "brute_force_detected")
        self.assertTrue(sec_log.is_suspicious())
        audit_s = sec_log.format_audit_string()
        self.assertIn("192.168.1.1", audit_s)
        sec_log.flag_failed_attempt(self.user2)
        self.assertEqual(sec_log.event_name, "login_failed")

    def test_system_and_search(self):
        sys = SocialNetworkSystem("MegaSocial")
        inactive_user = UserAccount("u_dead", "ghost", "hash", "ghost@site.com", is_active=False)
        with self.assertRaises(UserNotFoundException):
            sys.register_user(inactive_user)
        sys.register_user(self.user)
        self.assertEqual(sys.users_count, 1)
        sys.publish_post(self.post)
        self.assertEqual(sys.posts_count, 1)
        sys.enable_maintenance()
        self.assertTrue(sys.is_maintenance_mode)
        sys.disable_maintenance()
        self.assertFalse(sys.is_maintenance_mode)
        rep = sys.generate_system_report()
        self.assertIn("MegaSocial", rep)

        search = SearchService()
        found_users = search.search_users("eva", [self.user, self.user2])
        self.assertEqual(len(found_users), 1)
        self.assertEqual(len(search.search_users("e", [self.user])), 0)
        found_posts = search.search_posts("алгоритмы", [self.post])
        self.assertEqual(len(found_posts), 1)
        self.assertEqual(len(search.search_posts("а", [self.post])), 0)
        idx_count = search.index_document(Hashtag("dev"))
        self.assertEqual(idx_count, 1)

        backup = DataBackup("bak_1", "/backups/db.snap")
        status = backup.create_snapshot(120.5)
        self.assertEqual(status, "completed")
        self.assertTrue(backup.verify_checksum("sha256_mock_sum"))
        backup.mark_corrupted()
        self.assertEqual(backup.status, "corrupted")


if __name__ == "__main__":
    unittest.main()
