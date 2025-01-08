print("Welcome to the rollercoaster ride!")
height = int(input("What is your height in cm?: "))
bill = 0
if height >= 121:
    age = int(input("Enter your age: "))
    print("You can ride the rollercoaster!.")
    if age >= 18:
        bill = 10
        print("Adult tickets price $10.00")
    elif age >=10:
        bill = 7
        print("Youth tickets price $7.00")

    else:
        bill = 5
        print("Child tickets price $5.00")

    photo = input("Do yo want photo? y/n: ")
    if photo == "y":
        bill += 3
        print(f"Your total bill is ${bill}.00.Thank you!")
    else:
        print("Thank you!")


    
else:
    print("You are not allowed to ride the rollercoaster.")