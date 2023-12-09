from pathlib import Path
import re
import math

#path = Path(__file__).with_name("day-five-input.txt")
path = Path(__file__).with_name("test.txt")
file = open(path)

data = file.read().split("\n\n")
almanac = dict()
value = None

cache = dict()

for line in data:
    (first, sec) = line.split(":")
    almanac[first.replace("\n", " ")] = sec.strip().split("\n")

almanac["seeds"] = re.findall(r"\d+\s+\d+", almanac["seeds"][0])

seeds = almanac["seeds"]

location = 0

def binary_search(low: int, high: int, target: int, destination: int, mapName: str):
	value = None

	while high > low:
		mid = math.floor(low + (high - low) / 2)
		

		a = target - low
		value = destination + a


		if target == mid:
			value = mid
			break
		elif target > mid:
			low = mid + 1
		else:
			high = mid
		
	return value

def get_map(map, target, mapName):
	value = int(target)

	for sequence in map:
		(destination, source, offset) = sequence.split()
		source = int(source)
		destination = int(destination)
		offset = int(offset)
		target = int(target)

		if target >= source + offset or target < source:
			continue

		data = binary_search(source, source + offset, target, destination, mapName)

		if data and data == target:
				a = target - source
				value = destination + a
			

	return value


for seed_range in seeds:
	(low, high) = seed_range.split(" ")
	low = int(low)
	high = low + int(high)
	
	for seed in range(int(low), int(high)):
		soil = almanac["seed-to-soil map"]
		fertilizer = almanac["soil-to-fertilizer map"]
		water = almanac["fertilizer-to-water map"]
		light = almanac["water-to-light map"]
		temperature = almanac["light-to-temperature map"]
		humidity = almanac["temperature-to-humidity map"]
		location = almanac["humidity-to-location map"]

		soil_map = get_map(soil, seed, "seed-to-soil map")
		fertilizer_map = get_map(fertilizer, soil_map, "soil-to-fertilizer map")
		water_map = get_map(water, fertilizer_map, "fertilizer-to-water map")
		light_map = get_map(light, water_map, "water-to-light map")
		temperature_map = get_map(temperature, light_map, "light-to-temperature map")
		humidity_map = get_map(humidity, temperature_map, "temperature-to-humidity map")
		location_map = get_map(location, humidity_map, "humidity-to-location map")

		if value is None:
			value = location_map
		elif location_map < value:
			value = location_map

print(value)
