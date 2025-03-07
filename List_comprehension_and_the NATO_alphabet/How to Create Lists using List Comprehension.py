numbers = [1,2,3,4,5]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Hirak"
letters_list = [letter for letter in name]
print(letters_list)



double_numbers = [ numbers * 2 for numbers in range(1,5) ]
print(double_numbers)


name = ["Hirak", "Supriya", "Priyanka", "Dhruv"]

new_list = [item.upper() for item in name if len(item) < 6]
print(new_list)


