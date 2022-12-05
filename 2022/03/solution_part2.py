file = open("input.txt")
lines = file.readlines()

commons = []

priorities = 0


i = 0
while (i < len(lines)):
    commons.append("".join(set(lines[i].replace("\n", "")) & set(
        lines[i+1].replace("\n", "")) & set(lines[i+2].replace("\n", ""))))
    i += 3

print(commons)
for char in commons:
    if (char.isupper()):
        priorities += ord(char)-38
    else:
        priorities += ord(char)-96


print(priorities)
