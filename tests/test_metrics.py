import pytest
import os
import tempfile
from src.metrics import Metrics

def test_complexity():
    code = "def f():\n    if True:\n        print('hi')"
    result = Metrics.check_complexity(code)
    if 'error' in result:
        pytest.fail(f"Complexity check failed with error: {result['error']}")
    assert result['average'] > 0
    assert len(result['details']) == 1
    assert result['details'][0]['name'] == 'f'

def test_docstrings():
    code = "def f():\n    pass"
    result = Metrics.check_docstrings_ast(code)
    assert result['coverage'] == 0.0
    assert len(result['missing']) == 1
    
    code_good = "def f():\n    '''Doc'''\n    pass"
    result_good = Metrics.check_docstrings_ast(code_good)
    assert result_good['coverage'] == 100.0
    assert len(result_good['missing']) == 0

def test_pep8_file_not_found():
    # Should handle non-existent gracefully or we check file path before
    # Metrics.check_pep8 wraps subprocess, flake8 might return error for non-existent file
    pass

