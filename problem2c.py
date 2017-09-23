#Jack Slezak and Alex Bullock
import networkx as nx
import problem2b
import matplotlib.pyplot as plt

#declares list that tracks all pairs and their distances
distances = []
F = nx.Graph()
F.add_edges_from([('Lincoln','MIT'),('Lincoln','Case'),('MIT', 'BBN'),('MIT','Utah'),('BBN','Harvard'),
('BBN','Rand'),('Harvard','Carnegie'),('Case','Carnegie'),('Utah','SDC'),('SDC','Rand'),('Stanford','UCLA'),
('Stanford','SRI'),('UCLA','Rand'),('UCLA','SRI'),('UCLA','UCSB'),('SRI','UCSB'),('SRI','Utah')])

#performs BFS for each node, recording all node pairs with their distance
for i in F.nodes():
	x =  problem2b.bfs(i)
	for pair in x:
		distances.append([i, pair[0], pair[1]])

#removes node self-pairings
for row in distances:
	if row[0] == row[1]:
		distances.remove(row)

#removes repeats of node pairs
for r1 in distances:
	for r2 in distances:
		if r1[0] == r2[1]:
			if r1[1] == r2[0]:
				distances.remove(r2)

print distances

#creates histogram of distances between nodes
plotarray = []
for j in distances:
	plotarray.append(j[2])

plt.hist([plotarray], bins=max(plotarray))
plt.show()	