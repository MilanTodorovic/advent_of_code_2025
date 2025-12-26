def parse_file() -> list[str]:
	contents = []
	with open("input_6.txt", 'r') as f:
		for line in f.readlines():
			contents.append(line.strip('\n'))
	return contents


def part_one(c: list[str]):
	total = 0
	len_of_col = len(c)
	len_of_row = len(c[-1])
	digits: list[str] = []
	_op = ""
	for i, op in zip(range(len_of_row), c[-1]):
		#print(f"{i=}, {op=}")
		if op != " ":
			e = f"{_op}".join(d.strip() for d in digits)
			print(f"Evaluating {e=}.")
			total += eval(e) if e else 0
			digits: list[str] = []
			_op = op
		for j in range(len_of_col-1):
			if len(digits) == len_of_col-1:
				digits[j] += c[j][i]
			else:
				digits.append(c[j][i])
	else:
		# TODO the code as is doesn\t trigger for the last operand and digits
		#	this is a workaround
		total += eval(f"{_op}".join(d.strip() for d in digits))

	print("Part One:", total)


def part_two(c: list[str]):
	total = 0
	len_of_row = len(c[-1])
	tmp = []
	for i, op in zip(range(len_of_row), c[-1]):
		if op != " ":
			tmp.append(op)
			n = c[0][i]+c[1][i]+c[2][i]+c[3][i]
			tmp.append(n.strip())
		else:
			n = c[0][i]+c[1][i]+c[2][i]+c[3][i]
			n = n.strip()
			if n:
				tmp.append(n)
			else:
				total += eval(f"{tmp[0]}".join(n for n in tmp[1:]))
				tmp = []
	else:
		# TODO the code as is doesn\t trigger for the last operand and digits
		#	this is a workaround
		total += eval(f"{tmp[0]}".join(n for n in tmp[1:]))
	print("Part Two:", total)


if __name__ == '__main__':
	contents = parse_file()
	part_one(contents) # 5227286044585
	part_two(contents) # 10227753257799
