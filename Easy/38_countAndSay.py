class Solution(object):
    def countAndSay(self, n):
        say = "1"
        next_say = ""
        for i in range(n - 1):
            count = 1
            for j in range(len(say)):
                try:
                    if say[j] == say[j+1]:
                        # When same number appear consecutively
                        count += 1
                    else:
                        # When the roll count breaks
                        next_say += str(count) + say[j]
                        count = 1
                except:
                    # Handling the case when j+1 is out of index of the string
                    next_say += str(count) + say[j]
            # Pass the new count-say to next iteration and initialize
            say = next_say
            next_say = ""
        return say

s = Solution()
print(s.countAndSay(5))