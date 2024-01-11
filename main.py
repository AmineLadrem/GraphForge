import sys
import time
sys.path.insert(0, './lib')

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from graph import *

choice=None

def create_menu(options):
    console = Console()

    markdown_text = "# Bienvenue à GraphForge - Centre de Commande\n"
    for i, option in enumerate(options, 1):
        markdown_text += f"{i}. {option}\n"

    markdown = Markdown(markdown_text)
    panel = Panel(markdown, border_style="blue", expand=False)

    console.print(panel)

    choice = int(input("Veuillez entrer le numero de votre choix: ")) - 1
    if 0 <= choice < len(options):
        console.clear()
        message = Markdown(f"## Vous avez choisi l'option : {options[choice]}")
        message_panel = Panel(message, border_style="green", expand=False)
        console.print(message_panel)
        return choice
    else:
        print("Invalid choice. Please enter a number between 1 and", len(options))
        return None
 
options = [ "Construction d’un graphe orienté/non orienté", 
           "Affichage du graphe (représentation mémoire matrice d’adjacence/ liste d’adjacence).",
           "Affichage du graphe (représentation graphique).",
           "Calculer la densité du graphe",
           "Calculer le degré du graphe",
           "Vérifier si le graphe est eulérien",
           "Vérifier si le graphe est complet",
           "Vérifier si le graphe est un arbre",
           "Recherche d’un nœud a dans le graphe (afficher le nœud et ses liens)",
           "Recherche de tous les chemins entre un nœud a et un nœud b",
           "Recherche du chemin le plus court entre deux nœuds a et b",
           "Recherche d’une composante (fortement) connexe à partir d’un nœud a.",
           "Trouver tous les cycles/circuits dans le graphe",
           "Ajouter/ Supprimer un nœud a avec ses liens",
           "Ajouter un lien (arc ou arête) entre deux nœuds existants"
]   



def main():
    while True:
        choice = None
        while choice is None:
            choice = create_menu(options)

        if choice == 0:
            graphe=create_graph()
        if choice == 1:
            graphe.afficher()
            time.sleep(5)

        if choice == 2:
            graphe.afficher_graphe()

        if choice == 3:
            graphe.calculer_densite()
            time.sleep(5)    

if __name__ == "__main__":
    main()
    
