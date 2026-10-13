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
from lab3.network.communication.direct_message import DirectMessage
from lab3.network.relations.friend_request import FriendRequest
from lab3.network.moderation.banned_word_filter import BannedWordFilter
from lab3.network.moderation.content_filter import ContentFilter
from lab3.network.moderation.moderation_report import ModerationReport
from lab3.network.moderation.moderator import Moderator
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
        """Выводит главное меню возможностей социальной сети."""
        print("\n" + "=" * 60)
        print("     СОЦИАЛЬНАЯ СЕТЬ CosmoNet — КОНСОЛЬНОЕ УПРАВЛЕНИЕ")
        print("=" * 60)
        print("1. Показать сводный отчет системы")
        print("2. Просмотр зарегистрированных пользователей")
        print("3. Опубликовать новую запись в ленте")
        print("4. Продемонстрировать опрос и голосование")
        print("5. Отправить личное сообщение")
        print("6. Заявка в друзья и установление дружбы")
        print("7. Модерация: проверка спама и жалоба")
        print("8. Экономика: перевод средств и виртуальный подарок")
        print("9. Аналитика ленты и полнотекстовый поиск")
        print("0. Выход")
        print("=" * 60)

    def show_system_report(self) -> None:
        """Демонстрирует системный статус сети."""
        print("\n[СИСТЕМА]:", self.system.generate_system_report())

    def list_users(self) -> None:
        """Отображает список активных пользователей."""
        print("\n[СПИСОК ПОЛЬЗОВАТЕЛЕЙ]:")
        for username, user_account in self.users.items():
            status = "Активен" if user_account.is_active else "Заблокирован"
            print(f"- @{username} (ID: {user_account.user_id}, Email: {user_account.email}, Статус: {status})")

    def create_post_demo(self) -> None:
        """Создает новую публикацию и добавляет реакцию."""
        author = self.users["alex_dev"]
        new_post = Post(f"p_{len(self.posts) + 101}", author.user_id, "Архитектура ООП проекта полностью готова!")
        self.system.publish_post(new_post)
        self.posts.append(new_post)
        react = Reaction("like", self.users["elena_art"].user_id, new_post.post_id)
        comment = Comment(f"c_{len(self.posts)}", new_post.post_id, self.users["elena_art"].user_id, "Поздравляю с релизом!")
        comment.like(react)
        print(f"\n[УСПЕХ]: Опубликован пост '{new_post.text_content}' от @{author.username}")
        print(f"[КОММЕНТАРИЙ]: @elena_art: '{comment.text}' [+1 Лайк] (лайков: {comment.likes_count})")

    def run_poll_demo(self) -> None:
        """Демонстрирует создание опроса и подсчет голосов."""
        poll = PollPost("poll_1", "Какой язык программирования лучше для ООП?")
        opt_py = PollOption("opt_1", "Python")
        opt_cpp = PollOption("opt_2", "C++")
        poll.add_vote(opt_py)
        poll.add_vote(opt_py)
        poll.add_vote(opt_cpp)
        poll.calculate_results([opt_py, opt_cpp])
        print(f"\n[ОПРОС]: {poll.question} (Всего голосов: {poll.total_votes})")
        print(f"1. {opt_py.format_label()}")
        print(f"2. {opt_cpp.format_label()}")

    def send_message_demo(self) -> None:
        """Демонстрирует отправку и прочтение личного сообщения."""
        sender = self.users["alex_dev"]
        receiver = self.users["elena_art"]
        msg = DirectMessage("dm_1", sender.user_id, receiver.user_id, "Привет, Елена! Проверила отчет?")
        msg.mark_as_delivered()
        print(f"\n[ЛИЧНЫЕ СООБЩЕНИЯ]: @{sender.username} -> @{receiver.username}: {msg.content}")
        print(f"Статус до прочтения: {msg.format_preview()}")
        msg.mark_as_read(receiver)
        print(f"Статус после прочтения: {msg.format_preview()}")

    def friendship_demo(self) -> None:
        """Демонстрирует отправку и подтверждение дружбы."""
        sender = self.users["alex_dev"]
        receiver = self.users["elena_art"]
        req = FriendRequest("freq_1", sender.user_id, receiver.user_id, "Давай дружить в CosmoNet!")
        print(f"\n[ДРУЖБА]: Заявка от @{sender.username} к @{receiver.username}: '{req.message}'")
        friendship = req.accept(receiver)
        print(f"Статус дружбы: подтверждена={friendship.is_confirmed()}, уровень близости: {friendship.closeness_level}")

    def moderation_demo(self) -> None:
        """Демонстрирует проверку контента фильтрами и работу модератора."""
        c_filter = ContentFilter(spam_threshold=0.6)
        spam_text = "Купи крипта казино бесплатно http"
        score = c_filter.evaluate_spam_score(spam_text)
        print(f"\n[МОДЕРАЦИЯ]: Текст '{spam_text}' получил спам-балл: {score}")

        report = ModerationReport("rep_101", self.users["alex_dev"].user_id, "bad_actor", "спам в комментариях")
        moderator = Moderator("mod_admin", "Старший офицер безопасности", is_head_moderator=True)
        moderator.review_report(report, "вынесена блокировка")
        print(f"Жалоба рассмотрена модератором: статус='{report.status}', вердикт='{report.resolution}'")

    def monetization_demo(self) -> None:
        """Демонстрирует работу кошельков, транзакций и подарков."""
        w_alex = self.wallets["alex_dev"]
        w_elena = self.wallets["elena_art"]
        print(f"\n[ФИНАНСЫ]: До операции -> Alex: {w_alex.balance} руб., Elena: {w_elena.balance} руб.")

        tx = Transaction("tx_99", w_alex.wallet_id, w_elena.wallet_id, 300.0)
        tx.calculate_fee(1.0)
        tx.execute(w_alex, w_elena)
        print(f"Выполнен перевод 300 руб. (комиссия: {tx.fee} руб.): статус={tx.status}")

        gift = VirtualGift("gift_star", "Золотая звезда", price_coins=50, icon_code="[Звезда]")
        gift.send_gift(w_alex, self.users["elena_art"])
        print(f"Отправлен подарок: {gift.format_gift_card()}")
        print(f"Балансы после операций -> Alex: {w_alex.balance} руб., Elena: {w_elena.balance} руб.")

    def analytics_search_demo(self) -> None:
        """Демонстрирует аналитику вовлеченности и поиск."""
        post = self.posts[0]
        metrics = EngagementMetrics(post.post_id, views=500, likes=75, shares=15, comments_count=10)
        er = metrics.calculate_engagement_rate()
        print(f"\n[АНАЛИТИКА]: Пост '{post.text_content}'")
        print(f"Просмотры: {metrics.views}, Лайки: {metrics.likes}, ER: {er}%")

        found_users = self.search.search_users("alex", list(self.users.values()))
        found_posts = self.search.search_posts("запущена", self.posts)
        print(f"[ПОИСК]: По запросу 'alex' найдено пользователей: {len(found_users)}")
        print(f"[ПОИСК]: По запросу 'запущена' найдено постов: {len(found_posts)}")

    def run(self) -> None:
        """Главный цикл консольного приложения."""
        actions = {
            "1": self.show_system_report,
            "2": self.list_users,
            "3": self.create_post_demo,
            "4": self.run_poll_demo,
            "5": self.send_message_demo,
            "6": self.friendship_demo,
            "7": self.moderation_demo,
            "8": self.monetization_demo,
            "9": self.analytics_search_demo,
        }

        while True:
            self.print_menu()
            try:
                choice = input("Выберите пункт меню (0-9): ").strip()
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
