# https://leetcode.com/problems/string-compression/submissions/2145907868/
class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        k = 0
        while i < len(chars):
            char = chars[i]
            count = 1
            i += 1
            while i < len(chars) and chars[i] == char:
                count += 1
                i += 1
            if count == 1:
                chars[k] = char
                k += 1
            else:
                chars[k] = char
                k += 1
                count = str(count)
                for w in count:
                    chars[k] = w
                    k += 1
                
        return k

        