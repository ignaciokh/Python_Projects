vowels = ['a','e','i','o','u']

def count_vowels(name, count=0):
    for i in list(name):
        if i in vowels:
            count += 1
    return count

print(count_vowels("abcba"))
