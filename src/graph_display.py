import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def build_solution_graph(solution):
    DG = nx.MultiDiGraph()
    DG.add_nodes_from(['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd'])

    pos = {
        'a' : (5, 10),
        'b' : (10, 10),
        'c' : (15, 10),
        'd' : (20, 10),
        'A' : (5, 15),
        'B' : (10, 15),
        'C' : (15, 15),
        'D' : (20, 15),
    }

    edges = []

    #top row
    edges.append((solution[0][3], solution[0][0]))

    edges.append((solution[1][0], solution[1][1]))
    edges.append((solution[1][3], solution[1][0]))

    edges.append((solution[2][0], solution[2][1]))

    # #middle row
    edges.append((solution[3][2], solution[3][3]))
    edges.append((solution[3][3], solution[3][0]))

    edges.append((solution[4][0], solution[4][1]))
    edges.append((solution[4][1], solution[4][2]))
    edges.append((solution[4][2], solution[4][3]))
    edges.append((solution[4][3], solution[4][0]))

    edges.append((solution[5][0], solution[5][1]))
    edges.append((solution[5][1], solution[5][2]))

    # #bottom row
    edges.append((solution[6][2], solution[6][3]))

    edges.append((solution[7][1], solution[7][2]))
    edges.append((solution[7][2], solution[7][3]))

    edges.append((solution[8][1], solution[8][2]))

    DG.add_edges_from(edges)
    nx.draw_networkx_nodes(DG, pos, node_size = 200, alpha= 1)
    nx.draw_networkx_labels(DG, pos, font_size=10)

    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.2',edgelist=[edges[0]], edge_color="#DF2020", arrows=True)

    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.1',edgelist=[edges[1]], edge_color="#FF8000", arrows=True)
    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.1',edgelist=[edges[2]], edge_color="#FF8000", arrows=True)

    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.15',edgelist=[edges[3]], edge_color="#FFFF00", arrows=True)

    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.05',edgelist=[edges[4]], edge_color="#80FF00", arrows=True)
    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.05',edgelist=[edges[5]], edge_color="#80FF00", arrows=True)

    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.0',edgelist=[edges[6]], edge_color="#0066CC", arrows=True)
    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.0',edgelist=[edges[7]], edge_color="#0066CC", arrows=True)
    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.0',edgelist=[edges[8]], edge_color="#0066CC", arrows=True)
    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.0',edgelist=[edges[9]], edge_color="#0066CC", arrows=True)

    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.05',edgelist=[edges[11]], edge_color="#6600CC", arrows=True)
    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.05',edgelist=[edges[10]], edge_color="#6600CC", arrows=True)

    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.15',edgelist=[edges[12]], edge_color="#FF00FF", arrows=True)

    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.1',edgelist=[edges[13]], edge_color="#000000", arrows=True)
    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.1',edgelist=[edges[14]], edge_color="#000000", arrows=True)

    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.2',edgelist=[edges[15]], edge_color="#00FFFF", arrows=True)
    
    red_patch = mpatches.Patch(color='#DF2020', label='1')
    orange_patch = mpatches.Patch(color='#FF8000', label='2')
    yellow_patch = mpatches.Patch(color='#FFFF00', label='3')
    green_patch = mpatches.Patch(color='#80FF00', label='4')
    blue_patch = mpatches.Patch(color='#0066CC', label='5')
    purple_patch = mpatches.Patch(color='#6600CC', label='6')
    cyan_patch = mpatches.Patch(color='#00FFFF', label='7')
    black_patch = mpatches.Patch(color='#000000', label='8')
    pink_patch = mpatches.Patch(color='#FF00FF', label='9')

    plt.legend(handles=[red_patch, green_patch, cyan_patch, orange_patch, blue_patch, black_patch, yellow_patch, purple_patch, pink_patch], loc="best", ncol=3)

    plt.show()

def build_solution_graph_two_sided(solution, other_side):
    DG = nx.MultiDiGraph()
    DG.add_nodes_from(['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd'])

    pos = {
        'a' : (5, 10),
        'b' : (10, 10),
        'c' : (15, 10),
        'd' : (20, 10),
        'A' : (5, 15),
        'B' : (10, 15),
        'C' : (15, 15),
        'D' : (20, 15),
    }

    edges = []
    
    edges.append((solution[0][3], solution[0][0]))
    edges.append((solution[1][0], solution[1][1]))

    edges.append((solution[2][2], solution[2][3]))
    edges.append((solution[3][1], solution[3][2]))

    edges.append((other_side[0][3], other_side[0][0]))
    edges.append((other_side[1][0], other_side[1][1]))

    edges.append((other_side[2][2], other_side[2][3]))
    edges.append((other_side[3][1], other_side[3][2]))

    DG.add_edges_from(edges)
    nx.draw_networkx_nodes(DG, pos, node_size = 200, alpha= 1)
    nx.draw_networkx_labels(DG, pos, font_size=10)

    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.0',edgelist=[edges[0]], edge_color="#DF2020", arrows=True)
    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.0',edgelist=[edges[1]], edge_color="#FF8000", arrows=True)
    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.0',edgelist=[edges[2]], edge_color="#FFFF00", arrows=True)
    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.0',edgelist=[edges[3]], edge_color="#80FF00", arrows=True)

    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.2',edgelist=[edges[4]], edge_color="#DF2020", arrows=True)
    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.2',edgelist=[edges[5]], edge_color="#FF8000", arrows=True)
    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.2',edgelist=[edges[6]], edge_color="#FFFF00", arrows=True)
    nx.draw_networkx_edges(DG, pos, connectionstyle='arc3, rad = 0.2',edgelist=[edges[7]], edge_color="#80FF00", arrows=True)

    red_patch = mpatches.Patch(color='#DF2020', label='1')
    orange_patch = mpatches.Patch(color='#FF8000', label='2')
    yellow_patch = mpatches.Patch(color='#FFFF00', label='3')
    green_patch = mpatches.Patch(color='#80FF00', label='4')

    plt.legend(handles=[red_patch, orange_patch, yellow_patch, green_patch], loc="best", ncol=1)

    plt.show()