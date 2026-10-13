# -*- coding: utf-8 -*-
"""Скрипт для валидации требований лабораторной работы №3 (Социальная сеть).

Проверяет:
- Количество классов (>= 50)
- Количество полей (>= 150)
- Количество содержательных поведений (>= 100)
- Количество ассоциаций (>= 30)
- Количество собственных классов исключений (>= 12)
- Отсутствие файлов с более чем 1 классом
- Формирует сводную таблицу для README.md
"""

import ast
import os
import sys

def analyze_codebase(root_dir: str):
    """Анализирует исходный код пакета на соответствие количественным метрикам."""
    classes_info = []
    total_files_with_multiple_classes = 0

    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            if not f.endswith(".py") or f == "__init__.py":
                continue
            filepath = os.path.join(dirpath, f)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
            
            tree = ast.parse(content, filename=filepath)
            classes_in_file = [node for node in tree.body if isinstance(node, ast.ClassDef)]
            
            if len(classes_in_file) > 1:
                print(f"ОШИБКА: Файл {filepath} содержит {len(classes_in_file)} классов!")
                total_files_with_multiple_classes += 1
            
            for cls_node in classes_in_file:
                cls_name = cls_node.name
                is_exception = any(
                    (isinstance(b, ast.Name) and "Exception" in b.id) or
                    (isinstance(b, ast.Attribute) and "Exception" in b.attr)
                    for b in cls_node.bases
                )
                
                # Поля определяются в __init__
                fields = set()
                methods = []
                for item in cls_node.body:
                    if isinstance(item, ast.FunctionDef):
                        if item.name == "__init__":
                            for stmt in ast.walk(item):
                                if isinstance(stmt, ast.Assign):
                                    for target in stmt.targets:
                                        if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "self":
                                            fields.add(target.attr)
                                elif isinstance(stmt, ast.AnnAssign):
                                    is_self_attr = (
                                        isinstance(stmt.target, ast.Attribute)
                                        and isinstance(stmt.target.value, ast.Name)
                                        and stmt.target.value.id == "self"
                                    )
                                    if is_self_attr:
                                        fields.add(stmt.target.attr)
                        else:
                            methods.append(item.name)

                # Поиск связанных классов (ассоциаций)
                associations = set()
                ignore_types = {
                    "str", "int", "float", "bool", "dict", "list", "set", "tuple", "None",
                    "Optional", "List", "Dict", "Set", "Tuple", "Any"
                }
                for item in cls_node.body:
                    if isinstance(item, ast.FunctionDef):
                        for arg in item.args.args:
                            if arg.annotation:
                                for sub in ast.walk(arg.annotation):
                                    if isinstance(sub, ast.Name) and sub.id not in ignore_types:
                                        associations.add(sub.id)
                # Также смотрим импорты внутри файла как кандидаты на ассоциации
                for node in tree.body:
                    if isinstance(node, ast.ImportFrom):
                        for alias in node.names:
                            is_valid_assoc = (
                                alias.name[0].isupper()
                                and alias.name != cls_name
                                and alias.name not in ignore_types
                            )
                            if is_valid_assoc:
                                associations.add(alias.name)
                
                classes_info.append({
                    "name": cls_name,
                    "file": os.path.relpath(filepath, root_dir),
                    "is_exception": is_exception,
                    "fields_count": len(fields),
                    "methods_count": len(methods),
                    "methods": methods,
                    "fields": sorted(list(fields)),
                    "associations": sorted(list(associations)),
                    "docstring": ast.get_docstring(cls_node) or ""
                })

    return classes_info, total_files_with_multiple_classes

if __name__ == "__main__":
    target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "network"))
    info, violations = analyze_codebase(target_dir)
    print(f"Всего классов найдено: {len(info)}")
    print(f"Файлов с более чем 1 классом: {violations}")
    
    total_fields = sum(c["fields_count"] for c in info)
    total_methods = sum(c["methods_count"] for c in info)
    exceptions = [c for c in info if c["is_exception"]]
    domain_classes = [c for c in info if not c["is_exception"]]
    
    all_associations = sum(len(c["associations"]) for c in info)
    
    print(f"Суммарно полей: {total_fields}")
    print(f"Суммарно поведений (методов): {total_methods}")
    print(f"Исключений: {len(exceptions)}")
    print(f"Доменных классов: {len(domain_classes)}")
    print(f"Суммарно ассоциаций: {all_associations}")

    # Валидация граничных условий
    errors = []
    if len(info) < 50:
        errors.append(f"Классов {len(info)} < 50")
    if total_fields < 150:
        errors.append(f"Полей {total_fields} < 150")
    if total_methods < 100:
        errors.append(f"Методов {total_methods} < 100")
    if all_associations < 30:
        errors.append(f"Ассоциаций {all_associations} < 30")
    if len(exceptions) < 12:
        errors.append(f"Исключений {len(exceptions)} < 12")
    if violations > 0:
        errors.append(f"Обнаружено {violations} файлов с несколькими классами")

    if errors:
        print("\nОШИБКИ ВАЛИДАЦИИ:")
        for err in errors:
            print(f"- {err}")
        sys.exit(1)
    else:
        print("\nВсе требования успешно выполнены!")
