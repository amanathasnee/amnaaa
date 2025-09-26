lst=[]
while True:
    print("\n 1.Add 2.View 3.Exit")
    choice=input("enter your choice:")
    print(choice)

    if choice=="1":
        item=input("enter the thing to append: ")
        lst.append(item)
        print("item added")
    elif choice=="2":
        print("current list is:",lst)
    elif choice=="3":
        print("exitif the program!")
        break
    else:
        print("invalid choice")


