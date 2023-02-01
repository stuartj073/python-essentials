## prime factors

def get_prime_factors(number):
    factors = []
    diviser = 2
    while diviser <= number:
        if number % diviser == 0:
            factors.append(diviser)
            number = number // diviser
        else:
            diviser += 1
    return factors


print(get_prime_factors(11))