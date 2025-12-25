from collections import deque


def parse_file():
	ranges = deque()
	ingredients = []

	store_in_ranges = True
	with open("input_5_test.txt", 'r') as f:
		for line in f.readlines():
			if line == "\n":
				store_in_ranges = False
				continue
			if store_in_ranges:
				l, r = line.strip().split("-")
				ranges.append([int(l),int(r)])
			else:
				ingredients.append(int(line.strip()))
	ranges = deque(sorted(ranges))
	ingredients.sort()
	return ranges, ingredients


def merge_ranges(ranges):

	merged = True
	NEW_RANGES = deque()
	to_remove = []
	while merged or len(ranges):
		print(ranges)
		# TODO zajebava u test fajlu
		a = ranges.popleft()
		for b in ranges:
			# print(f"Checking range {b=} against range {a=}.")
			if a[0] <= b[0] and a[1] >= b[0]:
				# print(f"Found overlap - {a=} merged with {b=}.")
				a[0], a[1] = a[0], a[1] if a[1] > b[1] else b[1]
				to_remove.append(b)
				merged = True
			elif a[0] >= b[0] and a[0] <= b[1]:
				# print(f"Found overlap - {a=} merged with {b=}.")
				a[0], a[1] = b[0], a[1] if a[1] > b[1] else b[1]
				to_remove.append(b)
				merged = True
			elif a[1]+1 == b[0]:
				# No gap, but also no overlap 12-20 and 21-30. The ranges are inclusive
				# 	so we merge them together
				# print(f"Found overlap - {a=} merged with {b=}.")
				a[0], a[1] = a[0], b[1]
				to_remove.append(b)
				merged = True
			else:
				# if no merges happened at all, this variables stays False
				merged = False
		else:
			NEW_RANGES.append(a)
			while len(to_remove):
				ranges.remove(to_remove.pop())
			# TODO ovo nece
			if not len(ranges):
				break

	ranges = NEW_RANGES
	# print(f"Merged ranges: ", sorted(ranges))
	return ranges


def part_one(ranges, ingredients):
	fresh = 0
	local_ingredients = ingredients[::]
	for _range in ranges:
		left, right = _range
		j = 0
		for i, ingredient in zip(range(len(ingredients)), ingredients):
			# print(f"Range {left}-{right} and ingredient {ingredient}.")
			if ingredient >= left and ingredient <= right:
				fresh += 1
				local_ingredients.pop(i-j)
				j += 1
				# print(f"Ingredient {ingredient} is fresh and in range {left}-{right}.")
	print(f"Part One: {fresh}")


def part_two(ranges, ingredients):
	print(ranges, ingredients)
	fresh = 0
	s = []
	for _range in ranges:
		left, right = _range
		local_ingredients = ingredients[::]
		j = 0
		for i, ingredient in zip(range(len(local_ingredients)), local_ingredients):
			if ingredient >= left and ingredient <= right:
				# print(f"Popping elemnet {i}")
				ingredients.pop(i-j)
				s.append(_range)
				j += 1
	for r in s:
		fresh += r[1]-r[0]+1
	print(f"Part Two: {fresh}")


if __name__ == "__main__":
	ranges, ingredients = parse_file()
	# part_one(ranges, ingredients) # 701, solved in 301ms
	merged_ranges = merge_ranges(ranges)
	part_two(merged_ranges, ingredients) # 
