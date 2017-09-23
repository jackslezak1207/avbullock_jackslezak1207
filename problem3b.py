#Jack Slezak and Alex Bullock problem3b.py

import csv
import os
import networkx as nx
import operator

#Kevin Bacon's Number: 3257

#create the graph
G = nx.Graph()

#reads the csv file
with open('imdb_edges.tsv','rU') as tsvin:
    tsvreader = csv.reader(tsvin, delimiter='\t')

    kevandneighbors = ['3257']

    for row in tsvreader:
        #this if statement is used to first identify root node (Kevin Bacon)
        #and then find all of his first neighbors to create edge
        if row[0] == '3257':
            kevandneighbors.append(row[1])
            G.add_edge(row[0],row[1])

    #read the csv file again looking for second neighbors this time
    with open('imdb_edges.tsv','rU') as tsvin1:
        tsvreader1 = csv.reader(tsvin1, delimiter='\t')
        for r in tsvreader1:
            for x in kevandneighbors:
                #if actor is neighbor to Kevin's neihbor, create edge
                if r[0] == x:
                    edge = (r[0], r[1])
                    G.add_edge(r[0], r[1])

    #create a list of nodes from the edges we just created
    list_of_nodes = G.nodes()
    num_of_nodes = G.number_of_nodes()
    #empty dictionary for betweenness centrality
    bc = {}
    #run through all the nodes and map shortest path
    for i in range(num_of_nodes-1):
        for j in range(i+1, num_of_nodes):
            paths = nx.all_shortest_paths(G, source=list_of_nodes[i], target = list_of_nodes[j])
            count = 0.0
            #a second dictionary to keep track of path distances
            path_diz = {}
            for p in paths:
                count += 1.0
                for n in p[1:-1]:
                    if not path_diz.has_key(n):
                        path_diz[n] = 0.0
                    path_diz[n]+=1.0
            for n in path_diz.keys():
                path_diz[n] = path_diz[n]/count
                if not bc.has_key(n):
                    bc[n] = 0.0
                bc[n]+= path_diz[n]

    #generates dictionary of entries with top 20 values
    top20 = dict(sorted(bc.items(), key = lambda kv: kv[1], reverse = True))

    #top20 isn't sorted by values, so this list must be created to sort the dictionary
    top20_sorted = sorted(top20.items(), key = lambda kv: kv[1], reverse = True)

    #dictionary to link actor IDs to names
    names = {}
    with open('imdb_actors.tsv','rU') as tsvin2:
        tsvreader2 = csv.reader(tsvin2, delimiter='\t')

        #assign key,value pairs for actor IDs and names
        for row in tsvreader2:
            if row[0] != 'ID':
                k = int(row[0])
                names[k] = row[1]

    #iterate though all keys in the list of top 20 actors to access the names from the "names" dictionary
    for y in range(0,20):
        key1 = int(top20_sorted[y][0])
        print [names[key1] , top20_sorted[y][1]]