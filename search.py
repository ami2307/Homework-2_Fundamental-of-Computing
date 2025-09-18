def dfs(graph, start, visited=None, output=None):
    if visited is None:
        visited = set()
    if output is None:
        output = []
    visited.add(start)
    output.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, output)
    return output

graph = {0: [4], 1: [0, 1, 2], 2: [0], 3: [0, 1, 2, 4], 4: [3]}
order = dfs(graph, 0)
for node in order:
    print(node)


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

