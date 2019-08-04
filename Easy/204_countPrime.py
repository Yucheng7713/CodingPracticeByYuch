from math import floor, sqrt

class Solution(object):

    # Check each number which is smaller than the square of n - TLE
    # Time compleixty :  O(sqrt(n)*n)
    # Space complexity : O(1)
    def countPrimes(self, n: int) -> int:
        def isPrime(n):
            k = floor(sqrt(n))
            for i in range(2, k + 1):
                if n % i == 0:
                    return False
            return True

        count = 0
        for i in range(2, n + 1):
            if isPrime(i):
                count += 1
        return count

    # Use a list and unmark all non-prime numbers then sum them up
    # Time complexity : O(n^2) ??
    # Space complexity : O(n)
    def countPrimes_II(self, n):
        if n < 3:
            return 0
        nums = [True] * n
        nums[0] = nums[1] = False
        for i in range(2, n):
            if nums[i]:
                # Record all prime numbers
                # !! Need to clarify why need to use (n - 1)
                time_range = (n - 1)//i + 1
                # Increase j by its multiplication
                for j in range(2, time_range):
                    nums[i * j] = False
        return sum(nums)


    def countPrimes_III(self, n: int) -> int:
        if n < 2: return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, n):
            if primes[i]:
                # Increase j by its multiplication
                for j in range(i ** 2, n, i):
                    primes[j] = False
        return sum(primes)

s = Solution()
print(s.countPrimes_III(100))