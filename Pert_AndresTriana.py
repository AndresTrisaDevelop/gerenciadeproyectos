import matplotlib.pyplot as plt
import networkx as nx

# Datos de actividades
actividades = {
    'Inicio': {'duracion': 0, 'predecesores': []},
    'A': {'duracion': 7, 'predecesores': ['Inicio']},
    'B': {'duracion': 5, 'predecesores': ['A']},
    'C': {'duracion': 8, 'predecesores': ['A']},
    'D': {'duracion': 3, 'predecesores': ['B', 'C']},
    'E': {'duracion': 12, 'predecesores': ['D']},
    'F': {'duracion': 15, 'predecesores': ['E']},
    'G': {'duracion': 12, 'predecesores': ['E']},
    'H': {'duracion': 6, 'predecesores': ['F', 'G']},
    'I': {'duracion': 10, 'predecesores': ['H']},
    'J': {'duracion': 4, 'predecesores': ['I']},
    'K': {'duracion': 7, 'predecesores': ['J']},
    'Final': {'duracion': 0, 'predecesores': ['K']}
}

# Crear grafo
G = nx.DiGraph()

# Agregar nodos con duraciones
for actividad, datos in actividades.items():
    G.add_node(actividad, duracion=datos['duracion'])

# Agregar aristas según predecesores
for actividad, datos in actividades.items():
    for predecesor in datos['predecesores']:
        G.add_edge(predecesor, actividad)

# Calcular la ruta crítica
ruta_critica = nx.algorithms.dag.dag_longest_path(G, weight='duracion')

# Usar layout con ajuste para que sea de izquierda a derecha
pos = nx.spring_layout(G)


# Dibujar el grafo
plt.figure(figsize=(14, 10))

# Dibujar todas las aristas normalmente
nx.draw(G, pos, with_labels=True, node_size=2500, node_color='lightblue', font_size=12, font_weight='bold', arrows=True)

# Resaltar la ruta crítica en rojo
ruta_edges = [(ruta_critica[i], ruta_critica[i + 1]) for i in range(len(ruta_critica) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=ruta_edges, edge_color='r', width=3)

# Añadir etiquetas de duración
duraciones = nx.get_node_attributes(G, 'duracion')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{actividades[v]['duracion']} días" for u, v in G.edges()})

# Mostrar ruta crítica en el título
plt.title(f'Diagrama PERT - Ruta Crítica: {" -> ".join(ruta_critica)}', fontsize=14)

plt.show()
