import point2d
import line2d


def parseInputStringToPoint2D(str) -> point2d.Point2D:
    coords = str.split(",")

    return point2d.Point2D(int(coords[0]), int(coords[1]))

def parseInputStringToLine2D(str) -> line2d.Line2D:
    parts = str.split(" -> ")

    begin = parseInputStringToPoint2D(parts[0])
    end = parseInputStringToPoint2D(parts[1])

    return line2d.Line2D(begin, end)
