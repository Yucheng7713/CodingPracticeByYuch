class Solution:
    def formulatedStr(self, ver_str):
        v_list = []
        for ver_num in ver_str.split('.'):
            v_list += [int(ver_num)]
        return v_list
    def compareVersion(self, version1: 'str', version2: 'str') -> 'int':
        v1_list, v2_list = self.formulatedStr(version1), self.formulatedStr(version2)
        l1, l2 = len(v1_list), len(v2_list)
        if l1 < l2:
            v1_list += ([0] * (l2 - l1))
        elif l2 < l1:
            v2_list += ([0] * (l1 - l2))
        for i in range(len(v1_list)):
            if v1_list[i] < v2_list[i]:
                return -1
            elif v2_list[i] < v1_list[i]:
                return 1
        return 0
v1, v2 = "01", "1"
print(Solution().compareVersion(v1, v2))