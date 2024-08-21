# Write a function to split the restaurant bill among friends.
#
# Take the subtotal of the bill and the number of friends as inputs.
# Calculate the total bill by adding 20% tax to the subtotal and then divide it by the number of friends.
# Return the amount each friend has to pay, rounded off to two decimal places.

SubTotal = int(input("Give Sub Total of Bill: "))
NoOfFriends = int(input("Total Friends: "))

Total = SubTotal + (0.20 * SubTotal)
SplittedBill = Total / NoOfFriends
print("Total: ", Total)
print("Splitted Bill: ", SplittedBill.__round__(2) )
