file = open("input.txt")
lines = file.readlines()

pointsWin = 6
pointsDraw = 3

map_hand_enemy = {
    "A": "X",  # Sasso LOSE
    "B": "Y",  # Carta DRAW
    "C": "Z"  # Forbice WIN
}

default_point = {
    "A": 1,
    "B": 2,
    "C": 3,
}

win = {
    "A": default_point["B"],
    "B": default_point["C"],
    "C": default_point["A"]
}

lose = {
    "B": default_point["A"],
    "C": default_point["B"],
    "A": default_point["C"]
}

points = 0
for line in lines:
    enemy, me = line.split()
    if (me == "Y"):
        points += default_point[enemy] + pointsDraw
    if (me == "Z"):
        points += win[enemy] + pointsWin
    if (me == "X"):
        points += lose[enemy]

print(points)
