#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        if targetWord not in wordList:
            return []

        answer = []
        shortest_found = False
        shortest_len = 0

        pattern_map = defaultdict(list)
        L = len(startWord)

        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

        queue = deque([(startWord, [startWord])])
        visited = set([startWord])

        while queue and not shortest_found:
            level_visited = set()
            length = len(queue)

            for _ in range(length):
                node, node_list = queue.popleft()

                for i in range(L):
                    pattern = node[:i] + "*" + node[i+1:]

                    for neighbour in pattern_map[pattern]:
                        if neighbour == targetWord:
                            answer.append(node_list + [targetWord])
                            shortest_found = True

                        elif neighbour not in visited:
                            level_visited.add(neighbour)
                            new_path = node_list + [neighbour]
                            queue.append((neighbour, new_path))

            visited.update(level_visited)
        return answer
