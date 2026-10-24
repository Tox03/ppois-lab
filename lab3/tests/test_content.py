# -*- coding: utf-8 -*-
"""Модульные тесты для классов подсистемы content."""

import unittest
from lab3.network.core.user_account import UserAccount
from lab3.network.content.post import Post
from lab3.network.content.text_post import TextPost
from lab3.network.content.media_post import MediaPost
from lab3.network.content.poll_post import PollPost
from lab3.network.content.poll_option import PollOption
from lab3.network.content.comment import Comment
from lab3.network.content.reaction import Reaction
from lab3.network.content.hashtag import Hashtag
from lab3.network.content.media_attachment import MediaAttachment
from lab3.network.content.album import Album
from lab3.network.content.story import Story
from lab3.network.content.story_viewer import StoryViewer
from lab3.network.exceptions.invalid_content_exception import InvalidContentException
from lab3.network.exceptions.content_blocked_exception import ContentBlockedException


class TestContent(unittest.TestCase):
    """Тестирование классов подсистемы content."""

    def setUp(self):
        self.user = UserAccount("usr_1", "alex", "hash", "alex@mail.com")
        self.other_user = UserAccount("usr_2", "ivan", "hash", "ivan@mail.com")

    def test_post_lifecycle(self):
        post = Post("p_1", "usr_1", "Привет, мир!")
        self.assertTrue(post.pin(self.user))
        self.assertTrue(post.is_pinned)
        post.unpin()
        self.assertFalse(post.is_pinned)
        post.edit_content("Обновленный текст", self.user)
        self.assertEqual(post.text_content, "Обновленный текст")
        with self.assertRaises(InvalidContentException):
            post.edit_content("Хакер", self.other_user)
        post.soft_delete()
        self.assertTrue(post.is_deleted)
        post.restore()
        self.assertFalse(post.is_deleted)
        post.soft_delete()
        with self.assertRaises(ContentBlockedException):
            post.edit_content("Нельзя редактировать", self.user)

    def test_text_post(self):
        post = Post("p_2", "usr_1", "Это длинный пост о технологиях и искусственном интеллекте.")
        tp = TextPost("p_2")
        minutes = tp.calculate_reading_time(post)
        self.assertGreaterEqual(minutes, 1)
        summary = tp.generate_summary(post)
        self.assertTrue(len(summary) > 0)
        tp.apply_styling("monospace", "#000000")
        self.assertEqual(tp.font_style, "monospace")

    def test_media_and_attachments(self):
        att = MediaAttachment("att_1", "https://cdn.site/pic.jpg", 1024 * 500, "image/jpeg", 1920, 1080)
        self.assertTrue(att.is_image())
        self.assertFalse(att.is_video())
        self.assertIn("КБ", att.format_file_size())

        post = Post("p_3", "usr_1", "Фотоотчет")
        mp = MediaPost("p_3")
        count = mp.add_media_item(att)
        self.assertEqual(count, 1)
        mp.apply_filter("sepia")
        self.assertEqual(mp.filter_preset, "sepia")
        self.assertTrue(mp.verify_attachments(post))

    def test_polls(self):
        opt1 = PollOption("opt_1", "Да")
        opt2 = PollOption("opt_2", "Нет")
        poll = PollPost("p_4", "Вы любите Python?")
        poll.add_vote(opt1)
        poll.add_vote(opt1)
        poll.add_vote(opt2)
        self.assertEqual(poll.total_votes, 3)
        poll.calculate_results([opt1, opt2])
        self.assertAlmostEqual(opt1.percentage, 66.7, delta=0.5)
        self.assertAlmostEqual(opt2.percentage, 33.3, delta=0.5)
        poll.close_poll()
        self.assertTrue(poll.is_closed)
        poll.reopen_poll()
        self.assertFalse(poll.is_closed)
        poll.close_poll()
        with self.assertRaises(InvalidContentException):
            poll.add_vote(opt1)

    def test_comment_and_reaction(self):
        reaction = Reaction("like", "usr_2", "c_1")
        self.assertTrue(reaction.is_positive())
        self.assertEqual(reaction.get_emoji(), "👍")
        reaction.update_type("love", self.other_user)
        self.assertEqual(reaction.reaction_type, "love")

        comment = Comment("c_1", "p_1", "usr_2", "Отличный пост!")
        likes = comment.like(reaction)
        self.assertEqual(likes, 1)
        comment.edit_text("Исправленный комментарий", self.other_user)
        self.assertEqual(comment.text, "Исправленный комментарий")
        comment.hide()
        self.assertTrue(comment.is_hidden)
        comment.unhide()
        self.assertFalse(comment.is_hidden)

    def test_album_and_stories(self):
        album = Album("alb_1", "usr_1", "Отпуск")
        att = MediaAttachment("att_2", "https://cdn/pic2.jpg", 2048, "image/png")
        photos = album.add_photo(att, self.user)
        self.assertEqual(photos, 1)
        album.toggle_privacy()
        self.assertTrue(album.is_private)

        story = Story("st_1", "usr_1", "https://cdn/story.mp4")
        story.record_view(self.other_user)
        self.assertEqual(story.views_count, 1)
        self.assertTrue(story.check_expiration(25))
        self.assertTrue(story.is_expired)

        viewer = StoryViewer("usr_2", "st_1")
        viewer.mark_reaction(self.other_user)
        self.assertTrue(viewer.has_reacted)

    def test_hashtag(self):
        tag = Hashtag("#python")
        self.assertEqual(tag.tag_name, "python")
        tag.increment_usage()
        self.assertEqual(tag.usage_count, 2)
        score = tag.update_trend_score(10)
        self.assertGreater(score, 0)
        self.assertTrue(tag.validate_tag())


if __name__ == "__main__":
    unittest.main()
