#Prime factorization

#Requesting the limit 
def request_number():
    while True:
        response = input("Please add the number of sequences: ")
        if response.isdigit():
            return int(response)


#Fibonacci function 
def facto(numb):
    new_list = []

    for i in range(1, numb):
        divider = numb - i
        if numb % divider == 0 and divider > 1:
            new_list.append(divider)
    
    return new_list

request = request_number()
print(facto(request))



'''
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
 
for n in range(1, 6): # testing
    print(n, factorial_function(n))

'''
 
