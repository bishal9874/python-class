lst=[1,5,9,7,6,3]
length=len(lst)
element=int(input("Enter element to be searched for:"))
for i in range(0,length):
      if element==lst[i]:
            print(element,"found at index",i)
            break
else:
      print(element,"not found in given list")