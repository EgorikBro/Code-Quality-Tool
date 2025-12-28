import click
import os
from src.analyzer import Analyzer
from src.reporter import Reporter

@click.command()
@click.argument('target_dir', default='.')
@click.option('--output', default='report', help='Имя выходного файла (без расширения)')
def main(target_dir, output):
    """
    Инструмент оценки качества кода.
    
    Анализирует Python файлы в TARGET_DIR на соответствие PEP 8, сложность и наличие docstring'ов.
    """
    if not os.path.exists(target_dir):
        click.echo(f"Ошибка: Директория '{target_dir}' не найдена.")
        return

    click.echo(f"Анализ директории: {target_dir}...")
    analyzer = Analyzer(target_dir)
    results = analyzer.analyze()
    
    # Generate reports
    json_path = f"{output}.json"
    md_path = f"{output}.md"
    
    Reporter.generate_json(results, json_path)
    Reporter.generate_markdown(results, md_path)
    
    click.echo(f"Анализ завершен!")
    click.echo(f"JSON отчет: {json_path}")
    click.echo(f"Markdown отчет: {md_path}")

if __name__ == '__main__':
    main()

