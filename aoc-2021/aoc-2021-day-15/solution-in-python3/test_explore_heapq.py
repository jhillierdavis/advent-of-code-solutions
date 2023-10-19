
import heapq

# Local
from helpers import point

def test_explore_heapq():
    h = []
    heapq.heappush(h, (5, point.Point2D(0, 1)))
    heapq.heappush(h, (1, point.Point2D(2,1)))
    heapq.heappush(h, (3, point.Point2D(1,1)))
    heapq.heappush(h, (3, point.Point2D(1,0)))
    heapq.heappush(h, (4, point.Point2D(1,2)))

    #print(f"DEBUG: h={h}") # Sorted list (min. value first)

    assert heapq.heappop(h) == (1, point.Point2D(2,1))
    assert heapq.heappop(h)[0] == 3
    assert heapq.heappop(h)[0] == 3
    assert heapq.heappop(h)[0] == 4
    assert heapq.heappop(h)[0] == 5
    assert len(h) == 0    