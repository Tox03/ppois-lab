# -*- coding: utf-8 -*-
"""Интерактивный консольный интерфейс (CLI) платформы социальной сети."""

import hashlib
from typing import Optional, Iterator

from lab3.network.system.social_network_system import SocialNetworkSystem
from lab3.network.core.user_account import UserAccount
from lab3.network.content.post import Post
from lab3.network.content.comment import Comment
from lab3.network.content.reaction import Reaction
from lab3.network.content.poll_post import PollPost
from lab3.network.content.poll_option import PollOption
from lab3.network.communication.chat import Chat
from lab3.network.communication.group_chat import GroupChat
from lab3.network.communication.direct_message import DirectMessage
from lab3.network.relations.friend_request import FriendRequest
from lab3.network.relations.friendship import Friendship
from lab3.network.relations.block_record import BlockRecord
from lab3.network.moderation.banned_word_filter import BannedWordFilter
from lab3.network.moderation.content_filter import ContentFilter
from lab3.network.moderation.moderation_report import ModerationReport
from lab3.network.moderation.moderator import Moderator
from lab3.network.moderation.sanction import Sanction
from lab3.network.monetization.wallet import Wallet
from lab3.network.monetization.transaction import Transaction
from lab3.network.monetization.virtual_gift import VirtualGift
from lab3.network.analytics.engagement_metrics import EngagementMetrics
from lab3.network.system.search_service import SearchService


