# Write your test here
import pytest
from challenge02 import Stack

def test_valid_parentheses():
    stack = Stack()
    assert stack.is_valid("()") == True
    assert stack.is_valid("()[]{}") == True
    assert stack.is_valid("{[()]}") == True
    assert stack.is_valid("{[]}") == True
    assert stack.is_valid("") == True

def test_invalid_parentheses():
    stack = Stack()
    assert stack.is_valid("(]") == False
    assert stack.is_valid("([)]") == False
    assert stack.is_valid("{[}") == False
    assert stack.is_valid("}") == False
    assert stack.is_valid("{[}") == False

def test_mixed_characters():
    stack = Stack()
    assert stack.is_valid("a(b)c") == True
    assert stack.is_valid("[a+b]*(x/y)-{z}") == True
    assert stack.is_valid("a{b(c]d}e") == False
    assert stack.is_valid("a{b(c)d}e}") == False
    assert stack.is_valid("[") == False

def test_nested_parentheses():
    stack = Stack()
    assert stack.is_valid("{[({})]}") == True
    assert stack.is_valid("[{({[{}]})}]") == True
    assert stack.is_valid("{[(])}") == False
    assert stack.is_valid("{[()()]}[") == False
    assert stack.is_valid("[(({{[[]]}}))]") == True

def test_only_opening_parentheses():
    stack = Stack()
    assert stack.is_valid("(") == False
    assert stack.is_valid("{") == False
    assert stack.is_valid("[") == False
    assert stack.is_valid("(((") == False
    assert stack.is_valid("{{{{") == False

def test_only_closing_parentheses():
    stack = Stack()
    assert stack.is_valid(")") == False
    assert stack.is_valid("}") == False
    assert stack.is_valid("]") == False
    assert stack.is_valid(")))") == False
    assert stack.is_valid("}}}}") == False
