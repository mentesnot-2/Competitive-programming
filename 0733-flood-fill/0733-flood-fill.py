class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source = image[sr][sc]
        if color == source: return image
        def dfs(sr,sc):
            if image[sr][sc] == source:
                image[sr][sc] = color
           
                if sr >= 1:
                    dfs(sr - 1,sc)
                if sr + 1 < len(image):
                    dfs(sr + 1,sc)
                if sc >= 1:
                    dfs(sr,sc - 1)
                if sc + 1 < len(image[0]):
                    dfs(sr ,sc + 1)
            return image
        return dfs(sr,sc)
        