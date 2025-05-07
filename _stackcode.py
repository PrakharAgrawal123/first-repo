n=int(input("enter the size of the stack:"))

stack=[0]*n
top=-1

while True:
    print("\n1. Push\n2. Pop")
    choice = int(input("Enter your choice: "))
    if choice==1:
        if top==n-1:
            print("stack is overflow")
        else:
            value = int(input("Enter a value to push: "))
            top=top+1
            stack[top]=value
            print("Pushed:", value)
            print("Current stack:", stack[:top+1])
       
        
    elif choice==2:
        if top==-1:
            print("Stack is underflow")
        else:
            print("Poped:",stack[top])
            print("Current stack:", stack[:top])
            top-=1
    elif choice == 3:
         print("Exiting...")
         break

    else:
        print("Invalid choice. Try again.")
