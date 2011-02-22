class Matrix(object):
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        # initialize matrix and fill with zeroes
        self.matrix = []
        for i in range(rows):
            each_row = []
            for j in range(cols):
                each_row.append(0)
            self.matrix.append(each_row)

    def __getitem__(self, index):
        return self.matrix[index]
     
    def __repr__(self):
        outStr = "[\n"
        for i in range(self.rows):
            outStr += ' %s\n' % self.matrix[i]
        outStr += '\n]'
        return outStr
