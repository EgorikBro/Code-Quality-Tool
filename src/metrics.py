import ast
import subprocess
import shutil
import sys
from radon.complexity import cc_visit

class Metrics:
    @staticmethod
    def check_pep8(file_path):
        """
        Проверяет соблюдение PEP 8 используя flake8.
        """
        if not shutil.which("flake8"):
             return {"error": "flake8 not found", "violations": [], "count": 0}
        
        try:
            # Запускаем flake8 как подпроцесс
            result = subprocess.run(
                [sys.executable, "-m", "flake8", "--format=default", file_path],
                capture_output=True,
                text=True
            )
            violations = [line for line in result.stdout.strip().split('\n') if line]
            return {
                "violations": violations,
                "count": len(violations)
            }
        except Exception as e:
            return {"error": str(e), "violations": [], "count": 0}

    @staticmethod
    def check_complexity(code):
        """
        Проверяет цикломатическую сложность используя radon.
        """
        try:
            blocks = cc_visit(code)
            complexity_data = []
            total_complexity = 0
            for block in blocks:
                complexity_data.append({
                    "name": block.name,
                    "type": getattr(block, 'type', 'function'),
                    "complexity": block.complexity,
                    "rank": block.letter
                })
                total_complexity += block.complexity
            
            avg_complexity = total_complexity / len(blocks) if blocks else 0
            return {
                "details": complexity_data,
                "average": avg_complexity
            }
        except Exception as e:
            return {"error": str(e), "details": [], "average": 0}

    @staticmethod
    def check_docstrings_ast(code):
        """
        Проверяет наличие docstring'ов используя AST (абстрактное синтаксическое дерево).
        """
        try:
            tree = ast.parse(code)
            missing_docs = []
            found_docs = 0
            total_defs = 0
            
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    total_defs += 1
                    if not ast.get_docstring(node):
                        missing_docs.append({
                            "type": type(node).__name__,
                            "name": node.name,
                            "lineno": node.lineno
                        })
                    else:
                        found_docs += 1
            
            coverage = (found_docs / total_defs * 100) if total_defs > 0 else 100
            return {
                "missing": missing_docs,
                "coverage": coverage,
                "total_definitions": total_defs
            }
        except Exception as e:
            return {"error": str(e), "missing": [], "coverage": 0}

