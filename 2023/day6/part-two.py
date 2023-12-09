from pathlib import Path
import math
import re

path = Path(__file__).with_name("day-six-input.txt")
#path = Path(__file__).with_name("test.txt")
file = open(path)

(first, sec, _) = file.readlines()

time = int("".join(re.findall(r"\d+", first)))
distance = int("".join(re.findall(r"\d+", sec)))

jump_amount = math.floor(math.sqrt(time))

value1 = 1
value2 = 1

for i in range(value1, time):
	holding = i * 1
	remainder_time = time - holding
	if distance / holding <= remainder_time:
		value1 = i
		break

for i in range(time, value2, -1):
	holding = i * 1
	remainder_time = time - holding
	if distance / holding <= remainder_time:
		value2 = i
		break

print((max(value1, value2) - min(value1, value2)) + 1)
