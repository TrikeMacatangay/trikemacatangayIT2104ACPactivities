def isPalindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

num = int(input("Enter an integer: "))
if isPalindrome(num):
    print("Palindrome")
else:
    print("Not a Palindrome")