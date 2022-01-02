
#6. Write a Python program to remove duplicates from a list.


def Remove(duplicate):
	list = []
	for num in duplicate:
		if num not in list:
			list.append(num)
	return list
	
duplicate = [2, 4, 10, 20, 5, 2, 20, 4,20,5,21]
print(Remove(duplicate))
