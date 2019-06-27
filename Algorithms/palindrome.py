# Palindrome is a word spelled the same backwards as forwards

def palindrome(word):
    word = word.lower()
    # [::-1] is python's syntax for returning a slice of an entire iterable in reverse
    return word[::-1] == word

print(palindrome("Mother"))
print(palindrome("Mom"))

