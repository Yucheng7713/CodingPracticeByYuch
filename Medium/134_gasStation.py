class Solution:
    # Brute Force : TLE - Time limited exceed - O(N^2)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for start in range(n):
            # Try out all possible started indexes
            if gas[start] >= cost[start]:
                # Initially fill the tank
                tank = gas[start]
                previous, current = start, (start + 1) % n
                # Keep going until we reach back to the started index or
                # running out of gas.
                while current != start and tank - cost[previous] >= 0:
                    tank = tank - cost[previous] + gas[current]
                    previous = current
                    current = (current + 1) % n
                # If we can go back to the started index and have enough gas
                # Return the started index
                if current == start and tank - cost[previous] >= 0:
                    return start
        # Could not cycle back to any same index
        return -1

    def canCompleteCircuit_II(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total = current = 0
        start = 0
        for i in range(n):
            # Keep tracking of the total remaining gas
            total += gas[i] - cost[i]
            current += gas[i] - cost[i]
            # If current remaining gas < 0 at ith position
            # Set the new starting point at i + 1 position and reset the current gas
            if current < 0:
                start = i + 1
                current = 0
        return start if total >= 0 else -1

gas = [3, 3, 4]
cost = [3, 4, 4]
print(Solution().canCompleteCircuit(gas, cost))