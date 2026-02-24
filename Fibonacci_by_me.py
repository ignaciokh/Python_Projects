#Fibonacci Sequence 

#Requesting the limit 
def req_limit():
    while True:
        response = input("Please add the number of sequences: ")
        if response.isdigit():
            return int(response)


#Fibonacci function 
def fibo(numb):
    if numb < 1:
        return None
    if numb < 3:
        return 1
    
    a, b = 0, 1
    new_list = [a,b]
    # Sinde the counte wont be used we can just incluse _
    for _ in range(numb):
        a,b = b, a+b    # not necesary the use of other variable to store one value
        new_list.append(b)
    
    return new_list

request = req_limit()
print(fibo(request))



'''
Alternative 

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
 
for n in range(1, 10): # testing
    print(n, "->", fib(n))
    
    
'''