from pathlib import Path
import re

path = Path(__file__).with_name("day-six-input.txt")
#path = Path(__file__).with_name("test.txt")
file = open(path)

(first, sec, _) = file.readlines()

times = re.findall(r"\d+", first) 
distances = re.findall(r"\d+", sec)

number_of_races = len(times)

value = 1

for number in range(number_of_races):
	time = int(times[number])
	distance = int(distances[number])

	solutions = 0
	for i in range(1, time + 1):
		holding = i * 1
		remainder_time = time - holding
		if distance / holding >= remainder_time:
			continue
		else:
			solutions += 1

	value *= solutions
		
print(value)
