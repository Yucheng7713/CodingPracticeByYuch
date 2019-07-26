class Solution(object):
    def totalFruit(self, tree):
        if tree == []:
            return 0
        slow = fast = max_fruit = 0
        temp = 0
        genre = []
        genre.append(tree[0])
        while fast < len(tree):
            if tree[fast] != tree[slow]:
                if tree[fast] not in genre and len(genre) < 2:
                    temp += 1
                    genre.append(tree[fast])
                else:
                    if tree[fast] in genre:
                        temp += 1
                    else:
                        temp = fast - slow + 1
                        genre = [tree[slow]]
                        genre.append(tree[fast])
                slow = fast
            else:
                temp += 1
            if max_fruit < temp:
                max_fruit = temp
            fast += 1
        return max_fruit

    def totalFruit(self, tree):
        if not tree: return 0
        s = 0
        current_num = ans = 1
        # The basket will only store 2 elements : represent 2 types of fruit
        baskets = [tree[0]]
        for f in range(1, len(tree)):
            if tree[f] not in baskets:
                # If there are already 2 types of fruits being collected
                if len(baskets) == 2:
                    # Keep the one which will be included into the next collection
                    baskets = [tree[s]]
                    # Update the number of collected fruits
                    current_num = f - s
                # Include new collected fruit
                baskets += [tree[f]]
            # Update the tracking pointers
            if tree[s] != tree[f]:
                s = f
            current_num += 1
            ans = max(ans, current_num)
        return ans

s = Solution()
f_trees = [1,2,3]
f_trees_a = [0,1,2,2]
f_trees_b = [1,2,3,2,2]
f_trees_c = [3,3,3,1,2,1,1,2,3,3,4]
f_trees_d = [1,0,1,4,1,4,1,2,3]
print(s.totalFruit(f_trees_d))

