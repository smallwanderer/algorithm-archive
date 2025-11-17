def solution(arrows):
    from collections import defaultdict

    direction = [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
    ]
    visited_nodes = set()
    visited_edges = set()

    x, y = 0, 0
    visited_nodes.add((x, y))
    rooms = 0

    for arrow in arrows:
        for _ in range(2):
            dx, dy = direction[arrow]
            nx, ny = x + dx, y + dy

            if (x, y) < (nx, ny):
                edge = ((x, y), (nx, ny))
            else:
                edge = ((nx, ny), (x, y))

            if (nx, ny) in visited_nodes and edge not in visited_edges:
                rooms += 1

            visited_nodes.add((nx, ny))
            visited_edges.add(edge)

            x, y = nx, ny

    return rooms
