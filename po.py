def fizzbuzz(n):
    """Retorna:
    - 'Fizz' se n divisível por 3 e não por 5
    - 'Buzz' se n divisível por 5 e não por 3
    - 'FizzBuzz' se n divisível por 3 e por 5
    - o próprio número caso contrário
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    if n % 5 == 0 and n % 3 != 0:
        return "Buzz"
    return n