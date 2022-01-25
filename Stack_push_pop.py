
a=[]
def push(a, val):        
       a.append(val)
       print("element insert Successfully!!")
def popelement(a):
    val = a.pop()
    print("element poped item = ", val)  
                  
def display(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i])
        
while 1:
     choice = int(input("1. Push \n 2. Pop \n 3. Display \n 4. Exit \n Enter Your Choice: "))
     if(choice == 1):
        val =int(input("Enter the No. to Push: "))
        push(a, val)
     elif(choice == 2):
         if len(a)==0:
             print("stack is empty")
         else:
             popelement(a)
     elif choice == 3: 
           if len(a)==0:
             print("stack is empty")
           else:
             
             display(a)
     else:
         break               
                 



