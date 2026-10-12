"""Точка входа для запуска консольного интерфейса завода по изготовлению автомобильных деталей."""

import os
import sys

# Добавляем корневой каталог лабораторной работы в sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from cli.plant_cli import PlantCli

def main() -> None:
    """Запуск интерактивного консольного приложения."""
    app = PlantCli()
    app.run()

if __name__ == "__main__":
    main()
