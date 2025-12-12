import os
import pytest
from bs4 import BeautifulSoup

def test_html_exists():
    assert os.path.exists('index.html')

def test_html_structure():
    with open('index.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    assert soup.find('title') is not None
    assert soup.find('body') is not None

def test_portfolio_content():
    with open('index.html', 'r') as f:
        content = f.read()

    assert 'portfolio' in content.lower()
    assert len(content) > 100
