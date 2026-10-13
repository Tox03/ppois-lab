# -*- coding: utf-8 -*-
"""Модульные тесты для подсистем communication и relations."""

import unittest
from lab3.network.core.user_account import UserAccount
from lab3.network.communication.chat import Chat
from lab3.network.communication.direct_message import DirectMessage
from lab3.network.communication.chat_message import ChatMessage
from lab3.network.communication.group_chat import GroupChat
from lab3.network.communication.chat_member import ChatMember
from lab3.network.communication.call_session import CallSession
from lab3.network.communication.audio_message import AudioMessage
from lab3.network.relations.friendship import Friendship
from lab3.network.relations.follow import Follow
from lab3.network.relations.block_record import BlockRecord
from lab3.network.relations.friend_request import FriendRequest
from lab3.network.relations.user_group import UserGroup
from lab3.network.relations.group_membership import GroupMembership
from lab3.network.relations.group_event import GroupEvent
from lab3.network.exceptions.access_denied_exception import AccessDeniedException
from lab3.network.exceptions.group_capacity_exceeded_exception import GroupCapacityExceededException


class TestCommunicationAndRelations(unittest.TestCase):
    """Тестирование коммуникаций и социальных связей."""

    def setUp(self):
        self.user1 = UserAccount("u1", "alice", "hash1", "alice@test.com")
        self.user2 = UserAccount("u2", "bob", "hash2", "bob@test.com")

    def test_direct_message(self):
        msg = DirectMessage("m1", "u1", "u2", "Привет, Боб!")
        self.assertEqual(msg.format_preview(), "[Нов.] Привет, Боб!")
        msg.mark_as_delivered()
        self.assertTrue(msg.is_delivered)
        msg.mark_as_read(self.user2)
        self.assertTrue(msg.is_read)
        with self.assertRaises(AccessDeniedException):
            msg.mark_as_read(self.user1)

    def test_group_chat_and_members(self):
        chat = Chat("c1")
        chat.update_last_activity("2026-05-01 12:00")
        self.assertEqual(chat.messages_count, 1)
        chat.unarchive()
        chat.archive()
        self.assertTrue(chat.is_archived)

        group = GroupChat("c1", "Разработчики", "u1", members_limit=2)
        member = ChatMember("u2", "c1")
        self.assertTrue(group.add_participant(member, 1))
        with self.assertRaises(GroupCapacityExceededException):
            group.add_participant(member, 2)
        member.promote_to_admin(self.user1)
        self.assertEqual(member.role, "admin")
        member.demote()
        self.assertEqual(member.role, "member")
        group.remove_participant(member)
        self.assertEqual(member.role, "banned")
        group.mute()
        self.assertTrue(group.is_muted)
        invite = group.generate_invite(chat)
        self.assertIn("invite_c1", invite)

        c_msg = ChatMessage("cmsg_1", "c1", "u1", "Всем привет!")
        self.assertTrue(c_msg.pin(chat))
        self.assertTrue(c_msg.is_pinned)
        c_msg.unpin()
        self.assertFalse(c_msg.is_pinned)
        other_chat = Chat("c2")
        self.assertFalse(c_msg.pin(other_chat))
        c_msg.set_reply("cmsg_0", self.user1)
        self.assertEqual(c_msg.reply_to_id, "cmsg_0")
        c_msg.set_reply("cmsg_99", self.user2)
        self.assertEqual(c_msg.reply_to_id, "cmsg_0")

    def test_call_and_audio(self):
        call = CallSession("call_1", "u1", is_video=True)
        self.assertTrue(call.start_call(self.user2))
        self.assertEqual(call.status, "connected")
        duration = call.end_call(125)
        self.assertEqual(duration, 125)
        self.assertEqual(call.rate_quality(4.5), 4.5)

        audio = AudioMessage("aud_1", 130, "https://cdn/audio.ogg")
        self.assertTrue(audio.is_long_audio())
        self.assertEqual(audio.format_duration(), "02:10")
        audio.transcribe("Привет, перезвони мне")
        self.assertEqual(audio.transcription, "Привет, перезвони мне")

    def test_friendship_and_request(self):
        req = FriendRequest("req_1", "u1", "u2", "Будем друзьями?")
        self.assertTrue(req.is_pending())
        friendship = req.accept(self.user2)
        self.assertIsInstance(friendship, Friendship)
        self.assertTrue(friendship.is_confirmed())
        friendship.increase_closeness()
        self.assertEqual(friendship.closeness_level, 2)
        friendship.terminate(self.user1)
        self.assertFalse(friendship.is_confirmed())

    def test_follow_and_block(self):
        fol = Follow("u1", "u2")
        self.assertTrue(fol.notifications_enabled)
        fol.toggle_notifications()
        self.assertFalse(fol.notifications_enabled)
        self.assertTrue(fol.unfollow(self.user1))

        block = BlockRecord("u1", "u2", "Спам в ЛС")
        self.assertTrue(block.matches_pair("u1", "u2"))
        self.assertIn("Спам в ЛС", block.format_block_notice())
        block.deactivate(self.user1)
        self.assertFalse(block.is_active)

    def test_user_group_and_events(self):
        group = UserGroup("grp_1", "Python Devs", "Сообщество питонистов", "u1")
        group.verify_group()
        self.assertTrue(group.is_verified)
        self.assertTrue(group.close_group(self.user1))

        membership = GroupMembership("mem_1", "grp_1", "u2")
        membership.warn_member()
        self.assertEqual(membership.warning_count, 1)
        membership.change_role("moderator", self.user1)
        self.assertTrue(membership.is_moderator())

        event = GroupEvent("ev_1", "grp_1", "Митап", max_attendees=1)
        event.register_attendee(self.user2)
        self.assertTrue(event.is_full())
        with self.assertRaises(GroupCapacityExceededException):
            event.register_attendee(self.user1)


if __name__ == "__main__":
    unittest.main()
