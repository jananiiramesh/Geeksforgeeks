from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(words: List[str]) -> str:
        unique_chars = set("".join(words))
        char_to_index = {ch: idx for idx, ch in enumerate(sorted(unique_chars))}
        index_to_char = {idx: ch for ch, idx in char_to_index.items()}
        K = len(unique_chars)
        
        graph = defaultdict(list)
        in_degree = [0] * K
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            length = min(len(w1), len(w2))
            found_diff = False
            
            for j in range(length):
                if w1[j] != w2[j]:
                    f = char_to_index[w1[j]]
                    t = char_to_index[w2[j]]
                    found_diff = True
                    graph[f].append(t)
                    in_degree[t] += 1
                    break
                
            if not found_diff and len(w1) > len(w2):
                return ""
                
        queue = deque([i for i in range(K) if in_degree[i] == 0])
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(index_to_char[node])
            for neighbour in graph[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
                    
        if len(topo_order) != K:
            return ""
        
        return "".join(topo_order)
