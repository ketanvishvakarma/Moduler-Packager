def file_opration() :
    while True :
        print("File Operations :")
        print("1. Create a new File")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Append to a File")
        print("5. Back to Main Menu")
        print()

        choice = int(input("Enter Your Choice :- "))

        if choice == 1:
            name = input("Enter File Name(.txt .pdf .png...) :- ")
            with open(name, "x") as file:
                print("File created successfully")

        elif choice == 2:
            name = input("Enter File Name(.txt .pdf .png...) :- ")
            with open(name, "w") as file:
                text = input("Enter text to write :- ")
                file.write(text)
                print("Text written successfully")

        elif choice == 3:
            name = input("Enter File Name(.txt .pdf .png...) :- ")
            with open(name, "r") as file:
                content = file.read()
                print(content)
                
        elif choice == 4:
            name = input("Enter File Name(.txt .pdf .png...) :- ")
            keyword = input("Enter keyword to search :- ")
            new_line = input("Enter new line :- ")

            with open(name, "r") as file:
                lines = file.readlines()

            for i in range(len(lines)):
                if keyword in lines[i]:
                    lines[i] = new_line + "\n"
                    break

            with open(name, "w") as file:
                file.writelines(lines)

            print("Line modified successfully")

        elif choice == 5:
            print("Back to Main Menu")    
            break

        else:
            print("Enter Valid choice ! ")

 