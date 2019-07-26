class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alpha_list, num_list = list(), list()
        for log in logs:
            if log.split()[1].isnumeric():
                num_list.append(log)
            else:
                alpha_list.append(log)
        alpha_list.sort(key=lambda x: x.split()[0])
        # Place the higher priority sorting way to the end
        alpha_list.sort(key=lambda x: x.split()[1:])
        return alpha_list + num_list