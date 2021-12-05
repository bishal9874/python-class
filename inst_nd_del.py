
lst=[]
lst_size= int(input("enter the size of list: "))
def list_entries(nlist,n):
    for i in range(n):
        val= int(input("enter value: "))
        nlist.append(val)
    print("list is : ",nlist)
    
    print("1. If you want to insert element")
    print("2. If you want del element")
    print("3. Exit")
    choice_want(int(input("Enter your Choice: ")))
    
# choice case   

def choice_want(choi):
    if(choi==1):
        insert_sp(lst,
          int(input("enter a value to insert :")),
          int(input("enter the position :")),lst_size),""
    elif(choi==2):
        del_element(lst,int(input("enter the element to delete from list: ")),lst_size)
    elif(choi==3):
        exit
    else:
        print("invaild entry")
        
# insert element in a list 
   
def insert_sp(lst,item,pos,no):
    lst.append(None)
    print("length of array:",len(lst))
    for i in range(no-1,pos-2,-1): 
        lst[i+1]=lst[i]
    lst[pos-1]=item
    print("modified list", lst)
    
# delete element from a list

def del_element(lis,key,sze):
    for i in range(sze):
        if(lis[i]==key):
            print("element present in this list \n******________ Successfully passed________******")
            pos=i
            for i in range(pos,sze-1):
                lis[i]=lis[i+1]
            lis.pop(sze-1)
            print(key,"element del from ",i,"th position")
            print("modifed list: ",lis)
            break
    else:
        print("enter element not found in list")

list_entries(lst,lst_size)
