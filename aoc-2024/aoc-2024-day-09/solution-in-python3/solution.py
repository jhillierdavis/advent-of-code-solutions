from helpers import fileutils
from collections import deque

def queue_to_string(q_original):
    q = deque(q_original)
    s = ""
    if None == q:
        return s
    
    while len(q) > 0:
        v = q.popleft()
        if None == v:
            s += '.'
        else:
            s += str(v)
    #print(f"DEBUG: s={s}")
    return s


def to_block_representation_from(diskmap) -> deque:
    if None == diskmap:
        return None
    
    #print(f"DEBUG: diskmap={diskmap}")
    q = deque()

    file_id = 0
    for i, c in enumerate(diskmap):        
        v = int(c)
        if i % 2 == 0: # length of file
            for _ in range(v):
                q.append(file_id)
            file_id += 1
        else: # length of free space
            for _ in range(v):
                q.append(None)
    #print(f"DEBUG: q={q}")
    return q



def to_compacted_from(q_original:deque):
    q = deque(q_original)    
    q_compacted = deque()
    size = len(q)

    #print(f"DEBUG: q={q} size={size}")
    for _ in range(size):
        if len(q) <= 0:
            break

        v_i = q.popleft()
        #print(f"DEBUG: {v_i}")
        if v_i == None:
            v_j = None
            while len(q) > 0 and v_j == None:
                v_j = q.pop()
            if v_j is not None:
                q_compacted.append(v_j)
        else:
            q_compacted.append(v_i)

    #print(f"DEBUG: {q_compacted}")
    return q_compacted


def to_checksum_from(q_compacted:deque) -> int:
    q = deque(q_compacted)
    ans = 0
    i = 0
    while len(q) >= 1:
        file_id = q.popleft()
        multiple = file_id * i
        #print(f"DEBUG: file_id={file_id} i={i} mulitple = {multiple}")
        i += 1
        ans += multiple
    return ans    


def solve_part1(filename):
    input = fileutils.get_text_from(filename)
    qbr = to_block_representation_from(input)
    qc = to_compacted_from(qbr)
    #print(f"DEBUG: qc={qc}")

    return to_checksum_from(qc)


def solve_part2(filename):
    input = fileutils.get_text_from(filename)
    qbr = to_block_representation_from(input)
    qc = to_compacted_from(qbr) # TODO: Change compaction approach
    #print(f"DEBUG: qc={qc}")

    return to_checksum_from(qc)
