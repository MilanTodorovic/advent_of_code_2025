DATA: list[str] = []
DIGITS = 12


def parse_file():
	with open("input.txt", "r") as f:
		for line in f.readlines():
			DATA.append(line.strip())

def part_one():
	result: int = 0
	for row in DATA:
		nums: list[str] = list(row)  # get individual numbers as chars
		big = max(nums)
		idx = nums.index(big)
		if idx == len(nums) - 1:
			# max throws an error with empry itterable
			res = max(nums[:idx]) + big
		else:
			# if index is 0 or somewhere in between, always pick the number on the right side
			res = big + max(nums[idx + 1:])
		result += int(res)
	print(f"Part one {result=}")

def find_max(s: str, c_idx: int, side: str):
	global DIGITS

	# print(f"\tSubstring {side} {s:1} and {c_idx=}.")

	if len(s) - 1 <= 0:
		return []

	big = max(s)
	idx = s.index(big)  # index in substring
	DIGITS -= 1

	if DIGITS == 0:
		return [idx + c_idx]

	tail = len(s[idx + 1:])
	if tail == DIGITS:
		# return indicis for all the numbers to the right including the big
		# if there are no numbers on the right, returns just the big -> range(6, 6+0+1) -> [6]
		return [i + c_idx for i in range(idx, idx + tail + 1)]
	elif tail > DIGITS:
		return [idx + c_idx] + find_max(s[idx + 1:], idx + c_idx + 1, "right")  # works
	else:
		# not enough digits on the right side, must supplement from the left
		# but we take the whole right side
		rest = [i + c_idx for i in range(idx, idx + tail + 1)]
		DIGITS -= tail
		return rest + find_max(s[:idx], c_idx, "left")

def part_two():
	global DIGITS

	result: int = 0
	for row in DATA:
		DIGITS = 12
		# print("Starting number:", row)
		res: list[int] = find_max(row, 0, "right")
		res.sort()
		r = "".join(row[i] for i in res)
		# print(f"Final {res=} |", row, " -> ", r, "\n")
		result += int(r)
	print(f"Part two {result=}")


if __name__ == "__main__":
	parse_file()
	part_one()  # 17074
	part_two()  # 169512729575727
