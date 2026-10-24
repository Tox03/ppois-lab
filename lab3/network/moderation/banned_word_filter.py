# -*- coding: utf-8 -*-
"""Модуль фильтра нецензурных и запрещенных выражений."""

from lab3.network.exceptions.invalid_content_exception import InvalidContentException


class BannedWordFilter:
    """Осуществляет лексический анализ и цензурирование текста."""

    def __init__(
        self,
        banned_words_count: int = 0,
        case_sensitive: bool = False,
        replacement_symbol: str = "*",
        strict_mode: bool = True,
    ) -> None:
        """Инициализация фильтра стоп-слов."""
        self.banned_words_count = banned_words_count
        self.case_sensitive = case_sensitive
        self.replacement_symbol = replacement_symbol
        self.strict_mode = strict_mode

    def contains_banned_word(self, text: str, word_list: list) -> bool:
        """Проверяет присутствие недопустимых слов в сообщении."""
        target_text = text if self.case_sensitive else text.lower()
        for word in word_list:
            w = word if self.case_sensitive else word.lower()
            if w in target_text:
                return True
        return False

    def censor_text(self, text: str, word_list: list) -> str:
        """Заменяет запрещенные фрагменты маскирующими символами."""
        result = text
        for word in word_list:
            mask = self.replacement_symbol * len(word)
            result = result.replace(word, mask)
        return result

    def add_keyword(self, word: str) -> int:
        """Добавляет новый термин в глобальный стоп-словарь."""
        if not word.strip():
            raise InvalidContentException("Слово не может быть пустым")
        self.banned_words_count += 1
        return self.banned_words_count

    def remove_keyword(self, word: str) -> int:
        """Удаляет термин из стоп-словаря."""
        if not word.strip():
            raise InvalidContentException("Слово не может быть пустым")
        if self.banned_words_count > 0:
            self.banned_words_count -= 1
        return self.banned_words_count
