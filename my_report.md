# Отчет о качестве кода
**Дата:** 2025-12-27T23:46:08.212614

**Проверено файлов:** 2

## Файл: `examples/bad_code.py`
### PEP 8
Обнаружено 4 нарушений:
- `examples/bad_code.py:9:6: E225 missing whitespace around operator`
- `examples/bad_code.py:10:6: E225 missing whitespace around operator`
- `examples/bad_code.py:13:1: E302 expected 2 blank lines, found 1`
- `examples/bad_code.py:15:1: W391 blank line at end of file`
### Сложность (Cyclomatic Complexity)
**Средняя сложность:** 3.00
- 🔴 `complex_function` (function): 5
- 🔴 `EmptyClass` (function): 1
### Docstrings
**Покрытие:** 0.0%
Отсутствуют docstring'и в:
- `complex_function` (Line 1)
- `EmptyClass` (Line 13)
---
## Файл: `examples/good_code.py`
### PEP 8
Обнаружено 2 нарушений:
- `examples/good_code.py:7:1: E302 expected 2 blank lines, found 1`
- `examples/good_code.py:16:1: W391 blank line at end of file`
### Сложность (Cyclomatic Complexity)
**Средняя сложность:** 1.33
- 🔴 `add` (function): 1
- 🔴 `Calculator` (function): 2
- 🟢 `multiply` (function): 1
### Docstrings
**Покрытие:** 100.0%
---