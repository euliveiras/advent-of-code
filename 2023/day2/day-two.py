from pathlib import Path
import re

path = Path(__file__).with_name("day-two-input.txt")
# path = Path(__file__).with_name("test.txt")
file = open(path)

colors = {"red": 12, "green": 13, "blue": 14}


def get_ball_data(ball):
    (_, num, color) = ball.split(" ")
    return (int(num), color)


def get_line_data(line):
    print(line)
    (_, values) = line.split(":")
    balls = values.replace(";", ",").split(",")
    data = dict(red=0, blue=0, green=0)

    for ball in balls:
        (num, color) = get_ball_data(ball)
        joinedKeys = " ".join(colors.keys())
        match = re.search(color, joinedKeys)

        if not match:
            continue

        match = match.group()
        isGreater = num > data[match]

        if isGreater:
            data[match] = num

    return data


def get_games_id_sum():
    sum = 0
    for line in file:
        minimun_balls_required = get_line_data(line.rstrip())
        sum += (minimun_balls_required["red"] *
                minimun_balls_required["green"] * minimun_balls_required["blue"])
    return sum


print("sum", get_games_id_sum())
