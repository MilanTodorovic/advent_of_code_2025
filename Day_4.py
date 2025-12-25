def parse_file():
	contents = []
	with open("input.txt", 'r') as f:
		for line in f.readlines():
			contents.append(list(line.strip()))
	return contents


def part_one(puzzle_grid: list[list[str]]):
	count = 0
	toilet_paper = '@'
	for i in range(0, len(puzzle_grid)):
		for j in range(0, len(puzzle_grid[0])):
			neighbors = 0
			if puzzle_grid[i][j] == toilet_paper:
				if i == 0:
					neighbors += 1 if puzzle_grid[i + 1][j] == toilet_paper else 0  # S
				elif i == len(puzzle_grid) - 1:
					neighbors += 1 if puzzle_grid[i - 1][j] == toilet_paper else 0  # N
				else:
					neighbors += 1 if puzzle_grid[i - 1][j] == toilet_paper else 0  # N
					neighbors += 1 if puzzle_grid[i + 1][j] == toilet_paper else 0  # S

				if j == 0:
					neighbors += 1 if puzzle_grid[i][j + 1] == toilet_paper else 0  # E
				elif j == len(puzzle_grid[0]) - 1:
					neighbors += 1 if puzzle_grid[i][j - 1] == toilet_paper else 0  # W
				else:
					neighbors += 1 if puzzle_grid[i][j + 1] == toilet_paper else 0  # E
					neighbors += 1 if puzzle_grid[i][j - 1] == toilet_paper else 0  # W

				if i == 0:
					if j == 0:
						neighbors += 1 if puzzle_grid[i + 1][j + 1] == toilet_paper else 0  # SE
					elif j == len(puzzle_grid[0]) - 1:
						neighbors += 1 if puzzle_grid[i + 1][j - 1] == toilet_paper else 0  # SW
					else:
						neighbors += 1 if puzzle_grid[i + 1][j + 1] == toilet_paper else 0  # SE
						neighbors += 1 if puzzle_grid[i + 1][j - 1] == toilet_paper else 0  # SW
				elif i == len(puzzle_grid) - 1:
					if j == 0:
						neighbors += 1 if puzzle_grid[i - 1][j + 1] == toilet_paper else 0  # NE
					elif j == len(puzzle_grid[0]) - 1:
						neighbors += 1 if puzzle_grid[i - 1][j - 1] == toilet_paper else 0  # NW
					else:
						neighbors += 1 if puzzle_grid[i - 1][j + 1] == toilet_paper else 0  # NE
						neighbors += 1 if puzzle_grid[i - 1][j - 1] == toilet_paper else 0  # NW
				else:
					if j == 0:
						neighbors += 1 if puzzle_grid[i + 1][j + 1] == toilet_paper else 0  # SE
						neighbors += 1 if puzzle_grid[i - 1][j + 1] == toilet_paper else 0  # NE
					elif j == len(puzzle_grid[0]) - 1:
						neighbors += 1 if puzzle_grid[i + 1][j - 1] == toilet_paper else 0  # SW
						neighbors += 1 if puzzle_grid[i - 1][j - 1] == toilet_paper else 0  # NW
					else:
						neighbors += 1 if puzzle_grid[i - 1][j + 1] == toilet_paper else 0  # NE
						neighbors += 1 if puzzle_grid[i - 1][j - 1] == toilet_paper else 0  # NW
						neighbors += 1 if puzzle_grid[i + 1][j + 1] == toilet_paper else 0  # SE
						neighbors += 1 if puzzle_grid[i + 1][j - 1] == toilet_paper else 0  # SW
				# print(f"Toilet paper at {i},{j} has {neighbors} neighbors.")
				if neighbors < 4:
					count += 1
			else:
				pass
	print(f"Part One: {count}")

