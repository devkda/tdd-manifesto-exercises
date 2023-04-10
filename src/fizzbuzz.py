

def fizzbuzz(number):

    if number % 3 == 0 and number % 5 == 0:
        return str('FizzBuzz')

    if number % 3 == 0:
        return str('Fizz')

    if number % 5 == 0:
        return str('Buzz')

    return str(number)
