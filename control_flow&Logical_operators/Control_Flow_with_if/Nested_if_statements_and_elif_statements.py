print("Welcome to the rollercoaster ride!")
height = int(input("What is your height in cm?: "))
if height >= 121:
    age = int(input("Enter your age: "))
    print("You can ride the rollercoaster!.")
    if age >= 18:
        print("Adult tickets price $10.00")
    elif age >=10:
        print("Youth tickets price $7.00")

    else:
        print("Child tickets price $5.00")
else:
    print("You are not allowed to ride the rollercoaster.")

