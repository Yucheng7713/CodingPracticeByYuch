class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed
        flowerbed.append(0)
        for i in range(1, len(flowerbed)-1):
            if n > 0 and flowerbed[i] == flowerbed[i-1] == flowerbed[i+1] == 0 :
                flowerbed[i] = 1
                n -= 1
            if n == 0: return True
        return True if n == 0 else False