class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = 0
        b = len(matrix)
        k = len(matrix[0])-1

        while a<b:
            mid = (a+b)//2
            if matrix[mid][0] < target and matrix[mid][k] < target:
                if a != mid:
                    a= mid
                else:
                    return False

            elif matrix[mid][0] > target and matrix[mid][k] > target:
                if b != mid:
                    b = mid
                else:
                    return False

            elif (matrix[mid][0] <= target and matrix[mid][k] >= target):
                begin = 0
                end = len(matrix[mid])
                while begin < end:
                    mid1 = (begin+end)//2
                    if matrix[mid][mid1] > target:
                        if end != mid1:
                            end = mid1
                        else:
                            return False
                    elif matrix[mid][mid1] < target:
                        if begin != mid1:
                            begin = mid1
                        else:
                            return False
                    elif matrix[mid][mid1] == target:
                        return True
                    
        return False








