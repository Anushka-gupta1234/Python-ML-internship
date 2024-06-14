frequency = {}
string = input("Enter the string: ")
for i in string:
	if i in frequency:
		frequency[i] += 1
	else:
		frequency[i] = 1
for char, count in frequency.items():
    print("Character: '{char}' | Frequency: {count}")

