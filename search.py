def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result


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

