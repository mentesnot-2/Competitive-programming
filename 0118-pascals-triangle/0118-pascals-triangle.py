class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            prev_triangle = self.generate(numRows - 1)
            prev_row = prev_triangle[-1]
            new_row = [1]
            for i in range(1, len(prev_row)):
                new_row.append(prev_row[i - 1] + prev_row[i])
            new_row.append(1)
            prev_triangle.append(new_row)
            return prev_triangle


        