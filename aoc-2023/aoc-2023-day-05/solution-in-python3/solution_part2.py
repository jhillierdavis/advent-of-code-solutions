from helpers import fileutils

from collections import defaultdict

class IntervalAdjuster():
    def __init__(self, destination, source, offset):
            self.source_interval = Interval(source, offset)
            self.destination_interval = Interval(destination, offset)

    def adjust(self, interval_list):
        adjusted_interval_list = []

        for interval in interval_list:
            if not self.source_interval.overlaps(interval):
                adjusted_interval_list.append(interval)

            overlap_interval = self.source_interval.get_overlap_interval()
            #overlap_interval.
                

        return sorted(adjusted_interval_list, reverse=True)




def get_intervals(begin:int, end:int, interval_list):
    existing_intervals = sorted(interval_list, reverse=True)
    print(f"DEBUG: Existing intervals: {existing_intervals}")
    new_interval_set = []

    min = begin
    for ei in existing_intervals:
        
        b = ei.get_begin()
        e = ei.get_end()
        if b > min:
            gap = Interval(min, b - 1)
            print(f"DEBUG: Creating gap interval: {gap}")
            new_interval_set.append(gap)    

        if min < e:
            new_interval_set.append(ei)
            min = e

    last = new_interval_set[-1]
    if last.get_end() < end:
        new_interval_set.append(Interval(e, end - e))

    print(f"DEBUG: new_interval_set={new_interval_set}")
    return new_interval_set


class Interval():

    def __init__(self, start:int, offset:int):
        assert offset >= 1
        self.start = start
        self.offset = offset

    def get_begin(self) -> int:
        return self.start

    def get_end(self) -> int:
        return (self.start + self.offset) - 1
    
    def get_offset(self):
        return self.offset
    
    def adjust_begin(self, value) -> int:
        self.start += value

    
    def contains_value(self, value:int) -> bool:
        #print(f"DEBUG: begin={self.get_begin()} end={self.get_end}")
        if value >= self.get_begin() and value <= self.get_end():
            return True
        return False
    
    def contains(self, other_interval):
        if self.get_end() <= other_interval.get_end() and self.get_begin() >= other_interval.get_begin():
            return True
        return False

    def overlaps(self, other_interval):
        # contains
        if self.contains(other_interval):
            return True
        if other_interval.contains(self):
            return True        
        if self.get_end() <= other_interval.get_end() and self.get_end() >= other_interval.get_begin():
            return True
        if self.get_begin() >= other_interval.get_begin() and self.get_begin() <= other_interval.get_end():
            return True
        
        return False

    def get_overlap_interval(self, other_interval):
        # contains
        if self.contains(other_interval):
            # TODO: Add clone
            return Interval(other_interval.get_begin(), other_interval.get_offset())
        
        if other_interval.contains(self):
            # TODO: Add clone
            return Interval(self.get_begin(), self.get_offset())        
        
        if self.get_begin() <= other_interval.get_begin() and self.get_end() >= other_interval.get_begin():
            return Interval(other_interval.get_begin(), 1 + self.get_end() - other_interval.get_begin())

        if self.get_begin() >= other_interval.get_begin() and self.get_begin() <= other_interval.get_end():            
            return Interval(self.get_begin(), 1 + other_interval.get_end() - self.get_begin())

        return None



    def __eq__(self,other) -> bool:
        if other == None or self.get_begin() != other.get_begin() or self.get_offset() != other.get_offset():
            return False
        return True
    
    def __hash__(self):
        return hash(self.get_begin()) + hash(self.get_offset())
    
    def __lt__(self, other):
        return self.get_begin() > other.get_begin()
    
    def __repr__(self) -> str:
        return str(self)

    def __str__(self):
        return f"Interval(id={id(self)} , begin: {self.get_begin()}, offset: {self.get_offset()}, end: {self.get_end()})"

def get_seed_intervals_from_filename(filename):
    seed_lines = fileutils.get_lines_before_empty_from_file(filename)

    #print(f"DEBUG: seed_lines={seed_lines}")
    (s,v) = seed_lines[0].split(':')    
    pair_list = list(map(int, v.split()))

    seed_list = []
    for i in range(0, len(pair_list), 2):        
            seed_list.append(Interval(pair_list[i],pair_list[i+1] ))
    return sorted(seed_list, reverse=True)


    

