# tests for wc_tool
# Tests for the main functions in wc.py.

import wc_tool.ccwc as ccwc

def test_count_lines():
    text = "Hello\nWorld\n"
    assert ccwc.count_lines(text) == 2

def test_count_words():
    text = "Hello World"
    assert ccwc.count_words(text) == 2

def test_count_chars():
    text = "Hello"
    assert ccwc.count_chars(text) == 5

def test_count_bytes():
    text = "Hello World"
    assert ccwc.count_bytes(text) == len(text.encode('utf-8'))

def test_count_bytes_unicode():
    text = "こんにちは"  # "Hello" in Japanese
    assert ccwc.count_bytes(text) == len(text.encode('utf-8'))
