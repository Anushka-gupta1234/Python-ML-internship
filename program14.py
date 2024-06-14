lines = []
print("Enter multiple lines of input. Press Enter on an empty line to stop.")
while True:
    line = input()
    if not line:
        break
    lines.append(line)

print("\nLines entered by the user:")
for line in lines:
    print(line)