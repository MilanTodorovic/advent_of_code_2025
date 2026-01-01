TREE = dict()
DAC_OUT = 0
FFT_DAC = 0
SVR_FFT = 0
TOTAL = 0

def parse_file():
	if TEST_RUNE:
		if PART_TWO:
			file = "input_test2.txt"
		else:
			file = "input_test.txt"
	else:
		file = "input.txt"

	with open(file, 'r') as f:
		for line in f.readlines():
			root, children = line.strip().split(':')
			TREE[root] =  children.strip().split(' ')

def traverse(root: str, depth: int, goal: str):
	global TOTAL, DAC_OUT, FFT_DAC, SVR_FFT
	# prefix = " " * depth + "└─" if depth else ""
	# print(prefix+root)
	for child in TREE[root]:
		if child == goal:
			if goal == "dac":
				FFT_DAC += 1
			elif goal == "fft":
				SVR_FFT += 1
			elif goal == "out":
				DAC_OUT += 1
				TOTAL += 1
			break
		elif child == "out":
			break
		traverse(child, depth+2, goal)

def part_one():
	for child in TREE["you"]:
		traverse(child, 0, "out")
	print(f"Total number of possible path from 'you' to 'out': {TOTAL}")

def part_two():
	for child in TREE["svr"]:
		traverse(child, 0, "fft")
	for child in TREE["fft"]:
		traverse(child, 0, "dac")
	for child in TREE["dac"]:
		traverse(child, 0, "out")
	print(f"Total number of possible path from 'svr' to 'out' passing thru both 'dac' and 'fft': {DAC_OUT*FFT_DAC*SVR_FFT}")

if __name__ == '__main__':
	TEST_RUNE = False
	PART_TWO = True
	parse_file()
	part_one() # 508
	# part_two() # doesn't work
