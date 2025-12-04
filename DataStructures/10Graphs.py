#Graphs
'''
1.Graph is a data structure , which is a derived concept from mathematics
2.Graph is a collection of vertices and edges.Vertices represents data and edges represents

'''

#BFS - Breadth-first-search
'''
It is an algorithm to trace the nodes of the graph in a breadth-first order
that is the neighboring nodes in a single level are tracersed first,
then the nodes in the next level are traversed
'''
'''
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node,end = " ")

        for neighbore in graph[node]:
            if neighbore not in visited:
                visited.add(neighbore)
                queue.append(neighbore)


graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

print("BFS Traversal:")
bfs(graph, 'A')
'''

#DFS - depth-first search
'''
It is an algorithm to trace the nodes of the graph in a depth-first order.
the node in one depth are traversed first,then the nodes in the parallel are traversed.
it uses the concept of back-tracking after one vertical depth node is traversed.

'''

'''
def dfs(graph,node,visited =None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)

            
graph = {
    'A':['b','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}


print("DFS Traversal:")
dfs(graph, 'A')

'''































