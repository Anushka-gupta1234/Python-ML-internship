string= input("Enter the string")
file = open("TextFile.txt", "w")
file.write(string)
print("The string is written in the text file")