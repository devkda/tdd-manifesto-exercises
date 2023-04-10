# type: ignore
import pytest
from src.fizzbuzz import fizzbuzz, is_fizz, is_buzz, is_fizzbuzz


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


def test_fizzbuzz_accepts_only_numbers():
    with pytest.raises(TypeError):
        fizzbuzz('NaN')
    with pytest.raises(TypeError):
        fizzbuzz(None)


def test_is_fizz_recognizes_multiples_of_three_and_not_five(
    multiples_of_three_and_not_five, multiples_of_five_and_not_three
):
    for multiple in multiples_of_three_and_not_five:
        assert is_fizz(multiple) is True
    for multiple in multiples_of_five_and_not_three:
        assert is_fizz(multiple) is False


def test_is_buzz_recognizes_multiples_of_five_and_not_three(
    multiples_of_three_and_not_five, multiples_of_five_and_not_three
):
    for multiple in multiples_of_three_and_not_five:
        assert is_buzz(multiple) is False
    for multiple in multiples_of_five_and_not_three:
        assert is_buzz(multiple) is True


def test_is_fizzbuzz_recognizes_multiples_of_three_and_five(multiples_of_three_and_five):
    for multiple in multiples_of_three_and_five:
        assert is_fizzbuzz(multiple) is True
