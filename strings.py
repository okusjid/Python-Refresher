# String
myString = 'hello World!!'
print(myString)

# Slicing
print(myString[-1])
print(myString[0]) # H
print(myString[2:]) #llo World!!
print(myString[2:4]) #ll
print(myString[:3]) #Hel
print(myString[::2]) # --> Step Size

# Strings are immutable --> You cannot do myString[0] = 'X'

# Basic Method

x = myString.capitalize()
print(x)
y = x.upper() #--> It returns instead of updating in the original variable
print(y)

result = x.split('o')
print(result)

# Print formatting
X = "Item One: {} Item Two: {}".format("dog", "cat")
Y = "Item One: {x} Item Two: {x}".format(x="dog",y= "cat")

print(Y)