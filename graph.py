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
            self.matrice[v][u] = 1  # Si le graphe est non orienté

    def ajouter_arc(self, u, v):
        self.matrice[u][v] = 1

    def afficher_matrice(self):
        for ligne in self.matrice:
            print(ligne)

# Exemple d'utilisation
graphe_matrice_oriente = GrapheMatrice(4, oriente=True)
graphe_matrice_oriente.ajouter_arete(0, 1)
graphe_matrice_oriente.ajouter_arc(1, 2)
graphe_matrice_oriente.afficher_matrice()
