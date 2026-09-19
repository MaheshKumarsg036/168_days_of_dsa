# https://www.geeksforgeeks.org/problems/maximum-occuring-character-1587115620/1

class Solution:
    def getMaxOccuringChar(self, s):
        # code here
        freq = {}
        for i in s:
            freq[i] = freq.get(i,0)+1
            
        max_count = 0
        ans = None
        for char,count in freq.items():
            if ans is None:
                ans = char
            if count > max_count:
                ans = char
                max_count = count
            if count == max_count and char < ans:
                ans = char
                
        return ans