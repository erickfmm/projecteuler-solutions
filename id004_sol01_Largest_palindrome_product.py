#A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):
    s = str(number)
    return s[::-1] == s

largest_palindrome = 0
all_palindromes = []
for i1 in range(999, 99, -1):
    for i2 in range(999, 99, -1):
        prod = i1 * i2
        if is_palindrome(prod):
            all_palindromes.append(prod)
            if prod > largest_palindrome:
                largest_palindrome = prod

print("largest palindrome: ", largest_palindrome)
print("#"*40)
print("all palindromes: ", all_palindromes)
print("#"*40)
print("#"*40)
print("largest palindrome: ", largest_palindrome)