class Grid2d:    
    def __init__(self, grid_data):
        self.grid_data = grid_data          
        self._numberOfRows = len(self.grid_data[0])
        self._numberOfColumns = len(self.grid_data) 

    def getNumberOfRows(self):
        return self._numberOfRows

    def getNumberOfColumns(self):
        return self._numberOfColumns      

    def getRow(self, index):
        return self.grid_data[index]

    def getColumn(self, index):
        col = []
        for i in range(self._numberOfRows):
            col.append(self.grid_data[i][index])
        return col
    
    def __str__(self):
        return str(self.grid_data)
