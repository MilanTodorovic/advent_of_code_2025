from collections import deque


def parse_file():
	ranges = deque()
	ingredients = []

	store_in_ranges = True
	with open("input.txt", 'r') as f:
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


def merge_ranges(ranges: deque[list[int]]):
	NEW_RANGES = deque()
	to_remove = []

	while len(ranges) > 1:
		a = ranges.popleft()
		for b in ranges:
			# print(f"Checking range {b=} against range {a=}.")
			if a[0] <= b[0] and a[1] >= b[0]:
				# print(f"Found overlap - {a=} merged with {b=}.")
				a[0], a[1] = a[0], a[1] if a[1] > b[1] else b[1]
				to_remove.append(b)
			elif a[0] >= b[0] and a[0] <= b[1]:
				# print(f"Found overlap - {a=} merged with {b=}.")
				a[0], a[1] = b[0], a[1] if a[1] > b[1] else b[1]
				to_remove.append(b)
			elif a[1]+1 == b[0]:
				# No gap, but also no overlap 12-20 and 21-30. The ranges are inclusive
				# 	so we merge them together
				# print(f"Found overlap - {a=} merged with {b=}.")
				a[0], a[1] = a[0], b[1]
				to_remove.append(b)
			else:
				# no merge can happen
				pass
		else:
			NEW_RANGES.append(a)
			while len(to_remove):
				ranges.remove(to_remove.pop())
	if len(ranges):
		NEW_RANGES.append(ranges.pop())
	ranges = NEW_RANGES
	# print(f"Merged ranges: ", sorted(ranges))
	return ranges


def part_one(ranges: deque[list[int]], ingredients: list[int]):
	fresh = 0
	_ingredients = ingredients[:]
	for _range in ranges:
		to_remove = set()
		left, right = _range
		i = 0
		for ingredient in _ingredients:
			# print(f"Range {left}-{right} and ingredient {ingredient}.")
			if ingredient >= left and ingredient <= right:
				fresh += 1
				to_remove.add(i)
				# print(f"Ingredient {ingredient} is fresh and in range {left}-{right}.")
			i += 1
		else:
			to_remove = sorted(to_remove)
			while len(to_remove):
				_ingredients.pop(to_remove.pop())
	print(f"Part One: {fresh}")


def part_two(ranges: deque[list[int]]):
	fresh = 0
	for r in ranges:
		fresh += r[1]-r[0]+1 # adding +1 because both sides of the range are inclusive
	print(f"Part Two: {fresh}")


if __name__ == "__main__":
	ranges, ingredients = parse_file()
	part_one(ranges, ingredients) # 701
	merged_ranges = merge_ranges(ranges)
	part_two(merged_ranges) # 352340558684863
