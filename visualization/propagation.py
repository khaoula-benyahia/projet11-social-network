import networkx as nx

# --- ÉTAPE 1 : Préparation du Graphe ---
# Charger les données à nouveau pour créer l'objet Graphe
G = nx.read_edgelist('facebook_combined.txt')

# --- ÉTAPE 2 : Simulation de propagation (BFS) ---
# On choisit l'utilisateur '0' comme point de départ (Seed)
seed_node = '0'

# Simulation d'une propagation sur 2 niveaux (amis, puis amis des amis)
# On utilise l'algorithme BFS (Breadth-First Search)
propagation_path = list(nx.bfs_edges(G, source=seed_node, depth_limit=2))

# --- ÉTAPE 3 : Analyse des résultats ---
nodes_reached = set()
for u, v in propagation_path:
    nodes_reached.add(u)
    nodes_reached.add(v)

print(f"📢 Résultat de la propagation depuis l'utilisateur {seed_node}:")
print(f"✅ Nombre de personnes touchées en 2 étapes : {len(nodes_reached)}")