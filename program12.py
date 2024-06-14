number = int(input("Enter number: "))
sum=0
rem=0
while(number!=0):
    rem = number % 10
    sum = sum + rem
    number = number // 10
print("Sum of digits is: ",sum)
    