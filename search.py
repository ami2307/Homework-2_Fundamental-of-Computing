def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  
    visited.add(start)
    print(start)
    for neighbor in graph[start]:  
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


g = {1: [3, 2], 2: [], 3: [2, 4], 4: [3]}
dfs(g)



def bfs(graph):
    visited = set()
    nodes = sorted(graph.keys())
    queue = []

    for node in nodes:
        if node not in visited:
            queue.append(node)
            while queue:
                n = queue.pop(0)
                if n in visited:
                    continue
                print(n)
                visited.add(n)
                if n in graph:
                    for nbr in graph[n]:
                        if nbr not in visited:
                            queue.append(nbr)

