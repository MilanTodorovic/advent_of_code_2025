DIAL = 50

def parse_input():
	_input: list[int] = []
	with open('input_1.txt', 'r') as file:
		for line in file.readlines():
			_input.append(int(line[1:]) if line.startswith('R') else -int(line[1:]))
	return _input

def part_one(_input: list[int], dial_poisiton: int):
	result = 0
	for i in _input:
		dial_poisiton = (dial_poisiton + i) % 100
		if dial_poisiton == 0:
			result += 1
	print(f"{result=}")

def part_two(_input: list[int], dial_poisiton: int):
	result = 0
	starting_poisiton = dial_poisiton
	for i in _input:
		if i == 0:
			# if there is an L0 or R0
			continue
		full_rotations, remainder = abs(i)//100, abs(i)%100
		result += full_rotations
		if remainder == 0:
			# no rotation to be made
			continue
		else:
			remainder = remainder if i >=0 else -remainder # neccessary because // and % work differently with negative numbers
			dial_poisiton = dial_poisiton + remainder
			if (dial_poisiton >= 100 or dial_poisiton <= 0) and starting_poisiton != 0:
				# if we start from zero and move -1, then this condition will be triggered
				#	 as if we made a rotation from a positive number over a zero into 99
				result += 1
			dial_poisiton = dial_poisiton%100
			starting_poisiton = dial_poisiton
	
	print(f"{result=}")

if __name__ == "__main__":
	parsed_input = parse_input()
	part_one(parsed_input, DIAL) # 1141
	part_two(parsed_input, DIAL) # 6634