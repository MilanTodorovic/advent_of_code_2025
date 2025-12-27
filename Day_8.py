import math
from itertools import combinations


def parse_file() -> list[tuple[int,...]]:
	contents = []
	file_path = "input_test.txt" if TEST_RUN else "input.txt"
	with open(file_path, 'r') as f:
		for line in f.readlines():
			contents.append(tuple(int(x) for x in line.strip().split(',')))
	return contents

def compute_distance(p:tuple[int,...], q:tuple[int,...]):
	return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2 + (p[2] - q[2])**2)

def part_one(contents:list[tuple[int,...]], no_of_connections: int):
	connected: list[set[int]] = []
	perm:dict[tuple[int,...],float] = {p:0 for p in combinations(contents, 2)}

	for p in perm.keys():
		distance: float = compute_distance(p[0], p[1])
		perm[p] = distance
		# print(f"Distance for pair {p}", distance)
	sorted_dict = dict(sorted(perm.items(), key=lambda item: item[1]))

	for k,v in sorted_dict.items():
		# print(f"Merging {k} with distance {v}")
		# k = tuple(int,...)
		# connected = [set(int,...),set(int,...)]
		left, right = None, None
		for j, con in zip(range(len(connected)), connected):
			if k[0] in con:
				# print(f"Found {k[0]} at index {j}")
				left = j
			if k[1] in con:
				# print(f"Found {k[1]} at index {j}")
				right = j
			if left and right:
				# both found
				break

		if left == right:
			if left == None:
				# neither exist
				# print(f"Neither left nor right were connected. Creating connection.")
				connected.append(set(k))
			else:
				# already merged
				# print(f"Left and right element already merged.")
				pass
		elif left != right:
			if left == None:
				# merge
				# print(f"Updating {k[0]} with {connected[right]}.")
				connected[right].add(k[0])
				# print(f"After update {connected[right]}.")
			elif right == None:
				# merge
				# print(f"Updating {connected[left]} with {k[1]}.")
				connected[left].add(k[1])
				# print(f"After update {connected[left]}.")
			else:
				# merge
				# print(f"Updating {connected[left]} with {connected[right]}.")
				if left > right:
					connected[right].update(connected.pop(left))
					# print(f"After update {connected[right]}.")
				else:
					connected[left].update(connected.pop(right))
					# print(f"After update {connected[left]}.")

		no_of_connections -= 1
		if no_of_connections == 0:
			break

	s: list[int] = [len(junction) for junction in connected]
	s.sort(reverse=True)
	print("Product of the 3 largest junction boxes:", math.prod(s[0:3]))

def part_two(contents):
	connected: list[set[int]] = []
	perm:dict[tuple[int,...],float] = {p:0 for p in combinations(contents, 2)}
	last: tuple[int,...] = None

	for p in perm.keys():
		distance = compute_distance(p[0], p[1])
		perm[p] = distance
	sorted_dict = dict(sorted(perm.items(), key=lambda item: item[1]))

	for k,v in sorted_dict.items():
		left, right = None, None
		for j, con in zip(range(len(connected)), connected):
			if k[0] in con:
				left = j
			if k[1] in con:
				right = j
			if left and right: # both found
				break

		if left == right:
			if left == None: # neither exist
				connected.append(set(k))
				last = k
			else: # already merged
				pass
		elif left != right: # merging
			if left == None:
				connected[right].add(k[0])
			elif right == None:
				connected[left].add(k[1])
			else:
				if left > right:
					connected[right].update(connected.pop(left))
				else:
					connected[left].update(connected.pop(right))
			last = k
	print("The product of the X coordinates of the last two junction boxes that were merged:", last[0][0]*last[1][0])


if __name__ == '__main__':
	# We need to make 1000 shortest connections and
	# 	multiply together the sizes of the three largest circuits
	TEST_RUN = False
	NO_OF_CONNECTIONS = 10 if TEST_RUN else 1000
	contents: list[tuple[int,...]] = parse_file()
	part_one(contents, NO_OF_CONNECTIONS) # 66912
	part_two(contents) # 724454082
