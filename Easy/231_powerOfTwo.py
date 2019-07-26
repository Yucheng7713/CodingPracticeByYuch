class Solution:
    def isPowerOfTwo(self, n: 'int') -> 'bool':
        if n <= 0:
            return False
        return len([digit for digit in bin(n) if digit == '1']) == 1