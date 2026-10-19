from package import math_Opration
from package import date_time
from package import random_Opration
from package import uniqu_id
from package import file_opration
from package import dir_operation
 
def main():
    while True :
        print("============================")
        print("Welcome to Multi-Utility Toolkit ")
        print("============================")
        print("Choose an option :")
        print("1. Date-Time and Time Opration")
        print("2. Mathematical Opration")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Opration (Custom Module)")
        print("6. Explore Module Attributes (dur()) ")
        print("7. Exit ")
        print("============================")

        choice = int(input("Enter Your Choice :- "))
        print()
        
        if choice == 1 :
            date_time()

        elif choice == 2 :
            math_Opration()

        elif choice == 3 :
            random_Opration()

        elif choice == 4 :
            uniqu_id()

        elif choice == 5 :
            file_opration()

        elif choice == 6 :
            dir_operation()

        elif choice == 7 :
            print("Thank You For Using Multi-Utility Toolkit !")
            print("GoodBye!")
            break

 
if __name__ == "__main__" :
    main()