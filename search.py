def dfs(graph):
    visited = set()
    nodes = sorted(graph.keys())
    stack = []

    for node in nodes:
        if node not in visited:
            stack.append(node)
            while stack:
                n = stack.pop()
                if n in visited:
                    continue
                print(n)
                visited.add(n)
                if n in graph:
                    for nbr in reversed(graph[n]):
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

