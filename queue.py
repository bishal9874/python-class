a=[]
front=rear=None
def insert(a, val):
    a.append(val)
    if len(a)==1:
        front=rear=0
    else:
        rear=len(a)-1
def dequeue(a):
    x= a.pop(0)
    print("Deque item = ", x) 
    if len(a)==0:
        front = rear=None    
def display(a):
    for i in range(len(a)):
        print(a[i])               
while 1:
    ch = int(input("1.Insert\n2.Delete \n3.Display \n4.exit \nEnter your Choice: "))
    if(ch == 1):
        val =int(input("Enter the value in Queue: "))
        insert(a,val)
    elif(ch== 2):
         if len(a)==0:
             print("Queue is empty")
         else:
             dequeue(a)
    elif ch == 3: 
           if len(a)==0:
             print("Queue is empty")
           else:
            display(a)
    else:
         break             
    

    