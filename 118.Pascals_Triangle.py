class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        array = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return array
        for i in range(2, numRows):
            ar = [0 for _ in range(i+1)]
            ar[0] = 1
            ar[-1] = 1
            for j in range(1, i):
                ar[j] = array[i -1][j-1] + array[i -1][j]
            array.append(ar)
        return array
