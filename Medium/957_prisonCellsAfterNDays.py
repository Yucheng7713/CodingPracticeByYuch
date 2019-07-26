class Solution:
    # Brute Force - TLE when N is extremely large
    # One probably might notice that when N is large enough > 256 = 2^8
    # A cycle exists
    # The question will be : how to detect the cycle ?
    def prisonAfterNDays_I(self, cells, N: int):
        n = len(cells)
        for i in range(N):
            change = [0] * 8
            for j in range(n):
                if (j == 0 or j == n - 1) and cells[j] == 1:
                    change[j] = 0
                elif cells[j - 1] == cells[j + 1]:
                    change[j] = 1
                else:
                    change[j] = 0
            cells = change
        return cells

    # Use hash map to store all the seen cells statuses.
    # The reason why decreasing N is because it's convenient to simply just mod N
    # instead increasing it.
    def prisonAfterNDays_II(self, cells: List[int], N: int) -> List[int]:
        seen = {}
        next_cells = cells
        while N:
            seen[tuple(next_cells)] = N
            N -= 1
            next_cells = [0] + [cells[j - 1] ^ cells[j + 1] ^ 1 for j in range(1, 7)] + [0]
            if tuple(next_cells) in seen:
                # If the next cells' state has been seen already -> that means we have reached the entry point of the cycle
                # The cycle length will be seen[tuple(next_cells)] - N
                N %= (seen[tuple(next_cells)] - N)
            cells = next_cells
        return cells

cells = [0,1,0,1,1,0,0,1]
n = 7
print(Solution().prisonAfterNDays_II(cells, n))