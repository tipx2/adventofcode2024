with open("day08/input8.txt") as f:
  lines = [x.strip() for x in f.readlines()]

nodes = {}
for i, line in enumerate(lines):
  for j, letter in enumerate(line):
    if letter != ".":
      if letter not in nodes.keys():
        nodes[letter] = []
      nodes[letter].append((i, j))


boundi = len(lines)
boundj = len(lines[0])


def diagonal(start, di, dj):
  poses = set()
  new_node = start
  while 0 <= new_node[0] < boundi and 0 <= new_node[1] < boundj:
    poses.add(new_node)
    new_node = (new_node[0] + di, new_node[1] + dj)
  
  return poses

antinodes = set()
for key in nodes.keys():

  for node1 in nodes[key]:
    for node2 in nodes[key]:
      if node1 == node2:
        continue
      
      di = node1[0] - node2[0]
      dj = node1[1] - node2[1]
      
      start = (node1[0], node1[1])
      
      antinodes.update(diagonal(start, di, dj))
      antinodes.update(diagonal(start, di * -1, dj * -1))


print(len(antinodes))