# https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
class Solution:
    def getMinMax(self, arr):
        # code here
        max_ele = min_ele = arr[0]
        for i in arr[1:]:
            if i > max_ele:
                max_ele = i
            if i < min_ele:
                min_ele = i
                
        return [min_ele, max_ele]