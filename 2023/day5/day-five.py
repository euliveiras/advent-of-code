from pathlib import Path

path = Path(__file__).with_name("day-five-input.txt")
#path = Path(__file__).with_name("test.txt")
file = open(path)

data = file.read().split("\n\n")
almanac = dict()
value = None

for line in data:
    (first, sec) = line.split(":")
    almanac[first.replace("\n", " ")] = sec.strip().split("\n")

almanac["seeds"] = almanac["seeds"][0].split(" ")

seeds = almanac["seeds"]

location = 0


def get_map(map, target):
	value = int(target)
	for sequence in map:
		(destination, source, offset) = sequence.split()
		source = int(source)
		destination = int(destination)
		offset = int(offset)
		target = int(target)

		if target >= source + offset or target < source:
			continue

		for x in range(source, source + offset):
			if x == target:
				a = target - source
				value = destination + a

	return value


for seed in seeds:
	soil = almanac["seed-to-soil map"]
	fertilizer = almanac["soil-to-fertilizer map"]
	water = almanac["fertilizer-to-water map"]
	light = almanac["water-to-light map"]
	temperature = almanac["light-to-temperature map"]
	humidity = almanac["temperature-to-humidity map"]
	location = almanac["humidity-to-location map"]

	soil_map = get_map(soil, seed)
	fertilizer_map = get_map(fertilizer, soil_map)
	water_map = get_map(water, fertilizer_map)
	light_map = get_map(light, water_map)
	temperature_map = get_map(temperature, light_map)
	humidity_map = get_map(humidity, temperature_map)
	location_map = get_map(location, humidity_map)

	if value is None:
		value = location_map
	elif location_map < value:
		value = location_map

print(value)
