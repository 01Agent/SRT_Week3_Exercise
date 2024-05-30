def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "undefined"
    else:
        return a/b
 
if __name__ == "__main__":

    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    sum= add(a,b)
    print(f'The sum of a & b is: {sum}')

    sub = subtract(a,b)
    print(f'The subtration of a & b is: {sub}')

    mul = multiply(a,b)
    print(f'The multiplication of a & b is: {mul}')

    div = divide(a,b)
    if div == "Undefined":
        print(div)
    else:
        print(f'The division of a & b is: {div}')