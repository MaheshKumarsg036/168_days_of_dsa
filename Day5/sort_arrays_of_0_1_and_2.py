# https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

class Solution:
    def sort012(self, arr):
        # code here
        count_0 = count_1 = count_2 = 0
        for i in arr:
            if i == 0:
                count_0 += 1
            if i == 1:
                count_1 += 1
            if i == 2:
                count_2 += 1
                
        k = 0
        while count_0 > 0:
            arr[k] = 0
            k += 1
            count_0 -= 1
            
        while count_1 > 0:
            arr[k] = 1
            k += 1
            count_1 -= 1
            
        while count_2 > 0:
            arr[k] = 2
            k += 1
            count_2 -= 1
            
        return arr