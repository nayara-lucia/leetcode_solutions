class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = [i for i in s.split() if i!= ""]
        return len(last[-1])
        