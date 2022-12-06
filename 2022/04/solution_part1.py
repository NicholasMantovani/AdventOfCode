file = open("input.txt")
lines = file.readlines()


def getArrayInRange(pair):
    output = []
    pair_splitted = pair.split("-")
    first_number = pair_splitted[0]
    second_number = pair_splitted[1]
    for i in range(int(first_number), int(second_number) + 1):
        output.append(i)
    return output


fully_contained = 0

for line in lines:
    pairs = line.split(",")
    first_pair = pairs[0]
    second_pair = pairs[1]
    first_pair_range = getArrayInRange(first_pair)
    second_pair_range = getArrayInRange(second_pair)
    len_pair_merged = len(set(first_pair_range) & set(second_pair_range))
    if (len_pair_merged == len(first_pair_range) or len_pair_merged == len(second_pair_range)):
        fully_contained += 1
        print(line)

print(fully_contained)
