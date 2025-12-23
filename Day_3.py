

DATA: list[str] = []

def parse_file():
	with open("input_3.txt", "r") as f:
		for line in f.readlines():
			DATA.append(line.strip())

def part_one():
	result: int = 0
	for row in DATA:
		nums: list[str] = list(row) # get individual numbers as chars
		big = max(nums)
		idx = nums.index(big)
		if idx == len(nums)-1:
			# max throws an error with empry itterable
			res = max(nums[:idx]) + big
		else:
			# if index is 0 or somewhere in between, always pick the number on the right side
			res = big + max(nums[idx+1:])
		result += int(res)
	print(f"Part one {result=}")

def part_two():
	result: int = 0
	for row in DATA:
		nums: list[str] = list(row) # get individual numebrs as chars

	print(f"Part two {result=}")


if __name__ == "__main__":
	parse_file()
	part_one() # 17074
	part_two() # ???