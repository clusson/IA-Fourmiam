import math as m
import networkx as network
import matplotlib.pyplot as pyp
import random as r
import pants as p
import csv

# On déclare nos constantes

CONST_COMMUNE       = 'COMMUNE'
CONST_LIBELLE       = 'LIBELLE'
CONST_ABOUTISSANT   = 'ABOUTISSANT'
CONST_TENANT        = 'TENANT'
CONST_BI_MIN        = 'BI_MIN'
CONST_BI_MAX        = 'BI_MAX'
CONST_BP_MIN        = 'BP_MIN'
CONST_BP_MAX        = 'BP_MAX'
CONST_STATUT        = 'STATUT'

def nodes(node_x, node_y):
    dist = m.sqrt(pow(node_x[1] - node_y[1], 2) + pow(node_x[1] + node_y[1], 2))
    return dist

# Création du chemin noeud par noeud
def find_path(graph, start, end, path=[]):
    road = path + [start]
    if start == end:
        return road
    if not graph.has_key(road):
        return None
    for node in graph[road]:
        # Récursivité
        if node not in road:
            newroad = find_path(graph, node, end, road)
            if newroad : return newroad
    return None

# Créatioon de notre graphe


G = network.Graph()
network.draw(G)
pyp.draw()


# Lecture du CSV
with open('VOIES_NM.csv', encoding='utf-8') as csvFile:
    reader = csv.DictReader(csvFile)
    i = 0
    for row in reader:
        i += 1
        if i < 150:
            ADRESS = row[CONST_COMMUNE] + '' + row[CONST_LIBELLE]
            TENANT = row[CONST_TENANT]
            ABOUTISSANT = row[CONST_ABOUTISSANT]
            STATUT = row[CONST_STATUT]
            if TENANT != "" and ABOUTISSANT != "":
                    if (row[CONST_BI_MIN] == ""):
                        row[CONST_BI_MIN] = 1
                    else:
                        row[CONST_BI_MIN] = int(row[CONST_BI_MIN])
                    if (row[CONST_BP_MIN] == ""):
                        row[CONST_BP_MIN] = 1
                    else:
                        row[CONST_BP_MIN] = int(row[CONST_BP_MIN])
                    if (row[CONST_BI_MAX] == ""):
                        row[CONST_BI_MAX] = 1
                    else:
                        row[CONST_BI_MAX] = int(row[CONST_BI_MAX])
                    if (row[CONST_BP_MAX] == ""):
                        row[CONST_BP_MAX] = 1
                    else:
                        row[CONST_BP_MAX] = int(row[CONST_BP_MAX])

                    # Définition du poids de notre arrête
                    WEIGHT = max((row[CONST_BI_MAX] - row[CONST_BI_MIN]) / 2,
                                (row[CONST_BP_MAX] - row[CONST_BP_MIN]) / 2)
                    # Ajout des arrêtes au graphe
                    G.add_edge(row[CONST_TENANT], row[CONST_ABOUTISSANT], weight=WEIGHT,
                                   label=row[CONST_LIBELLE])

                    pos = network.spring_layout(G)

                    # Poids et nom des arrêtes
                    tab_weight = network.get_edge_attributes(G, 'weight')
                    tab_name = network.get_edge_attributes(G, 'label')

                    for x in tab_name:
                        print(tab_name[x], tab_weight[x])  # On affiche le nom et le poids de chaque rue

# Depuis notre schéma, on récupère les arrêtes, nom et points
network.draw_networkx_edges(G,pos)
network.draw_networkx_labels(G,pos)
network.draw_networkx_edge_labels(G, pos)
network.draw_networkx_nodes(G, pos)
pyp.show()

nodes = []
choice = r.randint(1, 10)

for i in range(choice):
    x = r.uniform(0, 10)
    y = r.uniform(0, 10)
    nodes.append([x, y])

ensemble = p.World(nodes, function)
solver = p.Solver()
solutions = solver.solutions(ensemble)

for solution in solutions:
    print(solution.distance)

print(nodes)
