import networkx as nx  
import matplotlib.pyplot as plt

# Завдання 1: Будуємо граф
G = nx.Graph()
G.add_nodes_from(["Router1", "Switch1", "PC1", "PC2", "PC3", "Server1"])  
G.add_edge("Router1", "Switch1")   
G.add_edge("Switch1", "PC1") 
G.add_edge("Switch1", "PC2")   
G.add_edge("Switch1", "PC3")
G.add_edge("Router1", "Server1")  

# Завдання 2: Алгоритми BFS і DFS 
print("DFS:", list(nx.dfs_preorder_nodes(G, source="Router1")))
print("BFS:", list(nx.bfs_tree(G, source="Router1").edges))

# Завдання 3: Найкоротші шляхи
G.add_edge("Router1", "Switch1", weight=2) 
G.add_edge("Switch1", "PC1", weight=1)  
G.add_edge("Switch1", "PC2", weight=3)
G.add_edge("Switch1", "PC3", weight=1) 
G.add_edge("Router1", "Server1", weight=5) 

path = nx.dijkstra_path(G, "Router1", "Server1") 
print("Shortest path:", path)  

# Візуалізація  
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edges(G, pos, edgelist=[("Router1", "Switch1"), ("Switch1", "Server1")], edge_color="r")
plt.show()