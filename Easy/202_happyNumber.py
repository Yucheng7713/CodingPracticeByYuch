class Solution:
    def isHappy(self, n):
        happy_hash = dict()
        sqrt_sum = -1
        while not happy_hash.get(sqrt_sum, False):
            happy_hash[sqrt_sum] = True
            sqrt_sum = 0
            while n != 0:
                sqrt_sum += (n % 10) ** 2
                n = n // 10
            if sqrt_sum == 1:
                return True
            n = sqrt_sum
        return False