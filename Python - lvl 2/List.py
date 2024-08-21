original_list = [1, 2, 3, [4, 5, 6]]

clone_list = original_list.copy()
print(clone_list)

clone_list[3][1] = 9
print("Clone List", clone_list)
print("Original List", original_list)

clone_list[2] = 1122
print("Clone List", clone_list)
print("Original List", original_list)

clone_list[3] = "Hello"
print("Clone List", clone_list)
print("Original List", original_list)
