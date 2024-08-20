# Similar to JS array

#LIST
myList = [1,2,3]
print(myList)

# Slicing
print(myList[-1]) # 3
print(myList[0]) # 1
print(myList[2:]) # [3]
print(myList[2:4]) # [3]
print(myList[:3]) # [1,2,3]
print(myList[::2]) # [1,3]

# Reassignment --> Mutable
myList[2] = 5
print(myList)

# Append
myList.append("New Item")
print(myList) # [1, 2, 5, 'New Item']

myList.append([9,7,5])
print(myList) # [1, 2, 5, 'New Item', [9, 7, 5]]

myList.extend([12,44,23])
print(myList) # [1, 2, 5, 'New Item', [9, 7, 5], 12, 44, 23]

# POP
myList.pop()
print(myList) # [1, 2, 5, 'New Item', [9, 7, 5], 12, 44]

result = myList.pop(2)
print(myList) # [1, 2, 'New Item', [9, 7, 5], 12, 44]
print(result) # 5

# Nested List
NestedList = [1,2,[3,4,5]]
print(NestedList[2]) # [3,4,5]
print(NestedList[2][2]) # 5

# Matrix --> List Comprehnsion
matix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matix] # [1, 4, 7]
print(first_col)

#Reverse
newlist = ['h','e','l','l','o']
print(newlist[::-1])

