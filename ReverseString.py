vowels = ['a','e','i', 'o', 'u']

def count_vowels(name):
    return "".join(reversed(name))
    #Alternatively we can also use 
    #return name[::-1]
    
print(count_vowels("abuberhvbahsuvbdhjvfahuisdvyui"))