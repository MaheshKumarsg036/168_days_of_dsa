# https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1

class Solution:
    def reverseWords(self, s):
        # code here
        s_array = s.split(".")
        s_array = [x for x in s_array if x != ""]
        ans = ".".join(s_array[::-1])
        if ans[0] == ".":
            ans = ans[1::]
        if ans[-1] == ".":
            ans = ans[:-1:]
        return ans