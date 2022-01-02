#3. Write a Python program to get the largest and the smallest number from a list.


list=[10,20,30,80,8]
elmt = list[ 0 ]
elmt2 = list[ 0 ]
for a in list:
    if a < elmt:
            elmt = a
for b in list:
    if  b > elmt2:
            elmt2 = b               
print("smallest element is : ",elmt)
print("maximum element is : ",elmt2)