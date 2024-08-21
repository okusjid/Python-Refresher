# Write a Python function to determine whether a given number is a prime number.
def isPrime(num):
	if num == 0 or num == 1:
		return "Not a prime number...!!"
	else:
		for i in range(2, num):
			if (num % i) == 0:
				return "Not a prime number...!!"
	return "Prime Number"


# print(isPrime(25))
# print('\n')
# print(isPrime(2))

# ------------------------------------------------------------------------------------
# Implement a Python script that calculates the factorial of a number using recursion.

def CalculateFac(num):
	if num == 1:
		return 1
	if num > 1:
		return num * CalculateFac(num - 1)


# print(CalculateFac(5)

# ------------------------------------------------------------------------------------
# Write a Python function that takes a string as input and returns a dictionary containing the frequency of each character in the string.

# myString = input("Please Enter: ")


def ProcessDictionary(myString):
	char_count = {}
	for char in myString:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count


# print(ProcessDictionary(myString))

# ------------------------------------------------------------------------------------
# Create a function that checks if a given string is a palindrome.
def Check_Palindrome(myStr):
    str_len = len(myStr)
    for i in range(0, str_len//2):
        if myStr[i] != myStr[str_len - i - 1]:
            return "Not a Palindrome"
    return "Palindrome"

print(Check_Palindrome("Hello"))
print(Check_Palindrome("olo"))