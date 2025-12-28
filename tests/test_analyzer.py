import os
import pytest
from src.analyzer import Analyzer

def test_analyzer_init():
    analyzer = Analyzer(".")
    assert analyzer.target_dir == "."

def test_analyze_excludes_venv(tmp_path):
    # Create a dummy structure
    d = tmp_path / "venv"
    d.mkdir()
    p = d / "bad.py"
    p.write_text("a=1")
    
    src = tmp_path / "src"
    src.mkdir()
    p2 = src / "good.py"
    p2.write_text("a=1")
    
    analyzer = Analyzer(str(tmp_path))
    results = analyzer.analyze()
    
    # Should not contain venv/bad.py
    assert not any("bad.py" in k for k in results.keys())
    # Should contain src/good.py
    assert any("good.py" in k for k in results.keys())

