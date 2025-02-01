import logo




def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2


operations = {

    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}
def calculator():
    print(logo.logo)
    calculation_continue = True
    num1 = float(input("Enter your number: "))
    while calculation_continue:

        for symble in operations:
            print(symble)

        operation_symble = input("Pick an operation: ")
        num2 = float(input("Enter your next number: "))
        answer = operations[operation_symble](num1,num2)
        print(f"{num1} {operation_symble} {num2} = {answer}")

        choice = input(f'Type "y" to continue calculating with {answer} , or type "n" to start a new calculation: ')    

        if choice == "y":
            num1 = answer
        else:
            calculation_continue = False
            print(f"Your answer is {answer}")
            calculator()
        
 
calculator()