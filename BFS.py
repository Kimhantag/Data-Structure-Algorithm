# BFS
# 20180150127 김한탁
# 너비우선탐색(BFS)

import collections

mygraph={'A' : set(['B', 'C']),
       'B' : set(['A', 'D']),
       'C' : set(['A', 'D', 'E']),
       'D' : set(['B', 'C', 'F']),
       'E' : set(['C', 'G', 'H']),
       'F' : set(['D']),
       'G' : set(['E', 'H']),
       'H' : set(['E', 'G'])}

def bfs(graph, start):
    visited = set([start])
    queue = collections.deque([start])
    while queue:
        vertex =queue.popleft()
        print(vertex, end=' ')
        nbr = graph[vertex]-visited
        for v in nbr:
            visited.add(v)
            queue.append(v)
            
bfs(mygraph, 'A')