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