def dfs(graph):
    visited = set()
    nodes = sorted(graph.keys())

    for start_node in nodes:
        if start_node not in visited:
            stack = [start_node]

            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                print(node)
                visited.add(node)
                if node in graph:
                   for nbr in sorted(graph[node], reverse=True):
                    if nbr not in visited:
                        stack.append(nbr)


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

