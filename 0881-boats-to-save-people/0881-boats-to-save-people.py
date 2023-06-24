class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        boats = 0
        print(people)
        while right >= left:
            if people[right] + people[left] > limit:
                right-=1
            # elif people[right] + people[left] <= limit:
            else:
                left+=1
                right-=1
            boats+=1
        return boats
        