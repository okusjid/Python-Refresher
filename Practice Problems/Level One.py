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
	for i in range(0, str_len // 2):
		if myStr[i] != myStr[str_len - i - 1]:
			return "Not a Palindrome"
	return "Palindrome"


# print(Check_Palindrome("olo"))
# print(Check_Palindrome("Hello"))

#--------------------------------------------------------------------------------------

# Lists:
# Write a function that accepts a list of integers and returns the maximum and minimum values in the list.
def Max_Min(my_list):
	
	length = len(my_list)
	if length == 0:
		print("List is empty...!!")
		return None, None
	min_ele = my_list[length - 1]
	max_ele = my_list[length - 1]
	for item in my_list:
		if item < min_ele:
			min_ele = item
		if item > max_ele:
			max_ele = item
	return min_ele, max_ele


mylist = []
min_val, max_val = Max_Min(mylist)
# print("Minimum: ", min_val, "Maximum: ", max_val)

# Create a Python program to remove duplicates from a list while preserving the order of elements.


'''
Dictionaries:
Write a Python program that merges two dictionaries into one, combining values for keys that appear in both dictionaries.
Implement a phonebook using a dictionary where the key is the contact’s name and the value is the phone number.
Tuples, Sets, and Booleans:

Write a Python function that accepts a tuple of numbers and returns a tuple with only the unique values.
Create a Python program that checks if two sets are disjoint (i.e., have no common elements).
Control Flow:

Implement a Python program that simulates a basic ATM system. The program should allow users to deposit, withdraw, and check their balance.
Write a Python program that prints all numbers from 1 to 100, replacing multiples of 3 with "Fizz," multiples of 5 with "Buzz," and multiples of both with "FizzBuzz."
Functions:

Write a Python function that accepts a list of numbers and returns a new list with each number squared.
Create a function that takes a list of strings and returns a single string where all the strings are concatenated with a space between them.
Level Two Practice Questions:
Scope:

Write a Python function that demonstrates the difference between local and global scope.
Create a program that uses nested functions and showcases the nonlocal keyword.
Object-Oriented Programming (OOP):

Define a class BankAccount that has attributes balance and account_number. Include methods to deposit, withdraw, and check the balance.
Create a class Car with attributes like make, model, and year. Add methods to start the car, stop the car, and print out the car’s details.
Errors and Exceptions:

Write a Python program that handles division by zero using a try-except block.
Create a program that raises a custom exception if a user inputs a negative number where only positive numbers are expected.
Regular Expressions:

Write a Python function that takes a string and validates whether it is a properly formatted email address.
Implement a script that extracts all phone numbers from a given text file using regular expressions.
Modules and Packages:

Create a Python package for a simple calculator with modules for addition, subtraction, multiplication, and division.
Write a Python script that uses the os module to list all files and directories in a specified directory.
Decorators:

Write a decorator that times the execution of a function.
Create a decorator that logs the arguments and return values of a function each time it is called.

'''
