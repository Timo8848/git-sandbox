import pytest

from algorithms.fizzbuzz import fizzbuzz


def test_basic_sequence():
    assert fizzbuzz(5) == "1\n2\nFizz\n4\nBuzz"


def test_fizzbuzz_at_15():
    lines = fizzbuzz(15).split("\n")
    assert lines[2] == "Fizz"
    assert lines[4] == "Buzz"
    assert lines[14] == "FizzBuzz"


def test_invalid_input():
    with pytest.raises(ValueError):
        fizzbuzz(0)
