import sys

class Pattern:
    def squareDiagnalTLtoRB(self, n):
        count = 1
        map = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            k = 0
            for j in range(i, n):
                map[k][j] = str(count)
                count += 1
                k += 1
        for i in range(n):
            for j in range(n):
                sys.stdout.write(str(map[i][j]) + ', ')
            sys.stdout.write('\n')

    def squareDiagnalRBtoTL(self, n):
        count = 1
        map = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            k = n - 1
            for j in range(i, -1, -1):
                map[j][k] = str(count)
                count += 1
                k -= 1
        for i in range(n):
            for j in range(n):
                sys.stdout.write(str(map[i][j]) + ', ')
            sys.stdout.write('\n')


Pattern().squareDiagnalRBtoTL(5)