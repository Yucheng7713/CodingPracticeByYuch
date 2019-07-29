class Solution:
    # Brute Force - Swap and check the maximum
    # Time complexity : O (N^3) - Nested iteration and for each swapped integer we spend O(N) time to check if the current maximum is updated
    # Space complexity : O (N) - the stored list
    def maximumSwap_I(self, num: int) -> int:
        # Since String is immutable in Python, we need to convert the integer into list
        str_num = list(str(num))
        max_num = num
        def swap(i, j):
            str_num[i], str_num[j] = str_num[j], str_num[i]
        for i in range(len(str_num)):
            for j in range(i+1, len(str_num)):
                swap(i, j)
                max_num = max(max_num, int("".join(str_num)))
                swap(i, j)
        return max_num

    # Greedy
    # Time complexity : O ()
    # Space complexity : O ()
    def maximumSwap_II(self, num: int) -> int:
        str_num = []
        for n in str(num):
            str_num.append(int(n))
        num_map = {x: i for i, x in enumerate(str_num)}

        for i, v in enumerate(str_num):
            # Check starting from 9 since it is the maximum value for single digit
            for j in range(9, v, -1):
                if j in num_map and num_map[j] > i:
                    # If there is any larger digit in later order, swap it to the front
                    # And since we are only allowed to swap once, so after a swap is made
                    # we can simply return the swapped value (it is guaranteed to be the maximum value )
                    str_num[i], str_num[num_map[j]] = str_num[[num_map[j]], str_num[i]
                    return int("".join(map(str, str_num)))
        return num

print(Solution().maximumSwap_II(2736))


