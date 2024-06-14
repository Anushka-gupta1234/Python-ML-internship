import string
str = input("Enter the string: ")
translator = str.maketrans('', '', string.punctuation)
print("Original string:", str)
print("String without punctuation:", str.translate(translator))