num =int(input("Enter number of terms in the series: ")) 
a = 0
b = 1 
i = 3
list = [0, 1]

while (i <= num) : 
    c = a + b 
    list.append(c)
    a = b
    b = c 
    i = i + 1
    
if (num > 0):
    print("The Fibonnaci sequence is:")
    if (num == 1):
        list.pop()
    print(list)