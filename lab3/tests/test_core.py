# -*- coding: utf-8 -*-
"""Модульные тесты для базовых классов ядра (core)."""

import hashlib
import unittest
from lab3.network.core.contact_info import ContactInfo
from lab3.network.core.user_privacy import UserPrivacy
from lab3.network.core.user_settings import UserSettings
from lab3.network.core.user_profile import UserProfile
from lab3.network.core.user_account import UserAccount
from lab3.network.core.user_activity import UserActivity
from lab3.network.core.user_reputation import UserReputation
from lab3.network.exceptions.authentication_exception import AuthenticationException
from lab3.network.exceptions.access_denied_exception import AccessDeniedException
from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class TestCore(unittest.TestCase):
    """Тестирование классов подсистемы core."""

    def test_contact_info(self):
        contact = ContactInfo("+79991234567", "Москва", "Россия", "@alex")
        self.assertEqual(contact.format_location(), "Москва, Россия")
        self.assertTrue(contact.confirm_phone("123456"))
        self.assertTrue(contact.is_phone_confirmed)
        contact.update_phone("+79998887766")
        self.assertEqual(contact.phone, "+79998887766")
        self.assertFalse(contact.is_phone_confirmed)
        with self.assertRaises(InvalidContentException):
            contact.update_phone("invalid")

    def test_user_privacy(self):
        privacy = UserPrivacy()
        self.assertEqual(privacy.profile_visibility, "public")
        privacy.set_visibility("friends_only")
        self.assertEqual(privacy.profile_visibility, "friends_only")
        with self.assertRaises(AccessDeniedException):
            privacy.set_visibility("invalid_level")
        self.assertTrue(privacy.can_receive_message_from(True))
        privacy.allow_messages_from_strangers = False
        self.assertFalse(privacy.can_receive_message_from(False))
        self.assertTrue(privacy.can_receive_message_from(True))
        status = privacy.toggle_online_status()
        self.assertFalse(status)

    def test_user_settings(self):
        settings = UserSettings()
        self.assertEqual(settings.theme, "dark")
        settings.switch_theme("light")
        self.assertEqual(settings.theme, "light")
        p = settings.toggle_push()
        self.assertFalse(p)
        settings.change_language("en")
        self.assertEqual(settings.language, "en")

    def test_user_profile(self):
        profile = UserProfile("Обо мне", "https://example.com", "1995-05-10")
        privacy = UserPrivacy()
        profile.update_bio("Новая биография", privacy)
        self.assertEqual(profile.bio, "Новая биография")
        self.assertTrue(profile.verify_profile(True))
        self.assertTrue(profile.is_verified)
        profile.unverify_profile()
        self.assertFalse(profile.is_verified)
        profile.verify_profile(True)
        contact = ContactInfo(city="Минск", country="Беларусь")
        card = profile.format_profile_card(contact)
        self.assertIn("Минск, Беларусь", card)
        self.assertIn("[✓]", card)

    def test_user_account(self):
        pwd_hash = hashlib.sha256("secret123".encode("utf-8")).hexdigest()
        acc = UserAccount("usr_1", "john_doe", pwd_hash, "john@example.com")
        self.assertTrue(acc.verify_password("secret123"))
        with self.assertRaises(AuthenticationException):
            acc.verify_password("wrong_password")
        acc.change_password("secret123", "new_secret_pwd")
        self.assertTrue(acc.verify_password("new_secret_pwd"))
        acc.deactivate()
        self.assertFalse(acc.is_active)
        acc.activate()
        self.assertTrue(acc.is_active)

    def test_user_activity(self):
        activity = UserActivity()
        acc = UserAccount("usr_2", "jane", "hash", "jane@example.com")
        activity.record_login(acc, "2026-05-01 10:00")
        self.assertEqual(activity.total_sessions, 1)
        self.assertTrue(activity.is_online)
        activity.set_status("Работаю над кодом")
        self.assertEqual(activity.current_status, "Работаю над кодом")
        activity.go_offline()
        self.assertFalse(activity.is_online)
        activity.go_online()
        self.assertTrue(activity.is_online)

    def test_user_reputation(self):
        rep = UserReputation()
        acc = UserAccount("usr_3", "bob", "hash", "bob@example.com")
        rep.add_karma(50, acc)
        self.assertEqual(rep.karma_points, 50)
        rep.deduct_karma(20)
        self.assertEqual(rep.karma_points, 30)
        rep.issue_warning()
        self.assertEqual(rep.warnings_count, 1)
        self.assertEqual(rep.calculate_trust_rank(), "neutral")


if __name__ == "__main__":
    unittest.main()
