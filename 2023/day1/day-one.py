from pathlib import Path
import re

path = Path(__file__).with_name("day-one-input.txt")
#path = Path(__file__).with_name("test.txt")
file = open(path)

nums = {"one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

pattern = "|".join(list(nums.keys()))


def get_sum(string):
    num = ""
    for i in range(len(string)):
        if string[i].isdigit():
            word = re.findall(pattern, string[:i + 1])

            if len(word) > 0 and word[0] in nums:
                num = nums[word[0]]

            else:
                num = string[i]
            break
    word = ""
    for i in range(len(string) - 2, -1, -1):
        word += string[i:]
        word_match = re.search(pattern, word)
        if word_match and word_match.group() in nums:
            num += nums[word_match.group()]
            break

        elif string[i].isdigit():
            num += string[i]
            break

    return int(num)


def get_calibration_sum():
    sum = 0
    for line in file:
        print("sum before", sum)
        sum += get_sum(line)
        print("sum after", sum)

    return sum


print(get_calibration_sum())
