def is_palindrome(name):
    if name == name[::-1]:
        print("Word is palindrome")
    else:
        print('Word is not palindrome')


is_palindrome("asdfasdfasdf")
