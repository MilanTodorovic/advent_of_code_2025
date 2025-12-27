from itertools import combinations


def parse_file() -> list[tuple[int,int]]:
	file = "input_test.txt" if TEST_RUN else "input.txt"
	contents = []
	with open(file, 'r') as f:
		for line in f.readlines():
			contents.append(tuple([int(l) for l in line.strip().split(',')]))
	return contents

def part_one(contents: list[tuple[int,int]]):
	combs = combinations(contents, 2)
	max_area = 0
	for a, b in combs:
		m = (abs(a[0]-b[0])+1) * (abs(a[1] - b[1])+1)
		max_area = m if m > max_area else max_area
	print(f"Biggest rectangle area: {max_area}")

def part_two(contents: list[tuple[int,int]]):
	combs = combinations(contents, 2)
	max_area = 0


	print(f"Biggest rectangle area inside green tiles: {max_area}")


if __name__ == "__main__":
	TEST_RUN = True
	contents: list[tuple[int,int]] = parse_file()
	part_one(contents) # 4774877510
	part_two(contents) #
