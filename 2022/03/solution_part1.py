file = open("input.txt")
lines = file.readlines()

commons = []

priorities = 0

for line in lines:
    first_part = line[:len(line)//2]
    second_part = line[len(line)//2:]
    commons.append("".join(set(first_part) & set(second_part)))


for char in commons:
    if (char.isupper()):
        priorities += ord(char)-38
    else:
        priorities += ord(char)-96

print(commons)
print(priorities)
