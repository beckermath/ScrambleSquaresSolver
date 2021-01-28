def add_vertex(graph, v):
  if v in graph:
    print("Vertex ", v, " already exists.")
  else:
    graph[v] = []

def add_edge(graph, v1, v2, c):
  if v1 not in graph:
    print("Vertex ", v1, " does not exist.")
  elif v2 not in graph:
    print("Vertex ", v2, " does not exist.")
  else:
    temp = [v2, c]
    graph[v1].append(temp)

def print_graph(graph):
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " edge color: ", edges[1])

