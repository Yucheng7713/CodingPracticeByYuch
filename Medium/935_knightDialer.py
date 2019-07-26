# Naive recursive counting
# TLE
# Time complexity : O ( 2^N )
class Solution_1:
    def __init__(self):
        self.move = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
    def hop(self, dial_nums, N):
        # If we have hopped the required steps
        if N == 0:
            return len(dial_nums)
        # Recursively accumulate number of paths
        d_seq = 0
        for d in dial_nums:
            d_seq += self.hop(self.move[d], N - 1)
        return d_seq

    def knightDialer(self, N: int) -> int:
        # Base case
        if N == 1:
            return 10
        return self.hop([i for i in range(10)], N - 1)

# recursion + memoization
# TLE at around 4000 hops
class Solution_2:
    def __init__(self):
        self.move = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        self.d_map = {}

    def hop(self, starting_pos, N):
        if (starting_pos, N) in self.d_map:
            return self.d_map[(starting_pos, N)]
        if N == 0:
            # Base case : If we have hopped the required steps
            return 1
        else:
            # Recursively accumulate number of paths
            d_seq = 0
            for d in self.move[starting_pos]:
                d_seq += self.hop(d, N - 1)
            self.d_map[(starting_pos, N)] = d_seq
            return d_seq

    def knightDialer(self, N: int) -> int:
        dial_nums = 0
        for i in range(10):
            dial_nums += self.hop(i, N - 1)
        return dial_nums % (10 ** 9 + 7)

# Dynamic Programming
class Solution_3:
    def knightDialer(self, N: int) -> int:
        mod = (10 ** 9 + 7)
        neighbors = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        prev_dials = [1] * 10
        current_dials = [0] * 10
        for i in range(N - 1):
            current_dials = [0] * 10
            for j in range(10):
                for n in neighbors[j]:
                    current_dials[j] += prev_dials[n]
            prev_dials = current_dials
        return sum(prev_dials) % mod

print(Solution_3().knightDialer(161))




