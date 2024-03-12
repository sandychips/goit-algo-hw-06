import networkx as nx
import matplotlib.pyplot as plt

# Завдання 1: Створення та візуалізація графа

# Створюємо граф
G = nx.Graph()

# Додамо вершини
G.add_nodes_from([1, 2, 3, 4, 5])

# Додамо ребра та їх ваги
G.add_edge(1, 2, weight=3)
G.add_edge(1, 3, weight=5)
G.add_edge(2, 3, weight=2)
G.add_edge(2, 4, weight=7)
G.add_edge(3, 4, weight=1)
G.add_edge(4, 5, weight=4)

# Візуалізуємо граф
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold')
plt.title('Граф')
plt.show()

# Аналіз характеристик графа
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Список вершин:", list(G.nodes()))
print("Список ребер:", list(G.edges()))

# Завдання 2: DFS та BFS

# Функція для DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for next_node in graph[start]:
        if next_node not in visited:
            dfs(graph, next_node, visited)

# Функція для BFS
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for next_node in graph[node]:
            if next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)

print("\nDFS шляхи:")
dfs_paths = dfs(G, 1)
print("\nBFS шляхи:")
bfs_paths = bfs(G, 1)

# Завдання 3: Алгоритм Дейкстри

# Знаходимо найкоротший шлях між усіма парами вершин
shortest_paths = nx.shortest_path(G, weight='weight')

print("\nНайкоротші шляхи між усіма парами вершин:")
for source in shortest_paths:
    for target in shortest_paths[source]:
        if source != target:
            path = shortest_paths[source][target]
            distance = nx.shortest_path_length(G, source=source, target=target, weight='weight')
            print(f"Шлях з {source} до {target}: {path}, Довжина: {distance}")
