"""Точка входа для запуска консольного интерфейса завода по изготовлению автомобильных деталей."""

import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Добавляем корневой каталог лабораторной работы в sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from cli.plant_cli import PlantCli

def main() -> None:
    """Запуск интерактивного консольного приложения."""
    app = PlantCli()
    app.run()

if __name__ == "__main__":
    main()
