print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L?: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y/N: ").lower()
extra_cheese = input("Do you want extra cheese? Y/N: ").lower()

bill = 0

if size == "s":
    bill = 15
    if pepperoni == "y":
        
        bill+=2
        
    if extra_cheese == "y":
        bill+=1
        print(f"Your total bill is ${bill}.00")
    else:
        print(f"Your total bill is ${bill}.00")

        
        

elif size == "m":
    bill = 20
    if pepperoni == "y":
        bill+=3
        
    if extra_cheese == "y":
        bill+=1
        print(f"Your total bill is ${bill}.00")
    else:
        print(f"Your total bill is ${bill}.00")
    

elif size == "l":
    bill = 30
    if pepperoni == "y":
        bill+=5
    if extra_cheese == "y":
        bill+=1
        print(f"Your total bill is ${bill}.00")
    else:
        print(f"Your total bill is ${bill}.00")


else:
    print("Invalid size selected.")
    exit()






# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, L?: ").lower()
# pepperoni = input("Do you want pepperoni on your pizza? Y/N: ").lower()
# extra_cheese = input("Do you want extra cheese? Y/N: ").lower()

# bill = 0

# if size == "s":
#     bill = 15
# elif size == "m":
#     bill = 20
# elif size == "l":
#     bill = 30
# else:
#     print("Invalid size selected.")
#     exit()
   


# if pepperoni == "y":
#     if size == "s":
#         bill += 2
#     else:
#         bill+=3
# if extra_cheese == "y":
#         bill += 1
 

# print(f"Your total bill is ${bill}.00")