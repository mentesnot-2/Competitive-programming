class Solution:
    
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        res = 0
        st = 0
        end = 0
        clips.sort()
        i = 0
        while st < time:
            while i < len(clips) and clips[i][0] <= st:
                end = max(end, clips[i][1])
                i += 1
            if st == end:
                return -1
            st = end
            res += 1
        return res
