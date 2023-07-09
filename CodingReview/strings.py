''' Lets see how strings are stored in memory '''

s = "973"
print(bin(id(s)))
print(bin(id(s[0])))
print(bin(id(s[1])))
print(bin(id(s[2])))

'''
So, strings are stored as individual characters in a contiguous
memory location!
'''
'''
Remember: Slicing opertion is implemented using for loops so its not very efficient
The Time Complexity of this approach is  O(N) where  N is the length of the string to be reversed.
From: https://www.scaler.com/topics/reverse-string-in-python/
'''
def is_palindrome(str):
    r = str[::-1]  # O(N) Time Complexity
    if(str == r):
        return True
    return False
