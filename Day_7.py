def parse_file() -> list[str]:
	contents: list[str] = []
	with open("input.txt", 'r') as f:
		for line in f.readlines():
			contents.append(line.strip())
	return contents

def part_one_and_two(contents: list[str]):
	splits: int = 0
	start: int = contents[0].index('S')
	moves: set[int] = {start}
	paths: dict[int,int] = {start:1}
	to_remove: list[int] = []
	to_update: list[int] = []
	for line in contents[1:]:
		for move in moves:
			if line[move] == '.':
				continue
			to_remove.append(move)
			to_update.extend([move-1,move+1])
			paths[move - 1] = paths.get(move - 1, 0) + paths.get(move, 0)
			paths[move + 1] = paths.get(move + 1, 0) + paths.get(move, 0)
			del paths[move]
			splits += 1
		while len(to_remove):
			moves.remove(to_remove.pop())
		while len(to_update):
			moves.add(to_update.pop())
	print("Part One:", splits)
	print("Part Two:", sum(paths.values()))


if __name__ == '__main__':
	contents = parse_file()
	part_one_and_two(contents)
