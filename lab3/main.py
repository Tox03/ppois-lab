# -*- coding: utf-8 -*-
"""Точка входа для запуска консольного интерфейса социальной сети."""

import os
import sys

# Добавляем корневой каталог проекта в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lab3.cli.network_cli import NetworkCli


def main() -> None:
    """Запуск интерактивного консольного приложения."""
    app = NetworkCli()
    app.run()


if __name__ == "__main__":
    main()
