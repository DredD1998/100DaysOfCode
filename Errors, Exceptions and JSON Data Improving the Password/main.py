# FileNotFoundError

# try:
#     file = open("password.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("password.txt","w")
#     file.write("Some passwords")
# except KeyError as error_message:
#     print(f"KeyError occurred: {error_message}")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File closed")
#     # print("End of program")
#     raise TypeError("This is a TypeError")




height = float(input("Enter your height in meters:"))
weight = float(input("Enter your weight in kilograms: "))
if height > 3:
    raise ValueError("Please insert a valid height")

bmi = weight / (height **2)
print(bmi)

 