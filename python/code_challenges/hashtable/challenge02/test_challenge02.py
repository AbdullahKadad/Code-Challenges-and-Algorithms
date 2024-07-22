import pytest
from challenge02 import find_first_repeated_word

def test_no_repetition():
    """
    Test that the function returns 'No Repetition' for a string with no repeated words.
    """
    input_str = "I am learning programming at ASAC."
    assert find_first_repeated_word(input_str) == "No Repetition"

def test_repeated_word():
    """
    Test that the function correctly identifies the first repeated word in a string.
    """
    input_str = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    assert find_first_repeated_word(input_str) == "ASAC"

def test_punctuation_handling():
    """
    Test that the function handles punctuation correctly and finds the first repeated word.
    """
    input_str = "Hello! Are you ready? Yes, I am ready to go. Ready?"
    assert find_first_repeated_word(input_str) == "ready"

def test_mixed_case_repetition():
    """
    Test that the function is case-insensitive when identifying repeated words.
    """
    input_str = "Python python PYTHON"
    assert find_first_repeated_word(input_str) == "Python"

def test_edge_case_empty_string():
    """
    Test the function with an empty string.
    """
    input_str = ""
    assert find_first_repeated_word(input_str) == "No Repetition"

def test_edge_case_single_word():
    """
    Test the function with a single word string.
    """
    input_str = "Hello"
    assert find_first_repeated_word(input_str) == "No Repetition"

def test_edge_case_single_repeated_word():
    """
    Test that the function identifies a single repeated word in a string.
    """
    input_str = "Hello Hello"
    assert find_first_repeated_word(input_str) == "Hello"

def test_words_with_numbers():
    """
    Test that the function correctly handles words with numbers.
    """
    input_str = "Word1 Word2 Word3 Word1"
    assert find_first_repeated_word(input_str) == "Word1"

def test_words_with_hyphens():
    """
    Test that the function correctly handles words with hyphens.
    """
    input_str = "high-speed high speed"
    assert find_first_repeated_word(input_str) == "high"
