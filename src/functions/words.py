import string

def alphabetDict():
    d ={}
    for index, letter in enumerate(string.ascii_lowercase):
        d[letter] = index + 1
    return d

# Takes a string, return true iff it's a palindrome
def isPalindrome(s):
    for i in range(int(len(s)/2)):
        if s[i] != s[-(i + 1)]:
            return False
    return True
