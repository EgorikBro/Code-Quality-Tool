import os
from .metrics import Metrics

class Analyzer:
    def __init__(self, target_dir):
        self.target_dir = target_dir

    def analyze(self):
        results = {}
        # Проходим по всем файлам в директории
        for root, dirs, files in os.walk(self.target_dir):
            # Исключаем venv и скрытые папки (более надежная проверка)
            path_parts = os.path.normpath(root).split(os.sep)
            if 'venv' in path_parts or '.git' in path_parts:
                continue
                
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    results[file_path] = self._analyze_file(file_path)
        return results

    def _analyze_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
        except Exception as e:
            return {"error": f"Cannot read file: {str(e)}"}

        return {
            "pep8": Metrics.check_pep8(file_path),
            "complexity": Metrics.check_complexity(code),
            "docstrings": Metrics.check_docstrings_ast(code)
        }

