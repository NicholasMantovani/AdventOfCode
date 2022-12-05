file = open("input.txt")
lines = file.readlines()

max_calories = 0
calories_count = 0
max_calories_elf = 0

for line in lines:
    if (line.strip()):
        calories_count += int(line.strip())
    else:
        if (max_calories < calories_count):
            max_calories = calories_count
        calories_count = 0
        max_calories_elf += 1

"""
for veryfing the result

for i in range(len(lines)):
    if (lines[i].strip()):
        calories_count += int(lines[i].strip())
    else:
        if (max_calories < calories_count):
            max_calories = calories_count
            print(i)
        calories_count = 0
        max_calories_elf += 1
"""


print('Max_calories: ' + str(max_calories))
print('Max_calories_elf: ' + str(max_calories_elf))
