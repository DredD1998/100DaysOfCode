import random

def calculate_discount(price, discount):
    final_price = price - price * discount
    return final_priice  # Error: Typo in variable name

def get_random_number():
    return random.randint(0, 100)  # This is fine, but let's pretend it has an issue

def greet_person(person_name):
    greeting = "Hi " + person_name  # Error: What if person_name is None?
    return greeting

def divide_numbers(a, b):
    return a / b  # Error: Will fail if b is 0

def find_smallest_number(numbers):
    smallest = min(numbers)  # Error: min(numbers) will fail if numbers is an empty list
    return smallest

def main():
    print("Calculating discount...")
    print(calculate_discount(200, 0.1))  # Error: This will not work because of a typo in final_priice
    
    print("Getting random number...")
    print(get_random_number())  # Assume this is fine for now
    
    print("Greeting person...")
    print(greet_person(None))  # Error: Will raise TypeError when None is passed
    
    print("Dividing numbers...")
    print(divide_numbers(10, 0))  # Error: ZeroDivisionError
    
    print("Finding smallest number...")
    print(find_smallest_number([]))  # Error: Will raise ValueError if the list is empty

if __name__ == "__main__":
    main()



