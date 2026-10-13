# -*- coding: utf-8 -*-
"""Модульные тесты для классов исключений социальной сети."""

import unittest
from lab3.network.exceptions.network_base_exception import NetworkBaseException
from lab3.network.exceptions.user_not_found_exception import UserNotFoundException
from lab3.network.exceptions.authentication_exception import AuthenticationException
from lab3.network.exceptions.access_denied_exception import AccessDeniedException
from lab3.network.exceptions.content_not_found_exception import ContentNotFoundException
from lab3.network.exceptions.content_blocked_exception import ContentBlockedException
from lab3.network.exceptions.invalid_content_exception import InvalidContentException
from lab3.network.exceptions.friendship_already_exists_exception import FriendshipAlreadyExistsException
from lab3.network.exceptions.user_already_blocked_exception import UserAlreadyBlockedException
from lab3.network.exceptions.group_not_found_exception import GroupNotFoundException
from lab3.network.exceptions.group_capacity_exceeded_exception import GroupCapacityExceededException
from lab3.network.exceptions.insufficient_privileges_exception import InsufficientPrivilegesException
from lab3.network.exceptions.payment_failed_exception import PaymentFailedException
from lab3.network.exceptions.subscription_expired_exception import SubscriptionExpiredException
from lab3.network.exceptions.report_already_processed_exception import ReportAlreadyProcessedException
from lab3.network.exceptions.rate_limit_exceeded_exception import RateLimitExceededException


class TestExceptions(unittest.TestCase):
    """Набор тестов для проверки 16 классов исключений."""

    def test_all_exceptions_inherit_from_base(self):
        """Проверка наследования всех исключений от NetworkBaseException."""
        exceptions = [
            UserNotFoundException("u1"),
            AuthenticationException("pwd"),
            AccessDeniedException("post"),
            ContentNotFoundException("c1"),
            ContentBlockedException("c1", "rules"),
            InvalidContentException("text"),
            FriendshipAlreadyExistsException("u1-u2"),
            UserAlreadyBlockedException("u2"),
            GroupNotFoundException("g1"),
            GroupCapacityExceededException(50),
            InsufficientPrivilegesException("ban"),
            PaymentFailedException("balance"),
            SubscriptionExpiredException("vip"),
            ReportAlreadyProcessedException("r1"),
            RateLimitExceededException(30),
        ]
        for exc in exceptions:
            self.assertIsInstance(exc, NetworkBaseException)
            self.assertTrue(len(str(exc)) > 0)


if __name__ == "__main__":
    unittest.main()
