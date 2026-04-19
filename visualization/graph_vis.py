from pyvis.network import Network
import networkx as nx

# --- ÉTAPE 1 : Création du Graphe NetworkX ---
# On charge un échantillon (sample) pour que le rendu soit fluide
G_full = nx.read_edgelist('facebook_combined.txt')
# Pour la visualisation, on prend les 100 premières connexions pour tester
G_sample = nx.Graph(list(G_full.edges())[:100])

# --- ÉTAPE 2 : Conversion vers Pyvis ---
net = Network(notebook=False, height='750px', width='100%', bgcolor='#222222', font_color='white')
net.from_nx(G_sample)

# --- ÉTAPE 3 : Personnalisation et Génération ---
net.show_buttons(filter_=['physics']) # Ajouter des contrôles pour l'animation
print("🌐 Génération du graphe interactif...")
net.show('facebook_graph.html', notebook=False)