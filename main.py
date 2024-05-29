#This is a Simple Calculator Program
#Made By: Ahmed Hazem Elabady
#Date: 29/5/2024
work = True
print("Please Entre only one operator of these '+' or '-' or '*' or '/'")
print("For Ending the Program Please Enter 'exit'")
print("Please Enter the Equation: \n")

while work:
    line = input()
    if line == 'exit':
        print("Thank You For Using Our Program ❤️")
        work = False
        break
    for i in range(0, len(line)):
        if line[i] == '+' or line[i] == '-' or line[i] == '*' or line[i] == '/':
            num1 = int(line[:i])
            num2 = int(line[i+1:])
            if line[i] == '+':
                print(num1 + num2)
            elif line[i] == '-':
                print(num1 - num2)
            elif line[i] == '*':
                print(num1 * num2)
            elif line[i] == '/':
                print(num1 / num2)
            break