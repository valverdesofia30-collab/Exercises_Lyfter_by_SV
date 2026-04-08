
def is_prime(number):
    if number <= 1:
        return False
    
    for numbers in range(2, number):
        if number % numbers == 0:
            return False
        
    return True


def get_prime_numbers(numbers_list):
    prime_numbers = []

    for number in numbers_list:
        if is_prime(number):
            prime_numbers.append(number)

    return prime_numbers


print(get_prime_numbers([65, 2, 69, 51, 63, 12]))