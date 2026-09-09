class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        subArr = -1 # index to apply binary search
        

        # iterate over each sub array to find where the target could be
        for i in range(m):
            subMin = matrix[i][0]
            subMax = matrix[i][n - 1]
            
            if target >= subMin and target <= subMax:
                subArr = i
                break
        
        if subArr == -1:
            return False

        if subArr >= 0:
            return self.binarySearch(matrix[subArr], 0, n-1, target)
            

    def binarySearch(self, subMatrix, l, r, target):
        if l > r:
            return False
        # compute midpoint
        mp = l + ((r - l) // 2)

        if subMatrix[mp] == target:
            return True
        elif subMatrix[mp] > target:
            # r = m - 1
            return self.binarySearch(subMatrix, l, mp - 1, target)
        else:
            return self.binarySearch(subMatrix, mp + 1, r, target)