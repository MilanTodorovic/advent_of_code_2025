from itertools import combinations

def pattern_to_bits(light_pattern: str) -> int:
	bits = "0b"
	for char in light_pattern:
		if char == '#':
			bits += '1'
		else:
			bits += '0'
	return int(bits,2)

def bit_mask(button_wiring: list[int], length: int) -> int:
	bits = ['0']*length
	for i in button_wiring:
		bits[i] = '1'
	bits = int("".join(bits),2)
	# print(f"Bitmask: {bits:08b} for {button_wiring}")
	return bits

def parse_file() -> list[list[int]]:
	contents: list[list[int]] = []
	file = "input_test.txt" if TEST_RUN else "input.txt"

	with open(file, 'r') as f:
		for line in f.readlines():
			light = line.index("]")
			jolt = line.index("{")
			light_pattern: str = line[1:light]
			jolts: list[int] = [int(j) for j in line.strip()[jolt+1:-1].split(',')]
			switches = []
			for bracket in line[light+1:jolt].strip().split(' '):
				tmp = []
				for num in bracket[1:-1].split(','):
					tmp.append(int(num))
				switches.append(bit_mask(tmp, len(light_pattern)))
			# print(f"{switches=}")
			contents.append([pattern_to_bits(light_pattern), switches, jolts])
	return contents

def check_mask(combination, pattern) -> int:
	for comb in combination:  # comb = [(x,),...]
		for c in comb:  # c = (x,...)
			result = pattern
			# print(f"Combination {c}")
			press = len(c)
			for mask in c:
				result ^= mask
			if result == 0:
				# print(f"Found button pattern {c} with press weight {press}")
				return press

def part_one(contents: list[list[int]]):
	# sum of fewest button presses for indicator lights
	result: list[int] = []
	for c in contents:
		pattern = c[0]
		switches = c[1]
		jolts = c[2]

		combination = [combinations(switches, i) for i in range(1, len(switches)+1)]
		result.append(check_mask(combination, pattern))

	print(f"Result: {sum(result)}")


def part_two(contents: list[str]):
	pass


if __name__ == "__main__":
	TEST_RUN = False
	contents = parse_file()
	part_one(contents)  # 385
	#part_two(contents)
