try:
    age = int(input("How old are you?: "))
    if age >= 18:
        print("You can vote.")
    else:
        print("You can't vote.")  
except Exception as e:
    print(f"An error occurred: {e}")
