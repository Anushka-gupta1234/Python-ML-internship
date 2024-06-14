n=int(input("Enter number: "))
temp = n
fact = 1
while (temp > 0):
    fact = fact * temp
    temp = temp - 1
print ("Factorial: ", fact)