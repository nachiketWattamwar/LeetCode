# LeetCode
Q)Factorial trailing zero.

Runtime: 44ms

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        multiply = 5
        count5 = 0
        while multiply <= n:
            count5 += n//multiply
            print("count5 ",count5)
            multiply *= 5
            print("multi ",multiply)
        return count5
        




