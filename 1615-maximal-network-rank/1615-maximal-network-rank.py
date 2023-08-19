class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        network = collections.defaultdict(set)

        for a,b in roads:
            network[a].add(b)
            network[b].add(a)

        res = 0
       
        for c1,c2 in itertools.combinations(network.keys(),2):
            conn = 1 if c1 in network[c2] else 0
            res = max(res,len(network[c1]) + len(network[c2]) - conn)
        return res