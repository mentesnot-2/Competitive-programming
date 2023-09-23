"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict()
        for i in range(len(employees)):
         
            iD,imp,sub = employees[i].id,employees[i].importance,employees[i].subordinates
           
            graph[iD] = (imp,sub)
        ans = 0
        stack = [id]
        visited = set()
        while stack:
            val = stack.pop()
            imp,sub = graph[val]
            ans+=imp
            visited.add(val)
            if sub:
                for i in sub:
                    if i not in visited:
                        stack.append(i)
        return ans



        