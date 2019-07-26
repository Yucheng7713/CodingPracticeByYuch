import sys

class Multiplication:
    def split_at(self, num, m):
        return int(str(num)[:-m]), int(str(num)[-m:])

    def karatsuba_Multiplication(self, x, y):
        if x < 10 or y < 10:
            return x * y
        m = min(len(str(x)), len(str(y))) // 2
        a, b = self.split_at(x, m)
        c, d = self.split_at(y, m)
        z0 = self.karatsuba_Multiplication(a, c)
        z1 = self.karatsuba_Multiplication(b, d)
        z2 = self.karatsuba_Multiplication(a + b, c + d)
        return z0 * 10**(m * 2) + (z2 - z1 - z0) * 10**m + z1

a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627
print(Multiplication().karatsuba_Multiplication(a, b))