DATA: list[str] = []
DIGITS = 12

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

def find_max(s: str, p_idx: int):
	global DIGITS

	print(f"\tSubstring {s:1} and {p_idx=}.")

	if len(s)-1 <= 0:
		return []
	else:
		big = max(s)
		_idx = s.index(big)
		DIGITS -= 1
		
		if DIGITS == 0:
			return [p_idx+_idx]

		tail = len(s[_idx+1:])
		if tail == DIGITS:
			# return indecis for all the numbers to the right including the big
			# if there are no numbers on the right, returns just the big -> range(6, 6+0+1) -> [6]
			return [p_idx+i for i in range(_idx, _idx+tail+1)]
		elif tail > DIGITS:
			return [p_idx+_idx] + find_max(s[_idx+1:], p_idx+_idx)
		else:
			# not enough digits on the right side, must supplement from the left
			return [p_idx+_idx] + find_max(s[p_idx+_idx+1:], p_idx+_idx) + find_max(s[:_idx], p_idx)

def part_two():
	global DIGITS

	result: int = 0
	for row in DATA:
		DIGITS = 12
		print("Starting number:", row)
		res: list[int] = find_max(row, 0)
		res.sort()
		print(f"Final {res=} |", row, " -> ", "".join(row[i] for i in res), "\n")
		

	print(f"Part two {result=}")


if __name__ == "__main__":
	parse_file()
	part_one() # 17074

	part_two() # ???
