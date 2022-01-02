#Write a Python program to sum all the item
total = 0

# creating a list
list1 = [11, 5, 17, 18, 23,20,23,50,40]

for ele in range(0, len(list1)):
	total = total + list1[ele]

# printing total value
print("Sum of all elements in given list: ", total)
