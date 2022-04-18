
def findLCM(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return a