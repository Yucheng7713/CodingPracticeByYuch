class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        A_area, B_area = (C - A) * (D - B), (G - E) * (H - F)
        if A > G or B > H or E > C or F > D: return A_area + B_area
        width = height = 0
        if A < E and G > C:
            width = C - E
        elif A > E and G < C:
            width = G - A
        else:
            width = min(C - A, G - E)
        if H < D and B > F:
            height = H - B
        elif H > D and B < F:
            height = D - F
        else:
            height = min(D - B, H - F)

        return A_area + B_area - (width * height)