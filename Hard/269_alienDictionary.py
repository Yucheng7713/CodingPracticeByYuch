import collections

class Solution:
    # Topological sort - Kahn's algorithm
    def alienOrder(self, words) -> str:
        graph = collections.defaultdict(set)
        indegrees = collections.defaultdict(int)
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in graph:
                    graph[words[i][j]] = set()
                    indegrees[words[i][j]] = 0
        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]
            for j in range(min(len(word_1), len(word_2))):
                if word_1[j] != word_2[j]:
                    if word_2[j] not in graph[word_1[j]]:
                        graph[word_1[j]].add(word_2[j])
                        indegrees[word_2[j]] += 1
                    break
        queue = collections.deque([c for c, d in indegrees.items() if d == 0])
        result = ""
        while queue:
            alien_ch = queue.pop()
            result += alien_ch
            for adj_ch in graph[alien_ch]:
                indegrees[adj_ch] -= 1
                if indegrees[adj_ch] == 0:
                    queue.appendleft(adj_ch)
        # If all characters has been traversed -> a valid topology
        return result if len(graph) == len(result) else ""

    def alienOrder_II(self, words) -> str:
        graph = collections.defaultdict(set)
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in graph:
                    graph[words[i][j]] = set()
        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]
            for j in range(min(len(word_1), len(word_2))):
                if word_1[j] != word_2[j]:
                    if word_2[j] not in graph[word_1[j]]:
                        graph[word_1[j]].add(word_2[j])
                    break

        def topologicalSortUtil(v, stack, visited, visiting):
            visited.add(v)
            visiting.add(v)
            for adj_v in graph[v]:
                if adj_v in visiting:
                    return True
                if adj_v not in visited:
                    if topologicalSortUtil(adj_v, stack, visited, visiting):
                        return True
            # finish visiting v, remove v
            # since there might be multiple single-direction path
            visiting.remove(v)
            stack.append(v)
            return False

        visited = set()
        stack = []
        for v in graph:
            if v not in visited:
                if topologicalSortUtil(v, stack, visited, set()):
                    return ""
        return "".join(stack[::-1])


dicts = ["wrt","wrf","er","ett","rftt"]
print(Solution().alienOrder_II(dicts))