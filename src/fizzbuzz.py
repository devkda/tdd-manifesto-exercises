"""Kata 1 – FizzBuzz
FizzBuzz is one of the most famous coding exercises for beginners. It is a simple exercise but an excellent one to start learning the TDD flow with.

Requirements
1. Write a “fizzBuzz” method that accepts a number as input and returns it as a String.

Notes:

start with the minimal failing solution
keep the three rules in mind and always write just sufficient enough code
do not forget to refactor your code after each passing test
write your assertions relating to the exact requirements
2. For multiples of three return “Fizz” instead of the number

3. For the multiples of five return “Buzz”

4. For numbers that are multiples of both three and five return “FizzBuzz”.
"""

def fizzbuzz(number: int) -> str:
    if is_fizzbuzz(number):
        return str('FizzBuzz')

    if is_fizz(number):
        return str('Fizz')

    if is_buzz(number):
        return str('Buzz')

    return str(number)


def is_fizzbuzz(number: int) -> bool:
    return is_fizz(number) and is_buzz(number)


def is_fizz(number: int) -> bool:
    if number % 3 == 0:
        return True
    return False


def is_buzz(number: int) -> bool:
    if number % 5 == 0:
        return True
    return False
