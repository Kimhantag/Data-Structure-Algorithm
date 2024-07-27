# DFS
# 20180150127 김한탁
# 깊이우선탐색(DFS) 

import collections

mygraph={'A' : set(['B', 'C']),
       'B' : set(['A', 'D']),
       'C' : set(['A', 'D', 'E']),
       'D' : set(['B', 'C', 'F']),
       'E' : set(['C', 'G', 'H']),
       'F' : set(['D']),
       'G' : set(['E', 'H']),
       'H' : set(['E', 'G'])}

def dfs(graph, start, visited=set()):
    if start not in visited :
        visited.add(start)
        print(start, end=' ')
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)
                      
dfs(mygraph, 'A')

                    