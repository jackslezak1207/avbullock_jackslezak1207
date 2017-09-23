#Jack Slezak and Alex Bullock
import networkx as nx
import numpy as np

def bfs(root):
	#create graph with corresponding edges from Arpanet
	G = nx.Graph()
	G.add_edges_from([('Lincoln','MIT'),('Lincoln','Case'),('MIT', 'BBN'),('MIT','Utah'),('BBN','Harvard'),
	('BBN','Rand'),('Harvard','Carnegie'),('Case','Carnegie'),('Utah','SDC'),('SDC','Rand'),('Stanford','UCLA'),
	('Stanford','SRI'),('UCLA','Rand'),('UCLA','SRI'),('UCLA','UCSB'),('SRI','UCSB'),('SRI','Utah')])
	
	#establish Case as root node, explore all of Case's neighbors, assigns them distances.
	#repeats process for Case's neighbors, their neighbors etc until all nodes are visited
	#root_node = root
	queue = []
	queue.append(root)
	G.node[root]["distance"] = 0
	while len(queue):
		working_node = queue.pop(0)
		for n in G.neighbors(working_node):
			if len(G.node[n])==0:
				G.node[n]["distance"]=G.node[working_node]["distance"]+1
				queue.append(n)
	
	#print all nodes names with corresponding distance from Case
	arpnodes = []
	for n in G.nodes():	
		arpnodes.append([n,G.node[n]["distance"]])
	return arpnodes
