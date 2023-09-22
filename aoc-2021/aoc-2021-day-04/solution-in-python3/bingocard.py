import grid

class BingoCard:    
    def __init__(self, grid2d:grid.Grid2d):
        self.grid2d = grid2d
        self._marked_numbers = []

    def isMatchedNumber(self, number):
        # Check if already present
        if number in self._marked_numbers:
            return True

        for r in range(self.grid2d.getNumberOfRows()):
            row = self.grid2d.getRow(r)
            if number in row:
                self._marked_numbers.append(number)
                return True


        for c in range(self.grid2d.getNumberOfColumns()):
            column = self.grid2d.getColumn(c)
            if number in column:
                self._marked_numbers.append(number)
                return True
            
        return False # Not contained
    
    def hasCompletedRow(self, row):
        for i in row:
            if i not in self._marked_numbers:
                return False        
        return True

    def hasCompletedColumn(self, column):
        for i in column:
            if i not in self._marked_numbers:
                return False        
        return True

    def isBingo(self):
        if len(self._marked_numbers) <= 0:
            return False

        #  Check rows        
        for r in range(self.grid2d.getNumberOfRows()):
            row = self.grid2d.getRow(r)
            if self.hasCompletedRow(row):
                    return True

        #  Check columns        
        for c in range(self.grid2d.getNumberOfColumns()):
            column = self.grid2d.getColumn(c)
            if self.hasCompletedColumn(column):
                return True

        return False

    def getUnmarkedNumbers(self):
        unmarked = []

        for r in range(self.grid2d.getNumberOfRows()):
            row = self.grid2d.getRow(r)
            for i in row:
                if i not in self._marked_numbers and i not in unmarked:
                    unmarked.append(i)
        
        for c in range(self.grid2d.getNumberOfColumns()):
            column = self.grid2d.getColumn(c)
            for i in column:
                if i not in self._marked_numbers and i not in unmarked:
                    unmarked.append(i)   

        return unmarked
    
    def __str__(self):
        return "grid:" + str(self.grid2d) + " marked_numbers:" + str(self._marked_numbers)