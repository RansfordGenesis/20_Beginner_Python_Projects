def add(a, b):
    answer = a + b
    print(answer)
    
def sub(a, b):
    answer = a - b
    print(answer)
    
def mul(a, b):
    answer = a * b
    print(answer)
    
def div(a, b):
    answer = a / b
    print(answer)

print("Welcome to my simple Calculator\n")
print("\n A. Addition\n B. Subtraction\n C. Multiplication\n D. Division\n E. Quit\n")

choice = input("Input your choice: ")

if choice.upper() == 'A':
    print("Addition")
    a = int(input("Input first integer: "))
    b = int(input("Input second integer: "))
    add(a, b)

elif choice.upper() == 'B':
    print("Subtraction")
    a = int(input("Input first integer: "))
    b = int(input("Input second integer: "))
    sub(a, b)

elif choice.upper() == 'C':
    print("Multiplication")
    a = int(input("Input first integer: "))
    b = int(input("Input second integer: "))
    mul(a, b)
    
elif choice.upper() == 'D':
    print("Division")
    a = int(input("Input first integer: "))
    b = int(input("Input second integer: "))
    div(a, b)
    
elif choice.upper() == 'E':
    print("Thank You for trying my Calculator")
    quit()