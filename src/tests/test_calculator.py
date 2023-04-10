# type: ignore
import pytest
from src.calculator import added, extract_expression_params


def test_empty_input_returns_zero():
    assert added('') == 0


def test_added_accepts_only_strings():
    with pytest.raises(TypeError):
        added(None)


@pytest.mark.parametrize(
    'expression, expected_result',
    [
        ('//,\n10,10,10', 30),
        ('//,\n50,50', 100),
        ('//,\n-100,200', 100),
        ('//,\n-10,10', 0),
        ('//,\n-10,10\n10', 10),
        ('//,\n0,10\n10', 20),
        ('//,\n1,2\n3', 6),
        ('//,\n0,10\n10\n10', 30),
    ]
)
def test_added_evaluates_the_sum_correctly(expression, expected_result):
    assert added(expression) == expected_result


@pytest.mark.parametrize(
    'expression',
    [
        '//,\n1,2\n\n3',
        '//,\n1,2\n3,',
        '//,\n1,2,',
    ]
)
def test_added_accepts_only_strings(expression):
    with pytest.raises(ValueError):
        added(expression)


@pytest.mark.parametrize(
    'expression, expected_result',
    [
        ('//,\n1,2', 3),
        ('//,\n1,2,3', 6),
        ('//|\n1|2', 3),
        ('//sep\n1sep2', 3),
    ]
)
def test_added_recognizes_different_delimiters(expression, expected_result):
    assert added(expression) == expected_result


@pytest.mark.parametrize(
    'expression',
    [
        '//;\n1,2\n\n3',
        '//|\n1,2\n3,',
        '//sep\n1,2,',
    ]
)
def test_inconsistent_delimiter_raises_value_error(expression):
    with pytest.raises(ValueError):
        added(expression)


@pytest.mark.parametrize(
    'expression, expected_result',
    [
        (
            '//,\n1,2', (
                ',', '1,2'
            )
        ),
        (
            '//,\n1,2,3', (
                ',', '1,2,3'
            )
        ),
        (
            '//|\n1|2', (
                '|', '1|2'
            )
        ),
        (
            '//sep\n1sep2', (
                'sep', '1sep2'
            )
        ),
    ]
)
def test_extractor_recognizes_delimiter_and_input_numbers(expression, expected_result):
    assert extract_expression_params(expression) == expected_result
