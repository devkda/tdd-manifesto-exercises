

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