class Solution:
    # BFS traversal
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        fill_queue = []
        filled_color = image[sr][sc]
        if newColor == filled_color: return image
        m, n = len(image), len(image[0])
        fill_queue.append((sr, sc))
        while fill_queue:
            r, c = fill_queue.pop(0)
            for adj_r, adj_c in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if adj_r > -1 and adj_r < m and adj_c > -1 and adj_c < n and image[adj_r][adj_c] == filled_color:
                    fill_queue.append((adj_r, adj_c))
            image[r][c] = newColor
        return image