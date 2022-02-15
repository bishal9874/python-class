#. Write a Python program to multiply all the items in a list.
def multiplyList(myList) :
	result = 1
	for x in myList:
		result = result * x
	return result
list1 = [1, 2, 3,5,6]
print("multiple of list",multiplyList(list1))

