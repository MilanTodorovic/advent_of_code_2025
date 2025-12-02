from itertools import batched


def parse_file() -> list[range]:
	generators: list[range] = []
	with open('input_2.txt', 'r') as file:
		contents = file.readline() # this time it is a single line
		for ranges in contents.split(','):
			s, e = ranges.split('-')
			generators.append(range(int(s), int(e)+1)) # must be inclusive
		return generators

def test_pattern(id_to_test: str) -> int:
	len_of_integer = len(id_to_test)
	if len_of_integer%2 == 0:
		ln = len_of_integer//2
		for x in range(1,ln+1):
			groups = batched(id_to_test, x)
			if all(id_to_test[:x] == digit for digit in groups):
				print("Integer macthes a pattern", id_to_test)
				return int(id_to_test)
		else:
			# integer doesn't match any pattern
			print("Integer dossn't macth any pattern", id_to_test)
			return 0
	else:
		# odd number of digits must all be the same
		pattern = id_to_test[0]
		if all(pattern == digit for digit in id_to_test):
			return int(id_to_test)
		else:
			return 0

def part_one(generators: list[range]):
	result: int = 0
	for generator in generators:
		for i in generator:
			str_i = str(i)
			len_of_integer = len(str_i)
			if len_of_integer%2 == 0:
				# integer has even number of digits
				if str_i[:len_of_integer//2] == str_i[len_of_integer//2:]:
					result += i
			else:
				continue
	print(f"{result=}")

def part_two(generators: list[range]):
	result: int = 0
	for generator in generators:
		for i in generator:
			str_i = str(i)
			result += test_pattern(str_i)
	print(f"{result=}")

if __name__ == "__main__":
	ranges: list[range] = parse_file()
	part_one(ranges) # 24157613387
	part_two(ranges) # >>>
