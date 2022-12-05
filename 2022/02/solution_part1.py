file = open("input.txt")
lines = file.readlines()

pointsWin = 6
pointsDraw = 3

map_hand_enemy = {
    "A": "X",  # Sasso
    "B": "Y",  # Carta
    "C": "Z"  # Forbice
}

default_point = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

win_outcome = ["XZ", "YX", "ZY"]

points = 0
for line in lines:
    enemy, me = line.split()
    points += default_point[me]
    if (me == map_hand_enemy[enemy]):
        points += pointsDraw
    if (me+map_hand_enemy[enemy]) in win_outcome:
        points += pointsWin

print(points)
