string = input("Enter a list of numbers separated by spaces: ")
list = [int(x) for x in string.split()]
element = int(input("Enter the element to count: "))
count = list.count(element)
print(f"Number of times {element} occurs is {count}")
