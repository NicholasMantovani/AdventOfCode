class Elf():
    def __init__(self, max_calories, max_calories_elf):
        self.max_calories = max_calories
        self.max_calories_elf = max_calories_elf


file = open("input.txt")
lines = file.readlines()


calories_list = []
calories_count = 0
max_calories_elf = 0
max_calories = 0

for line in lines:
    if (line.strip()):
        calories_count += int(line.strip())
    else:
        calories_list.append(
            Elf(calories_count, max_calories_elf))
        calories_count = 0
        max_calories_elf += 1

calories_list.sort(key=lambda x: x.max_calories, reverse=True)

print('-------FIRST-------')
print('Max_calories: ' + str(calories_list[0].max_calories))
print('Max_calories_elf: ' + str(calories_list[0].max_calories_elf))

print('-------SECOND-------')
print('Max_calories: ' + str(calories_list[1].max_calories))
print('Max_calories_elf: ' + str(calories_list[1].max_calories_elf))

print('-------THIRD-------')
print('Max_calories: ' + str(calories_list[2].max_calories))
print('Max_calories_elf: ' + str(calories_list[2].max_calories_elf))


for i in range(0, 3):
    max_calories += calories_list[i].max_calories

print('-------TOTAL-----')
print('Max_calories_total: ' + str(max_calories))
