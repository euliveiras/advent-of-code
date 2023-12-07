from pathlib import Path
import re

path = Path(__file__).with_name("day-four-input.txt")
#path = Path(__file__).with_name("test.txt")
file = open(path)

first_sol = 0
sec_sol = 0

# 25571
dict_matches = dict()


def get_matches(line, pattern=r"\d+"):
    return re.finditer(pattern, line)


for line in file:
    card_total = 0
    (first_part, my_numbers) = line.split("|")
    (game_label, winning_numbers) = first_part.split(":")
    id = re.search(r"\d+", game_label)
    game_id = 0

    if id:
        game_id = int(id.group())
        if game_id not in dict_matches.keys():
            dict_matches[game_id] = dict()

    winning_matches = get_matches(winning_numbers)
    my_numbers_matches = get_matches(my_numbers)

    dict_matches[game_id]["winning_numbers"] = winning_numbers.split()

    dict_matches[game_id]["matches"] = list()

    value = 0

    for match in my_numbers_matches:
        if match.group() in dict_matches[game_id]["winning_numbers"]:
            if value == 0:
                value += 1
            else:
                value *= 2
            if match.group() not in dict_matches[game_id]["matches"]:
                dict_matches[game_id]["matches"].append(match.group())

    dict_matches[game_id]["total"] = value

    if "copies" not in dict_matches[game_id]:
        dict_matches[game_id]["copies"] = 1

    for _ in range(int(dict_matches[game_id]["copies"])):
        for i in range(1, len(dict_matches[game_id]["matches"]) + 1):
            key = game_id + i
            if key not in dict_matches.keys():
                dict_matches[key] = dict(copies=1)

            dict_matches[key]["copies"] += 1



for key in dict_matches.keys():
	first_sol += dict_matches[key]["total"]
	sec_sol +=  dict_matches[key]["copies"]

print("first solution", first_sol)
print("sec solution", sec_sol)
