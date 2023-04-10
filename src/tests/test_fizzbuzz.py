import pytest
from src.fizzbuzz import fizzbuzz


@pytest.fixture
def multiples_of_three_and_not_five():
    return {
        number for number in range(1000) if number % 3 == 0 and number % 5 != 0
    }


@pytest.fixture
def multiples_of_five_and_not_three():
    return {
        number for number in range(1000) if number % 5 == 0 and number % 3 != 0
    }


@pytest.fixture
def multiples_of_three_and_five():
    return {
        number for number in range(1000) if number % 5 == 0 and number % 3 == 0
    }


def test_fizzbuzz_converts_int_to_str():
    actual_result = fizzbuzz(1)
    assert actual_result == '1'
    assert type(actual_result) is str


def test_fizzbuzz_returns_fizz_only_for_multiples_of_three(multiples_of_three_and_not_five):
    """
    For multiples of three return “Fizz” instead of the number
    """
    for multiple in multiples_of_three_and_not_five:
        assert fizzbuzz(multiple) == "Fizz"


def test_fizzbuzz_returns_buzz_for_multiples_of_five(multiples_of_five_and_not_three):
    """
    For the multiples of five return “Buzz”
    """
    for multiple in multiples_of_five_and_not_three:
        assert fizzbuzz(multiple) == "Buzz"


def test_fizzbuzz_returns_fizzbuzz_for_multiples_of_both(multiples_of_three_and_five):
    """
    For numbers that are multiples of both three and five return “FizzBuzz”.
    """
    for multiple in multiples_of_three_and_five:
        assert fizzbuzz(multiple) == "FizzBuzz"
