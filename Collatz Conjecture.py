#Prime factorization

#Requesting the limit 
def request_number():
    while True:
        response = input("Please add the number : ")
        if response.isdigit() and int(response) > 1:
            return int(response)



def prime_factors(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            steps += 1
        else:
            n = (n * 3) + 1
            steps += 1  
    return steps

request = request_number()
print(prime_factors(request))