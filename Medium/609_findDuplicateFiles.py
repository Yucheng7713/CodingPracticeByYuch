class Solution:
    def findDuplicate(self, paths: 'List[str]') -> 'List[List[str]]':
        file_map = collections.defaultdict(list)
        for p in paths:
            record = p.split(' ')
            d_path = record[0]
            for f in record[1:]:
                f_name, _, f_content = f.partition('(')
                file_map[f_content[:-1]] += [d_path + '/' + f_name]
        return [path for path in file_map.values() if len(path) > 1]