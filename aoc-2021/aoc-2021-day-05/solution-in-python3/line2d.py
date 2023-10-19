# from typing import Self # Not available before Python version 3.11: ImportError: cannot import name 'Self' from 'typing'

import point2d

class Line2D():

    def __init__(self, begin:point2d.Point2D, end:point2d.Point2D):
        self.begin = begin
        self.end = end

    def getBeginPoint(self) -> point2d.Point2D:
        return self.begin

    def getEndPoint(self) -> point2d.Point2D:
        return self.end

    def isHorizontalLine(self) -> bool:
        return self.begin.getX() == self.end.getX()
    
    def isVerticalLine(self) -> bool:
        return self.begin.getY() == self.end.getY()
    
    def isDiagonalLine(self) -> bool:
        return not (self.isHorizontalLine() or self.isVerticalLine())
    
    def getAllPoints(self):
        coords = []
        if self.isHorizontalLine():
            minY = min(self.begin.getY(), self.end.getY())
            maxY = max(self.begin.getY(), self.end.getY())
            for y in range(minY, 1 + maxY):
                coords.append(point2d.Point2D(self.begin.getX(), y))       
        elif self.isVerticalLine():
            minX = min(self.begin.getX(), self.end.getX())
            maxX = max(self.begin.getX(), self.end.getX())
            for x in range(minX, 1 + maxX):
                coords.append(point2d.Point2D(x, self.begin.getY()))
        else: # Diagonal
            diffx = 1
            diffy = 1
            if (self.begin.getX() > self.end.getX()):
                diffx = -1
            if (self.begin.getY() > self.end.getY()):                
                diffy = -1

            minX = min(self.begin.getX(), self.end.getX())
            maxX = max(self.begin.getX(), self.end.getX())
            size = maxX - minX
            #minY = min(self.begin.getY(), self.end.getY())
            #maxY = max(self.begin.getY(), self.end.getY())
            for i in range(1+size):
                coords.append(point2d.Point2D(self.begin.getX() + (i*diffx), self.begin.getY() + (i*diffy)))
        return coords
        
    def __str__(self):
        return f"Line2D(id={id(self)} , begin: {self.getBeginPoint()}, end: {self.getEndPoint()})"
    
    def __eq__(self,other) -> bool:
        return self.getBeginPoint() == other.getBeginPoint() and self.getEndPoint() == other.getEndPoint()    