num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))

choice= int(input("Enter number choice 1/2/3/4: "))

if (choice==1):
    print("Sum is: ", num1+num2)
    
elif (choice==2):
    print("Difference is: ", num1 - num2)

elif (choice==3):
    print("Product is: ", num1*num2)

elif (choice==4):
    print("Division gives: ", num1/num2)

else:
    print("Please enter valid choice")