# Инструмент оценки качества кода (Code Quality Assessment Tool)

![Tests](https://github.com/username/repo/workflows/Tests/badge.svg)

## Описание

Этот проект представляет собой инструмент для автоматического анализа качества Python кода. Он проверяет соответствие стандартам PEP 8, вычисляет цикломатическую сложность (Cyclomatic Complexity) и проверяет наличие документации (docstrings).

Проект разработан в рамках творческого задания и демонстрирует использование современных практик разработки: CI/CD, модульное тестирование и статический анализ.

### Основные возможности

*   **Проверка PEP 8:** Использует `flake8` для выявления нарушений стиля кодирования.
*   **Анализ сложности:** Использует `radon` для вычисления цикломатической сложности функций и классов.
*   **Проверка документации:** Использует AST (Abstract Syntax Tree) для проверки наличия docstring'ов во всех функциях и классах.
*   **Генерация отчетов:** Создает подробные отчеты в форматах JSON и Markdown.

## Структура проекта

```
code_quality_tool/
├── .github/workflows/   # CI/CD конфигурации
├── src/                 # Исходный код
│   ├── analyzer.py      # Логика обхода файлов
│   ├── metrics.py       # Реализация метрик (PEP8, Complexity, AST Docstrings)
│   └── reporter.py      # Генерация отчетов
├── tests/               # Модульные тесты
├── examples/            # Примеры кода (плохой/хороший) для демонстрации
├── main.py              # Точка входа (CLI)
├── requirements.txt     # Зависимости
└── README.md            # Документация
```

## Установка

Для работы требуется Python 3.8+.

1.  Клонируйте репозиторий:
    ```bash
    git clone https://github.com/your-username/code-quality-tool.git
    cd code_quality_tool
    ```

2.  Создайте виртуальное окружение (рекомендуется):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # или
    .\venv\Scripts\activate   # Windows
    ```

3.  Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Использование

Запустите инструмент, указав директорию для анализа:

```bash
python main.py examples/
```

### Опции

*   `TARGET_DIR`: Путь к директории с кодом (по умолчанию `.`).
*   `--output`: Имя выходного файла отчета (без расширения). По умолчанию `report`.

Пример запуска с сохранением отчета в `my_analysis`:

```bash
python main.py src/ --output my_analysis
```

После выполнения будут созданы файлы `my_analysis.json` и `my_analysis.md`.

## Примеры

### Анализ "плохого" кода (`examples/bad_code.py`)

**Вывод в консоль:**
```
Анализ директории: examples/...
Анализ завершен!
JSON отчет: report.json
Markdown отчет: report.md
```

**Фрагмент отчета (`report.md`):**

```markdown
## Файл: `examples/bad_code.py`
### PEP 8
Обнаружено 3 нарушений:
- `E225 missing whitespace around operator`
- `E302 expected 2 blank lines, found 1`
...

### Сложность
**Средняя сложность:** 4.00
- 🟢 `complex_function` (FunctionDef): 4

### Docstrings
**Покрытие:** 0.0%
Отсутствуют docstring'и в:
- `complex_function` (Line 1)
- `EmptyClass` (Line 11)
```

## Тестирование

Запуск модульных тестов:

```bash
python -m pytest tests/
```

## CI/CD и Автоматизация

В проекте настроены GitHub Actions workflows:

1.  **Tests (`ci.yml`):** Запускается при каждом push и pull request. Выполняет:
    *   Линтинг кода самого инструмента (`flake8`).
    *   Запуск тестов (`pytest`).
    
2.  **Self Check & Report (`self_check.yml`):** "Креативный" workflow.
    *   **Триггеры:** По расписанию (каждый понедельник) и вручную (`workflow_dispatch`).
    *   **Действие:** Запускает инструмент на самом себе (`src/`) и на примерах (`examples/`).
    *   **Результат:** Генерирует отчет `report.md` и сохраняет его как Artifact, доступный для скачивания. Это позволяет автоматически следить за качеством кода проекта без ручного запуска.

## Автор
Студент курса "AI в образовании"

