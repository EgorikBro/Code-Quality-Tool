import json
from datetime import datetime

class Reporter:
    @staticmethod
    def generate_json(results, output_file="report.json"):
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        return output_file

    @staticmethod
    def generate_markdown(results, output_file="report.md"):
        lines = ["# Отчет о качестве кода", f"**Дата:** {datetime.now().isoformat()}", ""]
        
        total_files = len(results)
        lines.append(f"**Проверено файлов:** {total_files}")
        lines.append("")

        for file_path, data in results.items():
            lines.append(f"## Файл: `{file_path}`")
            if "error" in data:
                lines.append(f"❌ Ошибка: {data['error']}")
                continue

            # PEP 8
            pep8 = data.get("pep8", {})
            lines.append("### PEP 8")
            if pep8.get("count", 0) == 0:
                lines.append("✅ Нарушений не найдено")
            else:
                lines.append(f"Обнаружено {pep8.get('count')} нарушений:")
                for v in pep8.get("violations", [])[:5]:
                    lines.append(f"- `{v}`")
                if pep8.get("count") > 5:
                    lines.append(f"- ... и еще {pep8.get('count') - 5}")

            # Complexity
            comp = data.get("complexity", {})
            avg = comp.get("average", 0)
            lines.append(f"### Сложность (Cyclomatic Complexity)")
            lines.append(f"**Средняя сложность:** {avg:.2f}")
            
            details = comp.get("details", [])
            if not details:
                lines.append("Функций/классов не найдено.")
            else:
                for func in details:
                    rank_icon = "🟢"
                    if func['rank'] == 'B': rank_icon = "🟡"
                    elif func['rank'] in ['C', 'D', 'E', 'F']: rank_icon = "🔴"
                    
                    lines.append(f"- {rank_icon} `{func['name']}` ({func['type']}): {func['complexity']}")

            # Docstrings
            docs = data.get("docstrings", {})
            lines.append(f"### Docstrings")
            lines.append(f"**Покрытие:** {docs.get('coverage', 0):.1f}%")
            if docs.get("missing"):
                lines.append("Отсутствуют docstring'и в:")
                for m in docs.get("missing", []):
                    lines.append(f"- `{m['name']}` (Line {m['lineno']})")
            
            lines.append("---")

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        return output_file

