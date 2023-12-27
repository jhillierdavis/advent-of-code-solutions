from collections import defaultdict

from helpers.fileutils import get_file_lines_from
from helpers.strutils import string_to_int_list


def is_same_cube(cube_a:(int,int,int), cube_b:(int,int,int)) -> bool:
	for i in range(3):
		if cube_a[i] != cube_b[i]:
			return False
	return True


def has_block_intersection(block_a:[(int,int,int)], block_b:[(int,int,int)]) -> bool:
	for c_a in block_a:
		for c_b in block_b:
			if is_same_cube(c_a, c_b):
				return True
	return False


def get_block_shifted_down(block:[(int,int,int)]) -> [(int,int,int)]:
	return [(x,y,z-1) for (x,y,z) in block]


def get_block_shifted_up(block:[(int,int,int)]) -> [(int,int,int)]:
	return [(x,y,z+1) for (x,y,z) in block]


def is_block_grounded(block:[(int,int,int)]) -> bool:
	for _,_,z in block:
		if z <= 1:
			return True
	return False


def get_block_cubes_from(begin, end):
	xb = begin[0]
	xe = end[0]
	yb = begin[1]
	ye = end[1]
	zb = begin[2]
	ze = end[2]

	cubes = []
	if xb == xe and yb == ye and zb == ze:
		cubes.append((xb,yb,zb))
	elif xb == xe and yb == ye:          
		for z in range(zb, 1 + ze):                
			cubes.append((xb,yb,z))
	elif xb == xe and zb == ze:          
		for y in range(yb, 1 + ye):                
			cubes.append((xb,y,zb))
	elif zb == ze and yb == ye:          
		for x in range(xb, 1 + xe):                
			cubes.append((x,yb,zb))
	else:
		raise Exception(f"Unhandled type of block with begin={begin} end={end}")
	return cubes


def get_blocks_from(filename):
	lines = get_file_lines_from(filename)

	blocks = []
	for l in lines:
		b,e = l.split('~')

		begin = string_to_int_list(b, ',')
		end = string_to_int_list(e, ',')

		block_cubes = get_block_cubes_from(begin, end)
		blocks.append(block_cubes)
	return blocks


def get_max_block_height_from(blocks):
	max_height = 0
	for b in blocks:
		for (_,_,z) in b:
			if z > max_height:
				max_height = z
	return max_height


def move_down(blocks):
	count = 0
	length = len(blocks)
	for i in range(length):
		if is_block_grounded(blocks[i]):
			continue

		can_shift_down = True
		
		while can_shift_down:
			block_below = [(x,y,z-1) for (x,y,z) in blocks[i]]

			for j in range(length):
				if i == j:
					break
				
				if j > i:
					can_shift_down = False
					break

				if has_block_intersection(block_below, blocks[j]):
					can_shift_down = False
					break

			if can_shift_down:
				blocks[i] = block_below
				count +=1
				if is_block_grounded(block_below):
					can_shift_down = False		

	return count


def get_blocks_sorted_by_height_ascending_from(blocks):
	max_height = get_max_block_height_from(blocks)

	sorted_blocks = []
	for h in range(max_height):
		for b in blocks:
			if b[0][2] == h + 1:
				sorted_blocks.append(b)

	#assert len(sorted_blocks) == len(blocks)
	return sorted_blocks


def display_blocks(blocks):
	for b in blocks:
		print(f"{sorted(b)}")  


def move_until_stable_from(filename):
	blocks = get_blocks_from(filename)
	#print(f"DEBUG: Initial blocks={blocks}")
	
	sorted_blocks = get_blocks_sorted_by_height_ascending_from(blocks)
	move_down(sorted_blocks)

	#display_blocks(blocks)
	#print(f"DEBUG: Final blocks={blocks}")
	return sorted_blocks


def get_support_map(blocks):
	support_map = defaultdict(set)

	for i,bi in enumerate(blocks):
		block_above = [(x,y,z+1) for (x,y,z) in bi]

		for j,bj in enumerate(blocks):
			if i == j:
				continue

			if has_block_intersection(block_above, bj):
				support_map[i].add(j)
	return support_map


def is_support_by_other_block(support_map, i, s):
	for k in support_map.keys():
		if k == i:
			continue

		if s in support_map[k]:
			return True
	return False


def are_all_supported_by_other_block(support_map, i):
	supporting = support_map[i]

	for s in supporting:
		if not is_support_by_other_block(support_map, i, s):
			return False
	return True


def solve_part1(filename):
	blocks = move_until_stable_from(filename)

	support_map = get_support_map(blocks)
	#print(f"DEBUG: support_map={support_map}")

	count = 0
	for i, _ in enumerate(blocks):
		supporting = support_map[i]

		if len(supporting) == 0:
			#print(f"DEBUG: Can disintegrate (not supporting): index={i} block={b}" )
			count +=1
		elif are_all_supported_by_other_block(support_map, i):
			#print(f"DEBUG: Can disintegrate (others supporting): index={i} block={b}" )				
			count +=1

	return count


"""
def get_all_unsupported_by_other_block(support_map, i):
	supporting = support_map[i]

	unsupported = set()
	for s in supporting:
		if not is_support_by_other_block(support_map, i, s):
			unsupported.add(s)
	return unsupported
"""

def get_other_supporters(support_map, i, s):
	supporters = set()
	for k in support_map.keys():
		if k == i:
			continue

		if s in support_map[k]:
			supporters.add(k)
	return supporters


def count_falls_with_chain_reaction(support_map, i, fall):	
	#print(f"DEBUG: [count_falls_with_chain_reaction] Block {i}")
	for s in list(support_map[i]):
		other_supporters = get_other_supporters(support_map, i, s)
		if len(other_supporters) == 0 or other_supporters.issubset(fall):
			fall.add(s)
			count_falls_with_chain_reaction(support_map, s, fall)	


def calculate_falls_for_block_disintegrations(support_map:defaultdict):
	count = 0
	
	for k in list(support_map.keys()):
		if 0 == len(support_map[k]):		
			continue
		elif are_all_supported_by_other_block(support_map, k):
			continue
		
		fall = set()
		count_falls_with_chain_reaction(support_map, k, fall)
		fall_count = len(fall)
		#print(f"DEBUG: Block {k} fall_count={fall_count} fall={fall}")
		fall.clear()
		count += fall_count

	#print(f"DEBUG: count={count}")
	return count


def solve_part2(filename):
	blocks = move_until_stable_from(filename)

	support_map = get_support_map(blocks)
	#print(f"DEBUG: support_map={support_map}")

	count = calculate_falls_for_block_disintegrations(support_map)
	return count