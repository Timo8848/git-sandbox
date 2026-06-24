from algorithms.palindrome import is_palindrome


def test_simple_palindrome():
    assert is_palindrome("level") is True


def test_sentence_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_not_palindrome():
    assert is_palindrome("hello") is False


def test_empty_string():
    assert is_palindrome("") is True
