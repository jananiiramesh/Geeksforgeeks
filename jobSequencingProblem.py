class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        max_deadline = max(deadline)
        jobs = list(zip(deadline, profit))
        jobs.sort(key=lambda x: x[1], reverse=True)

        parent = [i for i in range(max_deadline + 1)]

        def find(t):
            if parent[t] != t:
                parent[t] = find(parent[t])
            return parent[t]

        def union(u, v):
            parent[u] = v

        max_jobs = 0
        max_profit = 0

        for d, p in jobs:
            available_slot = find(d)
            if available_slot > 0:
                union(available_slot, available_slot - 1)
                max_jobs += 1
                max_profit += p

        return [max_jobs, max_profit]
