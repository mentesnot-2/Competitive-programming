class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = [False] * n
        seen[0] = True
        stack = [0]

        while stack:
            node = stack.pop()
            for i in rooms[node]:
                if not seen[i]:
                    seen[i] = True
                    stack.append(i)
        return all(seen)

            
            