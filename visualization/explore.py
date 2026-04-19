import pandas as pd
import networkx as nx

# --- ÉTAPE 1 : Chargement des données ---
# Assurez-vous que le fichier 'facebook_combined.txt' est dans le dossier principal du projet
file_path = 'facebook_combined.txt'

try:
    # Lecture du fichier : les colonnes sont séparées par des espaces
    # source : l'utilisateur de départ, target : l'utilisateur avec qui il est connecté
    df = pd.read_csv(file_path, sep=' ', names=['source', 'target'])
    
    print("✅ Données chargées avec succès !")
    print(f"📊 Nombre total de relations (Edges) : {len(df)}")
    print(f"👤 Nombre d'utilisateurs uniques (Nodes) : {pd.concat([df['source'], df['target']]).nunique()}")

    # --- ÉTAPE 2 : Création du Graphe avec NetworkX ---
    # Cette étape est essentielle pour les analyses de semaine 1
    G = nx.from_pandas_edgelist(df, source='source', target='target')

    # Affichage des informations de base sur le réseau
    print("\n🌐 Résumé du réseau social :")
    print(f"- Type de graphe : {type(G)}")
    print(f"- Nombre de nœuds : {G.number_of_nodes()}")
    print(f"- Nombre de liens : {G.number_of_edges()}")

    # --- ÉTAPE 3 : Aperçu des 5 premières lignes ---
    print("\n📋 Aperçu des premières relations :")
    print(df.head())

except FileNotFoundError:
    print(f"❌ Erreur : Le fichier '{file_path}' est introuvable.")
    print("💡 Conseil : Téléchargez le fichier depuis SNAP Stanford et placez-le à côté de votre dossier 'VISUALIZATION'.")