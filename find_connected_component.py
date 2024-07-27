# find_connected_component
# 20180150127 김한탁
# 연결성분 검사 알고리즘

mygraph1={'A' : set(['B', 'C']),
       'B' : set(['A']),
       'C' : set(['A']),
       'D' : set(['E']),
       'E' : set(['D']),
       }

def find_connected_component(graph):
    visited = set()
    colorList=[]
   
    for vtx in graph:
        if vtx not in visited:
            color = dfs_cc(graph, [], vtx, visited)
            colorList.append(color)
            
    print("그래프 연결성분 개수 = %d " % len(colorList))
    print(colorList)

def dfs_cc(graph, color, vertex, visited):
    if vertex not in visited:
        visited.add(vertex)
        color.append(vertex)
        nbr = graph[vertex] - visited
        for v in nbr:
            dfs_cc(graph, color, v, visited)
    return color

print()
print('find_connected_component: ')
find_connected_component(mygraph1)