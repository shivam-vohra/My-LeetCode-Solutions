class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        if (x < 0):
            rev = int("-" + str(abs(x))[::-1])
        else:
            rev = int(str(x)[::-1])
        if rev not in range(-2**31, 2**31):
            rev = 0
        return rev