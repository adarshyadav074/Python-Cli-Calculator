def calculator():
    while True:
        operation = input("What do you want to do(Add, Sub, Mul, Divide, Power, Modulus): ").lower()
        a = int(input("Enter Number 1: "))
        b = int(input("Enter Number 2: "))

        if operation == "add":
            print(f"Addition of {a} and {b} is {a+b}.")

        elif operation == "sub":
            print(f"Subtraction of {b} from {a} is {a-b}.")

        elif operation == "mul":
            print(f"Multiplication of {a} and {b} is {a*b}")

        elif operation == "divide":
            if b == 0:   # 👈 sirf denominator check karo
                print("Cannot divide by zero ❌")
            else:
                print(f"Division of {a} by {b} is {a/b}")

        elif operation == "power":
            print(f"{a}^{b} = {a**b}")

        elif operation == "modulus":
            if b == 0:
                print("Cannot Modulus by 0.")
            else:
                print(f"{a} % {b} = {a%b}")
        else:
            print("Invalid Argument.")

        ce = input("Do you want to continue (yes/no): ").lower()
        if ce == "no":
            break

calculator()