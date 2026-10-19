import math
import random
import uuid
import time
import datetime
import string

def dir_operation():
    while True :
        print("Explore Module Attributes :")
        print("1. Math")
        print("2. UUID")
        print("3. Random")
        print("4. Time")
        print("5. Datetime")
        print("6. String")
        print("7. Back To Main Menu")

        try :
            choice = int(input("Enter Your Choice :- "))
        
        except :
            print("Enter Valid Number !")
            return
        if choice == 1:
            module = math
            name = "math"

        elif choice == 2:
            module = uuid
            name = "uuid"

        elif choice == 3:
            module = random
            name = "random"

        elif choice == 4:
            module = time
            name = "time"

        elif choice == 5:
            module = datetime
            name = "datetime"

        elif choice == 6:
            module = string
            name = "string"

        elif choice == 7 :
            break

        else:
            print("Invalid choice")
            return

        print()
        print(f"Attributes of  {name} : ")
        print(dir(module))


# dir_operation()