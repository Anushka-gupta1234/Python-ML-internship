string = input("Enter a list of numbers separated by spaces: ")
numbers_string = string.split()
list= []
for i in numbers_string:
    list.append(int(i))
sum = 0
for number in list:
    sum += number
print("The sum of the list is: ", sum)
