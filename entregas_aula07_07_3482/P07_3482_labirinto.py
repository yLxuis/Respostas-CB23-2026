import random
from collections import deque

# QUESTÃO 1 - DFS interativo

def generate_maze(m, n, room=0, wall=1, cheese='.'):
    """Gera um labirinto perfeito de m X n células usando DFS iterativo."""

    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    stack = [(0, 0)]

    maze[1][1] = room

    while stack:

        x, y = stack[-1]

        shuffled_directions = directions.copy()
        random.shuffle(shuffled_directions)

        encontrou_vizinho = False

        for dx, dy in shuffled_directions:

            nx = x + dx
            ny = y + dy

            if (
                0 <= nx < m
                and 0 <= ny < n
                and maze[2 * nx + 1][2 * ny + 1] == wall
            ):

                maze[2 * x + 1 + dx][2 * y + 1 + dy] = room

                maze[2 * nx + 1][2 * ny + 1] = room

                stack.append((nx, ny))

                encontrou_vizinho = True

                break

        if not encontrou_vizinho:
            stack.pop()

    while True:

        i = random.randrange(1, 2 * m, 2)
        j = random.randrange(1, 2 * n, 2)

        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze


def print_maze(maze):
    """Imprime o labirinto no terminal."""

    for row in maze:
        print(" ".join(map(str, row)))


def find_cheese(maze, cheese='.'):
    """Procura a posição do queijo no labirinto."""

    for i in range(len(maze)):
        for j in range(len(maze[i])):

            if maze[i][j] == cheese:
                return (i, j)

    return None


def find_path(maze, start=(1, 1), cheese='.', wall=1):
    """Encontra o menor caminho até o queijo usando BFS."""

    goal = find_cheese(maze, cheese)

    if goal is None:
        return None

    # QUESTÃO 2 - BFS

    queue = deque([start])

    visited = {start}

    parent = {
        start: None
    }

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while queue:

        current = queue.popleft()

        if current == goal:
            break

        x, y = current

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if not (
                0 <= nx < len(maze)
                and 0 <= ny < len(maze[0])
            ):
                continue

            if maze[nx][ny] == wall:
                continue

            neighbor = (nx, ny)

            if neighbor in visited:
                continue

            visited.add(neighbor)

            parent[neighbor] = current

            queue.append(neighbor)

    if goal not in parent:
        return None

    path = []

    current = goal

    while current is not None:

        path.append(current)

        current = parent[current]

    path.reverse()

    return path


def print_path(maze, path, start=(1, 1), cheese='.'):
    """Imprime o labirinto destacando o caminho encontrado."""

    result = [
        row.copy()
        for row in maze
    ]

    if path is not None:

        for x, y in path:

            if result[x][y] != cheese:
                result[x][y] = '.'

    x, y = start
    result[x][y] = 'S'

    cheese_position = find_cheese(
        maze,
        cheese
    )

    if cheese_position is not None:

        x, y = cheese_position

        result[x][y] = 'Q'

    for row in result:
        print(" ".join(map(str, row)))

m = 10
n = 14

room = ' '
wall = 'W'
cheese = '*'

maze = generate_maze(
    m,
    n,
    room,
    wall,
    cheese
)

print("LABIRINTO")
print()

print_maze(maze)

path = find_path(
    maze,
    start=(1, 1),
    cheese=cheese,
    wall=wall
)

print()
print("CAMINHO ENCONTRADO")
print()

if path is None:

    print("Não foi possível encontrar um caminho até o queijo.")

else:

    print_path(
        maze,
        path,
        start=(1, 1),
        cheese=cheese
    )

    print()
    print("Comprimento do caminho:", len(path) - 1)