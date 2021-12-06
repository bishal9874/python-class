
total = 0

lst=[]
lst_size= int(input("enter the size of list: "))


def list_entries(nlist,n):
    for i in range(n):
        val= int(input("enter value: "))
        nlist.append(val)
    print("list is : ",nlist)
    
list_entries(lst,lst_size)  
  
for ele in range(0, len(lst)):
	total = total + lst[ele]
print("Sum of all elements in given list: ", total)
