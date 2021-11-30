

nlist=[]
n = int(input("enter the size of list: "))
for i in range(n):
    val = int(input("enter value: "))
    nlist.append(val)
print("list is : ",nlist)
def insert_sp(lst,item,pos,no):
    lst.append(None)
    print("length of array:",len(lst))
    for i in range(no-1,pos-2,-1): 
        lst[i+1]=lst[i]
    lst[pos-1]=item
    print("modified list", nlist)
insert_sp(nlist,
          int(input("enter a value to insert :")),
          int(input("enter the position :")),n)
