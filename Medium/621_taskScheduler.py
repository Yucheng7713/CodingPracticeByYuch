from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Since we need to sort the map -> use an array instead
        taskMap = [0] * 26
        # tracking the number of instances for each task
        for t in tasks:
            taskMap[ord(t) - ord('A')] += 1
        # Sort the map in ascending order
        taskMap.sort()
        time = 0
        # 若還有 pending 未執行的 instances
        while taskMap[-1] > 0:
            i = 0
            # keep tracking the interval n, make sure that each interval
            # between each priority task satisfies the constraint n
            while i <= n:
                # The rightmost task is executed completed
                # -> need to re-sort the map
                if taskMap[-1] == 0:
                    break
                # Execute other tasks for filling out the interval instead
                # being idle
                # The condition “i < 26" for preventing the case which the
                # interval is greater than 26.
                # For such case we definitely need to place some idles between
                # each instances
                if i < 26 and taskMap[25 - i] > 0:
                    taskMap[25 - i] -= 1
                time += 1
                i += 1
            taskMap.sort()
        return time
tasks = ["D","C","G","I","F","J","J","G","J","E","A","F","C","E","I","B","G","E","A","D","E","E","D","J","H","B","F","G","F","H","B","G","E","I","D","F","H","F","I","J","E","H","E","D","B","D","F","E","A","G","B","J","A","J","B","C","I","J","H","J","C","H","H","F","G","D","G","J","C","I","I","B","I","I","B","C","B","F","J","D","G","H","J","H","G","A","J","J","I","J","B","J","G","A","J","I","E","F","B","D","A","E","G","J","D","E","F","A","A","E","D","I","D","I","I","F","E","F","D","H","J","D","F","G","H","D","H","A","F","F","G","E","B","I","G","A","D","E","B","D","J","A","H","A","A","B","F","B","G","C","D","E","G","B","B","F","E","B","I","B","H","I","E","G","I","E","E","I","F","B","I","C","J","I","C","J","I","C","D","E","H","G","F","G","F","E","A","E","A","E","E","D","E","D","H","C","D","J","D","F","E","H","A","C","G","D","A","J","J","E","D","I","H","C","B","C","I","H","C","E","G","C","D","E","J","H","C","J","G","B","C","H","E","H","D","A","D","J","G","D","B","H","C","G","I","D","J","I","G","F","G","A","I","E","B","J","D","I","G","H","E","B","B","B","C","J","B","G","E","I","H","I","F","J","I","B","B","B","H","I","I","G","C","B","G","C","I","B","A","J","H","A","G","B","H","A","G","B","D","J","J","J","E","I","E","I","D","D","J","J","D","D","E","E","B","A","F","H","C","E","I","I","E","B","H","E","H","H","E","E","G","G","A","F","J","E","G","D","G","C","C","C","D","E","I","J","I","H","A","B","C","C","C","G","G","A","C","F","B","E","C","B","C","I","F","G","C","B","G","C","G","D","D","G","B","E","A","J","H","B","C","C","E","J","I","I","I","H","H","B","F","J","G","A","I","A","F","J","H","A","H","D","F","E","A","A","F","B","D","J","B","I","C","I","G","G","G","D","G","B","G","C","D","J","H","A","C","A","A","A","E","J","A","C","J","H","D","F","E","J","H","F","A","A","A","G","D","G","A","A","J","D","B","B","H","A","B","D","F","D","D","B","D","B","A","B","A","H","J","E","F","H","G","H","I","J","B","H","F","F","D","C","A","D","E","F","B","F","F","E","D","F","A","G","E","B","J","F","J","C","J","I","J","J","A","C","C","D","F","D","E","C","G","B","F","H","I","B","F","I","C","B","B","A","C","C","J","D","J","J","I","B","F","J","B","D","D","G","G","H","G","G","C","E","I","D","B","A","H","I","B","G","E","H","D","D","C","G","E","E","G","A","C","J","J","E","B","F","J","I","G","E","C","H","I","I","C","J","D","G","E","G","A","G","A","J","B","F","B","G","B","J","E","C","F","B","A","J","G","A","G","B","J","A","C","D","H","C","E","G","C","H","D","I","E","E","I","B","G","H","D","A","I","A","C","B","D","B","B","A","D","I","J","G","D","D","D","B","J","H","D","B","F","J","J","F","D","G","C","H","I","E","G","J","J","B","E","D","A","G","I","C","C","E","B","H","A","F","D","D","G","E","E","C","I","J","C","G","C","E","D","B","F","F","A","D","I","E","F","J","J","F","A","B","D","G","J","G","B","I","B","J","A","I","I","D","H","A","F","I","A","A","F","F","D","E","E","I","G","B","G","G","J","J","E","F","A","H","E","I","A","B","D","I","E","I","C","B","F","J","G","D","C","I","C","G","B","G","A","J","F","C","B","J","D","D","F","F","D","B","I","A","F","J","C","H","F","A","H","D","F","D","G","I","C","H","E","D","J","E","A","G","H","B","J","B","J","A","A","A","H","E","B","J","E","J","E","C","D","I","F","C","C","G","J","D","E","H","C","B","B","B","C","C","C","A","E","G","J","G","E","C","H","I","C","H","E","E","G","H","H","B","C","A","E","H","G","C","G","G","B","J","H","C","G","I","G","B","H","A","C","A","B","F","I","A","F","B","D","E","H","C","G","I","A","F","G","H","B","B","E","D","E","D","D","J","A","D","J","H","F","A","A","F","C","A","D","C","A","H","E","D","C","E","H","G","G","C","G","G","I","G","E","J","E","I","E","I","C","G","C","G","E","B","J","A","G","G","D","F","E","H","D","D","D","F","D","B","F","I","C","E","B","B","D","C","E","D","B","H","J","G","G","C","F","J","D","D","D","A","H","E","A","F","I","G","F","A","A","A","F","H","B","I","F","F","H","C","I","J","C","D","B","G","I","E","A","C","F","I","J","F","D","J","D","F","C","I","G","F","H","F","I","E","C","B","B","H","B","A"]
print(Solution().leastInterval(tasks,88))