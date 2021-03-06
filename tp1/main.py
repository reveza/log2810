from graph import Graph

g = Graph("centresLocaux.txt")

# g.printGraph()
# start = 1
# destination = 23
#g.dijkstraNi(22, 20, 'eleve')
#g.extraireSousGraph(22,'NI-NH', 'eleve')

menu = '(a) Mettre a jour la carte.\n(b) Determiner le plus court chemin securitaire.\n'
menu += '(c) Extraire un sous-graphe.\n(d) Quitter.\n'
while True:
    entree = input(menu)
    graph = Graph('centresLocaux.txt')
    if entree == 'a':
        fichier = input('Entrer le nom du fichier: ')
        graph = Graph(fichier)
        graph.printGraph()
    elif entree == 'b':
        depart = input('Entrer le point de depart: ')
        desti = input('Entrer le point de destination: ')
        risk = input('Entrer la categorie de risque du patient (faible, moyen ou eleve):')
        graph.dijkstraNi(int(depart), int(desti), risk)
    elif entree == 'c':
        sommet = input('Entrer le sommet de depart ')
        car = input('Entrer le type de vehicule: \nNI-NH ou LI-ion \n')
        graph.extraireSousGraph(int(sommet), car, 'eleve')
    elif entree == 'd':
        print('fin du programme')
        break
    else:
        print('Entree invalide \n')
