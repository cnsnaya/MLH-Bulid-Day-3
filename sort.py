def dictionairy():
    key_value = {}
    n = int(input("Enter the number of folders:"))

    for i in range (n) :
        number=int(input("Enter the folder number:"))
        key_value[number]=int(input("Enter the number of files in it:"))
    print("\nWhat do you want to see?")
    print("1.Sorted according to the Folder Numbers")
    print("2.Sorted according to the number of files in the folder")
    choice=int(input())
    print("\nNow it will show the folder's number first then the number of files in it")
    if choice == 1:
       
        for i in sorted(key_value):
            print((i, key_value[i]), end=" ")
        print("\nRequest Completed!")

    elif choice == 2:

        print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))
        print("\nRequest Completed!")
    else:
        print("Wrong Input! TRY AGAIN!")

if __name__ == "__main__":
    dictionairy()
