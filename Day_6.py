def parse_file() -> list[str]:
	# TODO needs rework to function with the second part
	contents = []
	with open("input.txt", 'r') as f:
		for line in f.readlines():
			contents.append([l.strip() for l in line.split()])
	return contents

def part_one(contents: list[str]):
	total = 0
	i = 0
	for op in contents[4]:
		if op == "*":
			total += int(contents[0][i]) * int(contents[1][i]) * int(contents[2][i]) * int(contents[3][i])
		else:
			total += int(contents[0][i]) + int(contents[1][i]) + int(contents[2][i]) + int(contents[3][i])
		i += 1
	print("Part One:", total)

def part_two(contents: list[str]):
	total = 0
	i = 0
  # TODO get space between * and + -1 to get the width of the largest number
	print("Part Two:", total)

if __name__ == '__main__':
	contents = parse_file()
	part_one(contents) # 5227286044585
	part_two(contents)
