def to_uppercase(s):
    return s.upper()  # i have used this site as a refference : https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/string/upper/python-string-upper/#:~:text=To%20convert%20any%20character%20into,and%20returns%20a%20new%20string.

def to_lowercase(s):
    return s.lower()

if __name__ == "__main__":
    s = input("Enter the String: ")
    choice = int(input("Enter 1 for Upeer case or 2 for lower case: "))

    if choice == 1:
        Uppercasr_String = to_uppercase(s)
        print (f'The String in uppercas is : {Uppercasr_String}')
    elif choice == 2:
        Lowercase_String= to_lowercase(s)
        print (f'The String in lowercase is : {Lowercase_String}')

    else:
        print("Enter the correct choice.")