def part_two(puzzle_grid: list[list[str]]):
	count = 0
	toilet_paper = '@'
	old_count = 0
	while True:
		copy_of_puzzle_grid = puzzle_grid[::]
		for i in range(0, len(copy_of_puzzle_grid)):
			for j in range(0, len(copy_of_puzzle_grid[0])):
				neighbors = 0
				if copy_of_puzzle_grid[i][j] == toilet_paper:
					if i == 0:
						neighbors += 1 if copy_of_puzzle_grid[i + 1][j] == toilet_paper else 0  # S
					elif i == len(copy_of_puzzle_grid) - 1:
						neighbors += 1 if copy_of_puzzle_grid[i - 1][j] == toilet_paper else 0  # N
					else:
						neighbors += 1 if copy_of_puzzle_grid[i - 1][j] == toilet_paper else 0  # N
						neighbors += 1 if copy_of_puzzle_grid[i + 1][j] == toilet_paper else 0  # S

					if j == 0:
						neighbors += 1 if copy_of_puzzle_grid[i][j + 1] == toilet_paper else 0  # E
					elif j == len(copy_of_puzzle_grid[0]) - 1:
						neighbors += 1 if copy_of_puzzle_grid[i][j - 1] == toilet_paper else 0  # W
					else:
						neighbors += 1 if copy_of_puzzle_grid[i][j + 1] == toilet_paper else 0  # E
						neighbors += 1 if copy_of_puzzle_grid[i][j - 1] == toilet_paper else 0  # W

					if i == 0:
						if j == 0:
							neighbors += 1 if copy_of_puzzle_grid[i + 1][j + 1] == toilet_paper else 0  # SE
						elif j == len(copy_of_puzzle_grid[0]) - 1:
							neighbors += 1 if copy_of_puzzle_grid[i + 1][j - 1] == toilet_paper else 0  # SW
						else:
							neighbors += 1 if copy_of_puzzle_grid[i + 1][j + 1] == toilet_paper else 0  # SE
							neighbors += 1 if copy_of_puzzle_grid[i + 1][j - 1] == toilet_paper else 0  # SW
					elif i == len(copy_of_puzzle_grid) - 1:
						if j == 0:
							neighbors += 1 if copy_of_puzzle_grid[i - 1][j + 1] == toilet_paper else 0  # NE
						elif j == len(copy_of_puzzle_grid[0]) - 1:
							neighbors += 1 if copy_of_puzzle_grid[i - 1][j - 1] == toilet_paper else 0  # NW
						else:
							neighbors += 1 if copy_of_puzzle_grid[i - 1][j + 1] == toilet_paper else 0  # NE
							neighbors += 1 if copy_of_puzzle_grid[i - 1][j - 1] == toilet_paper else 0  # NW
					else:
						if j == 0:
							neighbors += 1 if copy_of_puzzle_grid[i + 1][j + 1] == toilet_paper else 0  # SE
							neighbors += 1 if copy_of_puzzle_grid[i - 1][j + 1] == toilet_paper else 0  # NE
						elif j == len(copy_of_puzzle_grid[0]) - 1:
							neighbors += 1 if copy_of_puzzle_grid[i + 1][j - 1] == toilet_paper else 0  # SW
							neighbors += 1 if copy_of_puzzle_grid[i - 1][j - 1] == toilet_paper else 0  # NW
						else:
							neighbors += 1 if copy_of_puzzle_grid[i - 1][j + 1] == toilet_paper else 0  # NE
							neighbors += 1 if copy_of_puzzle_grid[i - 1][j - 1] == toilet_paper else 0  # NW
							neighbors += 1 if copy_of_puzzle_grid[i + 1][j + 1] == toilet_paper else 0  # SE
							neighbors += 1 if copy_of_puzzle_grid[i + 1][j - 1] == toilet_paper else 0  # SW
					# print(f"Toilet paper at {i},{j} has {neighbors} neighbors.")
					if neighbors < 4:
						count += 1
						puzzle_grid[i][j] = "."
				else:
					pass
		if old_count < count:
			# if we removed one stack of toilet paper, then count will be greater than old_count
			old_count = count
		else:
			break
	print(f"Part Two: {count}")


if __name__ == "__main__":
	contents = parse_file()
	part_one(contents) # 1486
	part_two(contents) # 9024
