"""练习用的小算法工具包。

每个模块一个独立、好懂的算法，配套测试在 tests/ 下。
练习时每个人改不同的模块，互不干扰。
"""

from .fizzbuzz import fizzbuzz
from .palindrome import is_palindrome
from .binary_search import binary_search

__all__ = ["fizzbuzz", "is_palindrome", "binary_search"]
