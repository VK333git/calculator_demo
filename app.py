from operations import *  ##* for importing all the functions and variables
def main():
    print("welcome to the calculator")
    print('''
        Select from the following operations:
          1. ADD
          2. SUBTRACT
          3. Multiply
''')
    user_i = input("Enter your choice : ")
    a = int(input('enter the first number: '))
    b = int(input('enter the second number: '))
    result = None

    if user_i == '1':
        result = do_sum(a,b)
    elif user_i == '2':
        result = do_sub(a,b)
    elif user_i == '3':
        result = do_mul(a,b)
    else:
        print('wrong operation entered')

    print(result)

if __name__ == '__main__':
    main()


    
    
