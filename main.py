import sys
import time
sys.path.insert(0, './lib')

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
import graph

choice=None

def create_graph():
    type_graphe = int(input("Type de graphe (0 pour non orienté, 1 pour orienté) : "))
    nombre_noeuds = int(input("Nombre de nœuds dans le graphe : "))

    graphe_matrice = graph.GrapheMatrice(nombre_noeuds, oriente=(type_graphe == 1))

    if type_graphe == 0:
        aretes = input("Liste des arêtes (chaque arête doit être un couple de nœuds sans espace, et chaque arête séparée par une virgule) : ").split(',')
        for arete in aretes:
            u, v = map(int, [arete[0], arete[1]])  
            graphe_matrice.ajouter_arete(u, v)
    else:
        arcs = input("Liste des arcs (chaque arc doit être un couple de nœuds sans espace, et chaque arc séparé par une virgule) : ").split(',')
        for arc in arcs:
            u, v = map(int, [arc[0], arc[1]])  # Split the arc string into two separate values
            graphe_matrice.ajouter_arc(u, v)

    graphe_matrice.afficher_matrice()
    graphe_matrice.afficher_graphe()

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
            create_graph()
        # Add elif statements here for other choices

        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
    
