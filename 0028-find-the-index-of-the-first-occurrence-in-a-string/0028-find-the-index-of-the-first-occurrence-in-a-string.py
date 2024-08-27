class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        position = 0
        check = int(len(needle))
        word = ""
        for i in range(len(haystack)):
            if haystack[i:check] == needle:
                position = i
                word += haystack[i:check]
                break
            else:
                check +=1

        if word != needle:
            return -1
        else:
            return position
        
        