class NetworkCli:
    """Консольный интерфейс для управления и демонстрации возможностей социальной сети."""

    def __init__(self) -> None:
        """Инициализация демонстрационного стенда социальной сети."""
        self._input_gen: Optional[Iterator[str]] = None
        self.system = SocialNetworkSystem("CosmoNet", version="3.0.0")
        self.users = {}
        self.posts = []
        self.wallets = {}
        self.banned_filter = BannedWordFilter()
        self.search = SearchService()
        self.active_chat = Chat("chat_01", "Диалог разработки")
        self.group_chat = GroupChat("gchat_01", "Разработчики CosmoNet", "usr_101")
        self.active_friendship: Optional[Friendship] = None
        self.active_block: Optional[BlockRecord] = None
        self.active_poll: Optional[PollPost] = None
        self._setup_demo_data()

    def _setup_demo_data(self) -> None:
        """Наполняет систему демонстрационными аккаунтами и записями."""
        pwd1 = hashlib.sha256("password123".encode("utf-8")).hexdigest()
        pwd2 = hashlib.sha256("password456".encode("utf-8")).hexdigest()

        alex = UserAccount("usr_101", "alex_dev", pwd1, "alex@cosmonet.ru")
        elena = UserAccount("usr_102", "elena_art", pwd2, "elena@cosmonet.ru")

        self.system.register_user(alex)
        self.system.register_user(elena)
        self.users["alex_dev"] = alex
        self.users["elena_art"] = elena

        self.wallets["alex_dev"] = Wallet("w_alex", "usr_101", 1500.0)
        self.wallets["elena_art"] = Wallet("w_elena", "usr_102", 500.0)

        demo_post = Post("p_101", alex.user_id, "Всем привет! Наша новая социальная сеть запущена!")
        self.system.publish_post(demo_post)
        self.posts.append(demo_post)

    def print_menu(self) -> None:
        """Выводит главное меню возможностей социальной сети с парными операциями."""
        print("\n" + "=" * 65)
        print("      СОЦИАЛЬНАЯ СЕТЬ CosmoNet — СИММЕТРИЧНОЕ УПРАВЛЕНИЕ")
        print("=" * 65)
        print("1.  Система: статус и техработы (включение / отключение)")
        print("2.  Пользователи: список, деактивация и активация аккаунта")
        print("3.  Публикации: публикация, удаление и восстановление поста")
        print("4.  Опросы: создание голосования, закрытие и возобновление")
        print("5.  Чаты: архив / разархив диалога, отключение / включение звука")
        print("6.  Дружба: принятие заявки и расторжение дружбы")
        print("7.  Черный список: блокировка и снятие блокировки пользователя")
        print("8.  Кошельки: пополнение, перевод, заморозка и разморозка")
        print("9.  Модерация: добавление / удаление стоп-слов, санкции и отзыв")
        print("10. Аналитика вовлеченности и полнотекстовый поиск")
        print("0.  Выход")
        print("=" * 65)

    def show_system_report(self) -> None:
        """Демонстрирует системный отчет и переключает режим техработ."""
        print(f"\n[СИСТЕМА ДО]: {self.system.generate_system_report()}")
        if self.system.is_maintenance_mode:
            self.system.disable_maintenance()
            print("[РЕЖИМ]: Техническое обслуживание ОТКЛЮЧЕНО (платформа в сети)")
        else:
            self.system.enable_maintenance()
            print("[РЕЖИМ]: Техническое обслуживание ВКЛЮЧЕНО (сервис на профилактике)")
        print(f"[СИСТЕМА ПОСЛЕ]: {self.system.generate_system_report()}")

    def manage_users(self) -> None:
        """Демонстрирует просмотр пользователей, деактивацию и повторную активацию."""
        user = self.users["elena_art"]
        print("\n[СПИСОК ПОЛЬЗОВАТЕЛЕЙ]:")
        for username, acc in self.users.items():
            st = "Активен" if acc.is_active else "Отключен"
            print(f"- @{username} (ID: {acc.user_id}, Статус: {st})")
        user.deactivate()
        print(f"[ОТКЛЮЧЕНИЕ]: Аккаунт @{user.username} успешно деактивирован (is_active={user.is_active})")
        user.activate()
        print(f"[ВКЛЮЧЕНИЕ]: Аккаунт @{user.username} успешно повторно активирован (is_active={user.is_active})")

    def manage_posts(self) -> None:
        """Демонстрирует создание, удаление и восстановление публикации."""
        author = self.users["alex_dev"]
        post_id = f"p_{len(self.posts) + 101}"
        new_post = Post(post_id, author.user_id, "Архитектура ООП проекта полностью готова!")
        self.system.publish_post(new_post)
        self.posts.append(new_post)
        print(f"\n[ДОБАВЛЕНИЕ]: Создан пост #{new_post.post_id}: '{new_post.text_content}'")

        new_post.soft_delete()
        print(f"[УДАЛЕНИЕ]: Пост #{new_post.post_id} помечен удаленным (is_deleted={new_post.is_deleted})")
        new_post.restore()
        print(f"[ВОССТАНОВЛЕНИЕ]: Пост #{new_post.post_id} успешно восстановлен (is_deleted={new_post.is_deleted})")

        react = Reaction("like", self.users["elena_art"].user_id, new_post.post_id)
        comment = Comment(f"c_{len(self.posts)}", new_post.post_id, self.users["elena_art"].user_id, "Отличная новость!")
        comment.like(react)
        print(f"[КОММЕНТАРИЙ]: @elena_art: '{comment.text}' (лайков: {comment.likes_count})")

    def manage_polls(self) -> None:
        """Демонстрирует создание, закрытие и повторное открытие опроса."""
        poll = PollPost("poll_101", "Какой язык программирования лучше для ООП?")
        self.active_poll = poll
        opt_py = PollOption("opt_1", "Python")
        opt_cpp = PollOption("opt_2", "C++")
        poll.add_vote(opt_py)
        poll.add_vote(opt_py)
        poll.add_vote(opt_cpp)
        poll.calculate_results([opt_py, opt_cpp])
        print(f"\n[ОПРОС СОЗДАН]: {poll.question} (Всего голосов: {poll.total_votes})")
        print(f"1. {opt_py.format_label()} | 2. {opt_cpp.format_label()}")
        poll.close_poll()
        print(f"[ЗАКРЫТИЕ ОПРОСА]: Голосование завершено (is_closed={poll.is_closed})")
        poll.reopen_poll()
        print(f"[ВОЗОБНОВЛЕНИЕ ОПРОСА]: Прием ответов возобновлен (is_closed={poll.is_closed})")

    def manage_chats(self) -> None:
        """Демонстрирует отправку сообщений, архивацию чата и управление звуком."""
        sender = self.users["alex_dev"]
        receiver = self.users["elena_art"]
        msg = DirectMessage("dm_1", sender.user_id, receiver.user_id, "Привет, Елена! Проверила отчет?")
        msg.mark_as_delivered()
        msg.mark_as_read(receiver)
        print(f"\n[ЛИЧНЫЕ СООБЩЕНИЯ]: @{sender.username} -> @{receiver.username}: {msg.content}")

        self.active_chat.archive()
        print(f"[АРХИВАЦИЯ]: Чат #{self.active_chat.chat_id} перемещен в архив (is_archived={self.active_chat.is_archived})")
        self.active_chat.unarchive()
        print(f"[РАЗАРХИВАЦИЯ]: Чат #{self.active_chat.chat_id} возвращен из архива (is_archived={self.active_chat.is_archived})")

        self.group_chat.mute()
        print(f"[ЗВУК ВЫКЛЮЧЕН]: Уведомления беседы '{self.group_chat.title}' отключены (is_muted={self.group_chat.is_muted})")
        self.group_chat.unmute()
        print(f"[ЗВУК ВКЛЮЧЕН]: Уведомления беседы '{self.group_chat.title}' включены (is_muted={self.group_chat.is_muted})")

    def manage_friendship(self) -> None:
        """Демонстрирует принятие заявки в друзья и расторжение дружбы."""
        sender = self.users["alex_dev"]
        receiver = self.users["elena_art"]
        req = FriendRequest("freq_1", sender.user_id, receiver.user_id, "Давай дружить в CosmoNet!")
        print(f"\n[ЗАЯВКА В ДРУЗЬЯ]: От @{sender.username} к @{receiver.username}: '{req.message}'")
        self.active_friendship = req.accept(receiver)
        print(f"[ДРУЖБА УСТАНОВЛЕНА]: Статус подтверждения={self.active_friendship.is_confirmed()}")
        self.active_friendship.terminate(sender)
        print(f"[РАСТОРЖЕНИЕ ДРУЖБЫ]: Дружба прекращена (статус={self.active_friendship.status})")

    def manage_blocking(self) -> None:
        """Демонстрирует блокировку и последующую разблокировку пользователя."""
        alex = self.users["alex_dev"]
        elena = self.users["elena_art"]
        self.active_block = BlockRecord(alex.user_id, elena.user_id, "тестовая блокировка")
        print(f"\n[БЛОКИРОВКА]: {self.active_block.format_block_notice()} (is_active={self.active_block.is_active})")
        self.active_block.deactivate(alex)
        print(f"[РАЗБЛОКИРОВКА]: Блокировка отменена (is_active={self.active_block.is_active})")

    def manage_finances(self) -> None:
        """Демонстрирует пополнение, перевод, заморозку и разморозку кошелька."""
        w_alex = self.wallets["alex_dev"]
        w_elena = self.wallets["elena_art"]
        print(f"\n[ФИНАНСЫ ДО]: Alex: {w_alex.balance} руб., Elena: {w_elena.balance} руб.")
        w_alex.deposit(500.0)
        print(f"[ПОПОЛНЕНИЕ]: Alex пополнил баланс на +500 руб. (Текущий баланс: {w_alex.balance} руб.)")

        tx = Transaction("tx_99", w_alex.wallet_id, w_elena.wallet_id, 300.0)
        tx.calculate_fee(1.0)
        tx.execute(w_alex, w_elena)
        print(f"[ПЕРЕВОД]: Переведено 300 руб. от Alex к Elena (комиссия: {tx.fee} руб.)")

        gift = VirtualGift("gift_star", "Золотая звезда", price_coins=50, icon_code="[Звезда]")
        gift.send_gift(w_alex, self.users["elena_art"])
        print(f"[ПОДАРОК]: Отправлен подарок: {gift.format_gift_card()}")

        w_alex.freeze()
        print(f"[ЗАМОРОЗКА]: Кошелек Alex заморожен (is_frozen={w_alex.is_frozen})")
        w_alex.unfreeze()
        print(f"[РАЗМОРОЗКА]: Кошелек Alex успешно разморожен (is_frozen={w_alex.is_frozen})")
        print(f"[ФИНАНСЫ ПОСЛЕ]: Alex: {w_alex.balance} руб., Elena: {w_elena.balance} руб.")

    def manage_moderation(self) -> None:
        """Демонстрирует добавление/удаление стоп-слов, а также наложение и отзыв санкций."""
        keyword = "запрещенка"
        count = self.banned_filter.add_keyword(keyword)
        print(f"\n[СТОП-СЛОВА]: Добавлено слово '{keyword}', всего ключевых слов: {count}")
        count_after = self.banned_filter.remove_keyword(keyword)
        print(f"[СТОП-СЛОВА]: Удалено слово '{keyword}', осталось ключевых слов: {count_after}")

        c_filter = ContentFilter(spam_threshold=0.6)
        score = c_filter.evaluate_spam_score("Купи крипта казино бесплатно http")
        print(f"[ФИЛЬТР СПАМА]: Оценка подозрительного текста: {score}")

        rep = ModerationReport("rep_101", self.users["alex_dev"].user_id, "bad_actor", "спам в чате")
        moderator = Moderator("mod_admin", "Офицер безопасности", is_head_moderator=True)
        moderator.review_report(rep, "вынесено предупреждение")
        print(f"[МОДЕРАТОР]: Жалоба рассмотрена: статус='{rep.status}', вердикт='{rep.resolution}'")

        sanction = Sanction("sanc_1", "bad_actor", sanction_type="mute", duration_days=3)
        print(f"[САНКЦИЯ]: Наложена санкция #{sanction.sanction_id} (отозвана={sanction.is_revoked})")
        sanction.revoke()
        print(f"[ОТЗЫВ САНКЦИИ]: Санкция досрочно аннулирована (отозвана={sanction.is_revoked})")

    def show_analytics_and_search(self) -> None:
        """Демонстрирует расчет вовлеченности (ER) и полнотекстовый поиск."""
        post = self.posts[0]
        metrics = EngagementMetrics(post.post_id, views=500, likes=75, shares=15, comments_count=10)
        er = metrics.calculate_engagement_rate()
        print(f"\n[АНАЛИТИКА]: Пост '{post.text_content}'")
        print(f"Просмотры: {metrics.views}, Лайки: {metrics.likes}, ER: {er}%")

        found_users = self.search.search_users("alex", list(self.users.values()))
        found_posts = self.search.search_posts("запущена", self.posts)
        print(f"[ПОИСК ПОЛЬЗОВАТЕЛЕЙ]: По запросу 'alex' найдено: {len(found_users)}")
        print(f"[ПОИСК ПУБЛИКАЦИЙ]: По запросу 'запущена' найдено: {len(found_posts)}")

    def run(self) -> None:
        """Главный цикл консольного приложения."""
        actions = {
            "1": self.show_system_report,
            "2": self.manage_users,
            "3": self.manage_posts,
            "4": self.manage_polls,
            "5": self.manage_chats,
            "6": self.manage_friendship,
            "7": self.manage_blocking,
            "8": self.manage_finances,
            "9": self.manage_moderation,
            "10": self.show_analytics_and_search,
        }

        while True:
            self.print_menu()
            try:
                choice = input("Выберите пункт меню (0-10): ").strip()
            except EOFError:
                print("\nПолучен сигнал завершения ввода. Завершение работы.")
                break
            if choice == "0":
                print("\nЗавершение работы социальной сети. До свидания!")
                break
            handler = actions.get(choice)
            if handler:
                handler()
            else:
                print("\nНеверный пункт меню. Повторите ввод.")
