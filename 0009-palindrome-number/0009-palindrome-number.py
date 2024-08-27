class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)
        x2 = ""
        for i in range(len(x1)-1,-1,-1):
            x2 += x1[i]
        return x2 == x1

        