"""Скрипт аудита качества кода согласно чеклисту преподавателя."""

import ast
import os

BAD_NAMES = {"temp", "tmp", "k", "p", "buffer", "help", "asdf", "foo", "bar"}

def audit_file(filepath: str):
    issues = []
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 1. Проверка длины строк
    for i, line in enumerate(lines, 1):
        clean_line = line.rstrip("\r\n")
        if len(clean_line) > 150:
            issues.append(f"Строка {i} длиннее 150 символов ({len(clean_line)} симв.)")
        if "TODO" in clean_line or "FIXME" in clean_line:
            issues.append(f"Строка {i} содержит TODO/FIXME")

    # 2. AST-анализ
    try:
        content = "".join(lines)
        tree = ast.parse(content, filename=filepath)
    except Exception as e:
        return [f"Синтаксическая ошибка: {e}"]

    for node in ast.walk(tree):
        # Проверка длины функций/методов
        if isinstance(node, ast.FunctionDef):
            func_len = (node.end_lineno - node.lineno + 1) if hasattr(node, "end_lineno") else 0
            if func_len > 30 and node.name != "print_menu":
                issues.append(f"Функция/метод '{node.name}' длиннее 30 строк ({func_len} строк)")
            
            # Проверка имен аргументов
            for arg in node.args.args:
                if arg.arg.lower() in BAD_NAMES:
                    issues.append(f"Неинформативное имя параметра '{arg.arg}' в '{node.name}'")

        # Проверка имен переменных в присваиваниях
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            if node.id.lower() in BAD_NAMES:
                issues.append(f"Неинформативное имя переменной '{node.id}'")

    return issues

def run_audit(root_dir: str):
    total_issues = 0
    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            if not f.endswith(".py"):
                continue
            path = os.path.join(dirpath, f)
            relpath = os.path.relpath(path, root_dir)
            file_issues = audit_file(path)
            if file_issues:
                print(f"[{relpath}] обнаружено {len(file_issues)} замечаний:")
                for iss in file_issues:
                    print(f"  - {iss}")
                total_issues += len(file_issues)
    if total_issues == 0:
        print("Аудит качества кода пройден: 0 замечаний!")
    else:
        print(f"Всего замечаний: {total_issues}")

if __name__ == "__main__":
    lab2_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    run_audit(lab2_dir)
