# bfsST
# 20180150127 김한탁
# 신장 트리 알고리즘

import collections

mygraph={'A' : set(['B', 'C']),
       'B' : set(['A', 'D']),
       'C' : set(['A', 'D', 'E']),
       'D' : set(['B', 'C', 'F']),
       'E' : set(['C', 'G', 'H']),
       'F' : set(['D']),
       'G' : set(['E', 'H']),
       'H' : set(['E', 'G'])}

def bfsST(graph, start):
    visited = set([start])
    queue= collections.deque([start])
    while queue:
        v = queue.popleft()
        nbr = graph[v] - visited
        for u in nbr:
            print("(", v, ",", u, ")", end="")
            visited.add(u)
            queue.append(u)

print()
bfsST(mygraph, 'A')
