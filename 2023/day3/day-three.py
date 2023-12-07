from pathlib import Path
import re
from typing_extensions import Match

path = Path(__file__).with_name("day-three-input.txt")
# path = Path(__file__).with_name("test.txt")
file = open(path)


def part_two():
    value = 0
    iterations = 0
    prev = ""
    nxt = ""

    lines = file.readlines()

    for line in lines:
        if iterations == len(lines) - 1:
            prev = lines[iterations - 1]
        elif iterations == 0:
            nxt = lines[iterations + 1]
        else:
            nxt = lines[iterations + 1]
            prev = lines[iterations - 1]

        prev_iter = re.finditer("\d+", prev)
        line_iter = (re.finditer("\d+", line))
        next_iter = (re.finditer("\d+", nxt))
        num_matches = list()

        for x in prev_iter:
            num_matches.append(x)

        for y in line_iter:
            num_matches.append(y)

        for z in next_iter:
            num_matches.append(z)

        gears_match = re.finditer("\*", line)

        for gear_match in gears_match:
            adjacencies = list()
            for num_match in num_matches:
                print(num_match, gear_match, "\n",  prev,  line, nxt)
                (num_start, num_end) = num_match.span()
                (gear_start, gear_end) = gear_match.span()
                if num_end < gear_start:
                    continue
                elif num_start > gear_end:
                    continue
                else:
                    print("true")
                    adjacencies.append(int(num_match.group()))
                    continue
            if len(adjacencies) == 2:
                print(adjacencies)
                value = value + adjacencies[0] * adjacencies[1]

            # print(prev, line, nxt, "value", value,  "\n")
        iterations += 1

    return value


def get_match(num: str, line: str):
    pattern = num
    matches = re.finditer(pattern, line.strip())
    for match in matches:
        if match.group() == num:
            return match


def get_line_data(line):
    return re.finditer(r"\d+", line)

   # if len(symbols) > 0:
   #     for symbol in symbols:
   #         symbol_match = get_match("\\" + symbol, line)
   #         if symbol_match:
   #             span = symbol_match.span()
   #             (index, _) = span
   #             line = line[:index] + "." + line[index+1:]
   #             symbol_matches.append(span)


def get_adjacencies(match: Match, prev: str, line: str, nxt: str):
    prev_adjacencies = ""
    nxt_adjacencies = ""
    pres = ""
    (start, end) = match.span()

    if start == 0:
        prev_adjacencies = prev[start:end + 1]
        nxt_adjacencies = nxt[start:end + 1]
        pres = line[start:end + 1]
    elif len(line) - 1 == end or len(nxt) - 1 == end or len(prev) - 1 == end:
        prev_adjacencies = prev[start - 1:end]
        nxt_adjacencies = nxt[start - 1:end]
        pres = line[start - 1: end]
    else:
        prev_adjacencies = prev[start - 1:end + 1]
        nxt_adjacencies = nxt[start - 1:end + 1]
        pres = line[start - 1:end + 1]

    # print("adjacencies", "prev", prev_adjacencies,
    #      "pres", pres, "nxt", nxt_adjacencies)
    symbol = re.search(
        r"([^\.|\d|\s])", prev_adjacencies + nxt_adjacencies + pres)

    if symbol:
        return int(match.group())
    else:
        return 0


def get_parts_sum():
    value = 0
    iterations = 0
    prev = ""
    nxt = ""

    lines = file.readlines()

    for line in lines:
        if iterations == len(lines) - 1:
            prev = lines[iterations - 1]
        elif iterations == 0:
            nxt = lines[iterations + 1]
        else:
            nxt = lines[iterations + 1]
            prev = lines[iterations - 1]
        print(prev, line, nxt, value, "\n")

        matches = get_line_data(line)
        for match in matches:
            value += get_adjacencies(match, prev,
                                     line, nxt)
            # print(prev, line, nxt, "value", value,  "\n")
        iterations += 1

    return value


# print(get_parts_sum())
print(part_two())
