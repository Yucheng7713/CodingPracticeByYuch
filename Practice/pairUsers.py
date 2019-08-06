import random

class UserPair:
    def randomPairUp(self, users):
        def pairGenerate():
            x = y = 0
            while x == y:
                x = random.randint(0,len(users)-1)
                y = random.randint(0,len(users)-1)
            usr_1, usr_2 = users[x], users[y]
            del users[x]
            if x < y:
                del users[y-1]
            else:
                del users[y]
            return tuple(sorted([usr_1, usr_2]))
        result = []
        while len(users) > 0:
            new_pair = pairGenerate()
            result.append(new_pair)
        return result

users = ["Andy", "Nickie", "Steven", "Maggie", "Ginger", "Jie", "Andrew", "Anthony", "John", "Sara", "Christy", "Stu"]
print(UserPair().randomPairUp(users[:]))
print(UserPair().randomPairUp(users))