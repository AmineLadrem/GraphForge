import sys
import time
sys.path.insert(0, './lib')

import networkx as nx
import matplotlib.pyplot as plt

class GrapheMatrice:
    def __init__(self, taille, oriente=False):
        self.taille = taille
        self.oriente = oriente
        self.matrice = [[0] * taille for _ in range(taille)]

    def ajouter_arete(self, u, v):
        self.matrice[u][v] = 1
        if not self.oriente:
            self.matrice[v][u] = 1 

    def ajouter_arc(self, u, v):
        self.matrice[u][v] = 1

    def afficher_matrice(self):
        for ligne in self.matrice:
            print(ligne)

    def afficher_graphe(self):
        G = nx.Graph() if not self.oriente else nx.DiGraph()
        G.add_nodes_from(range(self.taille))

        for u in range(self.taille):
            for v in range(self.taille):
                if self.matrice[u][v] == 1:
                    G.add_edge(u, v)

        nx.draw(G, with_labels=True)
        plt.show()
 

class GrapheListe:
    def __init__(self, taille, oriente=False):
        self.taille = taille
        self.oriente = oriente
        self.liste = {i: [] for i in range(taille)}

    def ajouter_arete(self, u, v):
        self.liste[u].append(v)
        if not self.oriente:
            self.liste[v].append(u)

    def ajouter_arc(self, u, v):
        self.liste[u].append(v)

    def afficher_liste(self):
        for noeud, voisins in self.liste.items():
            print(f'{noeud}: {voisins}')

    def afficher_graphe(self):
        G = nx.Graph() if not self.oriente else nx.DiGraph()
        for u, voisins in self.liste.items():
            for v in voisins:
                G.add_edge(u, v)

        nx.draw(G, with_labels=True)
        plt.show()