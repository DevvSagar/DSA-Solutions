class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1   #constraints
        INT_MIN = -2**31      #constraints
        reversed_digit = 0
        org_x = x
        x = abs(x)
        while (x > 0):
            last_digit = x % 10
            x = x // 10
            reversed_digit = (reversed_digit * 10) + last_digit
        if org_x < 0:
            reversed_digit = reversed_digit * -1
        if reversed_digit > INT_MAX or reversed_digit < INT_MIN:
            return 0

        return reversed_digit

