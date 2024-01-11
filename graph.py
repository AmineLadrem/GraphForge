import sys
import time
sys.path.insert(0, './lib')

import networkx as nx
import matplotlib.pyplot as plt

class Graphe:
    def __init__(self, memType, taille, oriente=False):
        self.taille = taille
        self.oriente = oriente
        self.memType = memType

        if self.memType == 'matrice':
            self.graphe = [[0] * taille for _ in range(taille)]
        elif self.memType == 'liste':
            self.graphe = {i: [] for i in range(taille)}

    def ajouter_arete(self, u, v):
        if self.memType == 'matrice':
            self.graphe[u][v] = 1
            if not self.oriente:
                self.graphe[v][u] = 1
        elif self.memType == 'liste':
            self.graphe[u].append(v)
            if not self.oriente:
                self.graphe[v].append(u)

    def ajouter_arc(self, u, v):
        if self.memType == 'matrice':
            self.graphe[u][v] = 1
        elif self.memType == 'liste':
            self.graphe[u].append(v)


    def afficher_graphe(self):
        G = nx.Graph() if not self.oriente else nx.DiGraph()
        if self.memType == 'matrice':
            G.add_nodes_from(range(self.taille))
            for u in range(self.taille):
                for v in range(self.taille):
                    if self.graphe[u][v] == 1:
                        G.add_edge(u, v)
        elif self.memType == 'liste':
            for u, voisins in self.graphe.items():
                for v in voisins:
                    G.add_edge(u, v)
        nx.draw(G, with_labels=True)
        plt.show()

    def afficher(self):
        if self.memType == 'liste':
            for noeud, voisins in self.graphe.items():
                print(f'{noeud}: {voisins}')
        elif self.memType == 'matrice':
            for ligne in self.graphe:
                print(ligne)

    def calculer_densite(self):
        if self.oriente:  # Directed graph
         max_edges = self.taille * (self.taille - 1)
        else:  # Undirected graph
         max_edges = self.taille * (self.taille - 1) / 2

        if self.memType == 'liste':
         num_edges = sum(len(voisins) for voisins in self.graphe.values())
        elif self.memType == 'matrice':
         num_edges = sum(sum(1 for v in ligne if v != 0) for ligne in self.graphe)

        if self.oriente == False:  # For undirected graph, each edge is counted twice
         num_edges /= 2

        print(num_edges / max_edges if max_edges > 0 else 0)


    def calculer_degre(self, node):
     if self.memType == 'liste':
        print(len(self.graphe[node]))
     elif self.memType == 'matrice':
        print(sum(1 for v in self.graphe[node] if v != 0))

    def calculer_degre_total(self):
     print(sum(self.calculer_degre(node) for node in range(self.taille)))

def create_graph():
    type_graphe = -1
    while type_graphe not in [0, 1]:
        type_graphe = int(input("Type de graphe (0 pour non orienté, 1 pour orienté) : "))

    memType = -1
    while memType not in [0, 1]:
        memType = int(input("Type de représentation en mémoire (0 pour matrice, 1 pour liste) : "))
    memType = 'matrice' if memType == 0 else 'liste'

    nombre_noeuds = int(input("Nombre de nœuds dans le graphe : "))

    graphe = Graphe(memType, nombre_noeuds, oriente=(type_graphe == 1))

    if type_graphe == 0:
        aretes = input("Liste des arêtes (chaque arête doit être un couple de nœuds sans espace, et chaque arête séparée par une virgule) : ").split(',')
        for arete in aretes:
            u, v = map(int, [arete[0], arete[1]])  
            graphe.ajouter_arete(u, v)
    else:
        arcs = input("Liste des arcs (chaque arc doit être un couple de nœuds sans espace, et chaque arc séparé par une virgule) : ").split(',')
        for arc in arcs:
            u, v = map(int, [arc[0], arc[1]])  # Split the arc string into two separate values
            graphe.ajouter_arc(u, v)
  
    return graphe