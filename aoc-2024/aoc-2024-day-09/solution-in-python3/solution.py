from collections import deque
from helpers import fileutils


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
        if file_id is not None: 
            multiple = file_id * i
            ans += multiple
        #print(f"DEBUG: file_id={file_id} i={i} mulitple = {multiple}")
        i += 1
        
    return ans    


def solve_part1(filename):
    input = fileutils.get_text_from(filename)
    qbr = to_block_representation_from(input)
    qc = to_compacted_from(qbr)
    #print(f"DEBUG: qc={qc}")

    return to_checksum_from(qc)


def to_block_representation_as_pairs_from(diskmap) -> deque:
    if None == diskmap:
        return None
    
    #print(f"DEBUG: diskmap={diskmap}")
    q = deque()

    file_id = 0
    for i, c in enumerate(diskmap):        
        v = int(c)
        count = 0
        if i % 2 == 0: # length of file            
            for _ in range(v):
                count += 1
            q.append((file_id, count))    
            if count > 0:
                file_id += 1
        else: # length of free space
            count = 0
            for _ in range(v):
                count += 1
            if count > 0:
                q.append((None, count))
    #print(f"DEBUG: q={q}")
    return q

    
def populate_gap(dfq, qp, qp_reversed, size):
    matched = None
    remainder = 0
    for e in qp_reversed:
        ev, ec = e
        if ev == None:
            continue

        if ec <= size:
            remainder = size - ec
            matched = e
            for _ in range(ec):
                dfq.append(ev)
            break
    
    if matched:
        idx = qp.index(matched)
        qp.remove(matched)
        qp.insert(idx, (None, matched[1]))
        qp_reversed.remove(matched)
        if remainder > 0:
            populate_gap(dfq, qp, qp_reversed, remainder)
    elif remainder > 0:        
        for _ in range(remainder):
            dfq.append(None)
    else:       
        for _ in range(size):
            dfq.append(None)
    #print(f"DEBUG: size={size} remainder={remainder} dfq={dfq}")
    

def solve_part2(filename):
    input = fileutils.get_text_from(filename)

    qp = to_block_representation_as_pairs_from(input)
    #print(f"DEBUG: qp={qp}")

    qp_reverse = deque(qp)
    qp_reverse.reverse()

    dfq = deque()
    while len(qp) > 0:
        p = qp.popleft()
        v,c = p

        if v is not None:
            for _ in range(c):
                dfq.append(v)
            if qp_reverse.count(p) > 0:
                qp_reverse.remove(p)
        else:
            populate_gap(dfq, qp, qp_reverse, c)
        

    #print(f'DEBUG: dfq={dfq}')
    return to_checksum_from(dfq)