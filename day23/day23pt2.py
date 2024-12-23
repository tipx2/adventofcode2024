import networkx as nx
with open("day23/input23.txt") as f:
  twos = [x.strip().split("-") for x in f.readlines()]

adj = {}

for x, y in twos:
  if x not in adj.keys():
    adj[x] = set()
  if y not in adj.keys():
    adj[y] = set()
  
  adj[y].add(x)
  adj[x].add(y)

g = nx.Graph()

for k in adj.keys():
  g.add_edges_from([(k, x) for x in adj[k]])

print(",".join(sorted(list(nx.approximation.max_clique(g)))))