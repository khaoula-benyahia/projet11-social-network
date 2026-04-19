import networkx as nx

# --- ÉTAPE 1 : Chargement du réseau ---
G = nx.read_edgelist('facebook_combined.txt')

# --- ÉTAPE 2 : Calcul du degré de chaque nœud ---
# Le degré est le nombre d'amis de chaque utilisateur
degrees = dict(G.degree())

# --- ÉTAPE 3 : Identifier les comptes suspects (Bots) ---
# On considère comme "Bot" tout compte ayant plus de 200 amis (seuil à tester)
threshold = 200
bots = [node for node, degree in degrees.items() if degree > threshold]

print(f"⚠️ Analyse des comportements suspects :")
print(f"✅ Nombre de comptes identifiés comme potentiels 'Bots' : {len(bots)}")
print(f"🆔 Liste des IDs suspects : {bots[:10]}...")