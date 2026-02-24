#Prime factorization

#Requesting the limit 
def request_number():
    while True:
        response = input("Please add the number of sequences: ")
        if response.isdigit():
            return int(response)



def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1

    return factors


request = request_number()
print(prime_factors(request))
