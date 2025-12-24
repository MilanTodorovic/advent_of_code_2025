def parse_file():
	contents = []
	with open("input.txt", 'r') as f:
		for line in f.readlines():
			contents.append(line.strip())
	return contents


def part_one(input: list[str]):
	count = 0
	toilet_paper = '@'
	for i in range(0, len(input)):
		for j in range(0, len(input[0])):
			neighbors = 0
			if input[i][j] == toilet_paper:
				if i == 0:
					neighbors += 1 if input[i + 1][j] == toilet_paper else 0  # S
				elif i == len(input) - 1:
					neighbors += 1 if input[i - 1][j] == toilet_paper else 0  # N
				else:
					neighbors += 1 if input[i - 1][j] == toilet_paper else 0  # N
					neighbors += 1 if input[i + 1][j] == toilet_paper else 0  # S

				if j == 0:
					neighbors += 1 if input[i][j + 1] == toilet_paper else 0  # E
				elif j == len(input[0]) - 1:
					neighbors += 1 if input[i][j - 1] == toilet_paper else 0  # W
				else:
					neighbors += 1 if input[i][j + 1] == toilet_paper else 0  # E
					neighbors += 1 if input[i][j - 1] == toilet_paper else 0  # W

				if i == 0:
					if j == 0:
						neighbors += 1 if input[i + 1][j + 1] == toilet_paper else 0  # SE
					elif j == len(input[0]) - 1:
						neighbors += 1 if input[i + 1][j - 1] == toilet_paper else 0  # SW
					else:
						neighbors += 1 if input[i + 1][j + 1] == toilet_paper else 0  # SE
						neighbors += 1 if input[i + 1][j - 1] == toilet_paper else 0  # SW
				elif i == len(input) - 1:
					if j == 0:
						neighbors += 1 if input[i - 1][j + 1] == toilet_paper else 0  # NE
					elif j == len(input[0]) - 1:
						neighbors += 1 if input[i - 1][j - 1] == toilet_paper else 0  # NW
					else:
						neighbors += 1 if input[i - 1][j + 1] == toilet_paper else 0  # NE
						neighbors += 1 if input[i - 1][j - 1] == toilet_paper else 0  # NW
				else:
					if j == 0:
						neighbors += 1 if input[i + 1][j + 1] == toilet_paper else 0  # SE
						neighbors += 1 if input[i - 1][j + 1] == toilet_paper else 0  # NE
					elif j == len(input[0]) - 1:
						neighbors += 1 if input[i + 1][j - 1] == toilet_paper else 0  # SW
						neighbors += 1 if input[i - 1][j - 1] == toilet_paper else 0  # NW
					else:
						neighbors += 1 if input[i - 1][j + 1] == toilet_paper else 0  # NE
						neighbors += 1 if input[i - 1][j - 1] == toilet_paper else 0  # NW
						neighbors += 1 if input[i + 1][j + 1] == toilet_paper else 0  # SE
						neighbors += 1 if input[i + 1][j - 1] == toilet_paper else 0  # SW

				# neighbors += 1 if input[i - 1][j] == toilet_paper else 0  # N
				# neighbors += 1 if input[i + 1][j] == toilet_paper else 0  # S
				# neighbors += 1 if input[i][j + 1] == toilet_paper else 0  # E
				# neighbors += 1 if input[i][j - 1] == toilet_paper else 0  # W
				# neighbors += 1 if input[i - 1][j + 1] == toilet_paper else 0  # NE
				# neighbors += 1 if input[i - 1][j - 1] == toilet_paper else 0  # NW
				# neighbors += 1 if input[i + 1][j + 1] == toilet_paper else 0  # SE
				# neighbors += 1 if input[i + 1][j - 1] == toilet_paper else 0  # SW
				print(f"Toilet paper at {i},{j} has {neighbors} neighbors.")
				if neighbors < 4:
					count += 1
			else:
				pass
	print(f"Part One: {count}")

def part_two(input: list[str]):
	pass


if __name__ == "__main__":
	contents = parse_file()
	part_one(contents) # 1486
	part_two(contents)
