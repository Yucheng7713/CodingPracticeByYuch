class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        dp = [0] * (len(questions) + 1)

        for i in range(len(questions) - 1, -1, -1):
            next_q = i + questions[i][1] + 1
            # If the next question is available even solving question i.
            if next_q < len(questions):
                dp[i] = max(questions[i][0] + dp[next_q], dp[i + 1])
            else:
                dp[i] = max(questions[i][0], dp[i + 1])

        return dp[0]