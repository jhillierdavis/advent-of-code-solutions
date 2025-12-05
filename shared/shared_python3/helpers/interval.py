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
        if self.get_end() >= other_interval.get_end() and self.get_begin() <= other_interval.get_begin():
            return True
        return False

    def has_intersection(self, other_interval):
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

    def get_intersection(self, other_interval):
        if self.contains(other_interval):
            return other_interval.clone()
        
        if other_interval.contains(self):
            return self.clone()
        
        if self.get_begin() <= other_interval.get_begin() and self.get_end() >= other_interval.get_begin():
            return Interval(other_interval.get_begin(), 1 + self.get_end() - other_interval.get_begin())

        if self.get_begin() >= other_interval.get_begin() and self.get_begin() <= other_interval.get_end():            
            return Interval(self.get_begin(), 1 + other_interval.get_end() - self.get_begin())

        return None
    
    def get_subtraction(self, other_interval):
        if self.contains(other_interval):
            if self == other_interval:
                return []
            elif self.get_begin() == other_interval.get_begin():
                return [Interval(other_interval.get_end() + 1, self.get_offset() - other_interval.get_offset())]
            elif self.get_end() == other_interval.get_end():
                return [Interval(self.get_begin(), self.get_offset() - other_interval.get_offset())]
            else:
                #print(f"DEBUG: {self} {other_interval} ")
                return [Interval(self.get_begin(), other_interval.get_begin() - self.get_begin()), Interval(other_interval.get_end() + 1, self.get_end() - (other_interval.get_end() + 1))]

        if other_interval.contains(self):
            return other_interval.get_subtraction(self)

        intersection = self.get_intersection(other_interval)

        if not intersection:
            return sorted([self, other_interval], reverse=True)
        
        if other_interval > self:
            #print(f"DEBUG: intersection > self")
            self_subtraction = Interval(intersection.get_end()+1, self.get_offset() - intersection.get_offset())
            other_subtraction = Interval(other_interval.get_begin(), other_interval.get_offset() - intersection.get_offset())            
        else:
            #print(f"DEBUG: intersection <= self")
            self_subtraction = Interval(self.get_begin(), self.get_offset() - intersection.get_offset())
            other_subtraction = Interval(intersection.get_end()+1, other_interval.get_offset() - intersection.get_offset())            

        subtraction = [self_subtraction, other_subtraction]
        #print(f"DEBUG: self={self} other_interval={other_interval} intersection={intersection} subraction={subtraction}")
        return sorted(subtraction, reverse=True)        
        #return [Interval(5,2), Interval(10,2)]


    """
    def get_difference(self, other_interval):
        begin = self.get_begin()            
        if begin <= other_interval.get_begin():
            if self.get_end() <= other_interval
    """
            
    
    def get_union(self, other_interval):
        intersection = self.get_intersection(other_interval)
        if not intersection:
            union = [self, other_interval]
            return sorted(union, reverse=True)

        #print(f"DEBUG: intersection={intersection}")
        
    
        return None


    def __eq__(self,other) -> bool:
        if other == None or self.get_begin() != other.get_begin() or self.get_offset() != other.get_offset():
            return False
        return True
    
    def clone(self):
        return Interval(self.get_begin(), self.get_offset())
    
    def __hash__(self):
        return hash(self.get_begin()) + hash(self.get_offset())
    
    def __lt__(self, other):
        return self.get_begin() > other.get_begin()
    
    def __repr__(self) -> str:
        return str(self)

    def __str__(self):
        return f"Interval(id={id(self)} , begin: {self.get_begin()}, offset: {self.get_offset()}, end: {self.get_end()})"
