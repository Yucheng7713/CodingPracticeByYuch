class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        e_times = [0] * n
        t_stack = []
        prev_time = 0
        for log in logs:
            fn, s_e, time = log.split(':')
            fn, time = int(fn), int(time)
            if s_e == 'start':
                if t_stack:
                    e_times[t_stack[-1]] += time - prev_time
                t_stack.append(fn)
                prev_time = time
            else:
                e_times[t_stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return e_times

print(Solution().exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))