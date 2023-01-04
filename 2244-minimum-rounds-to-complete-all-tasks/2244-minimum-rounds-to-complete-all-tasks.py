class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        task=Counter(tasks)
        count=0
        for i in task.values():
            if i==1:
                return -1
            count+=(i+2)//3
        return count
            
        