#Jack Slezak and Alex Bullock problem3c.py

import csv
import os
import networkx as nx
import operator

#Kevin Bacon's Number: 3257

#Create the graph
G = nx.Graph()

#Read the csv file
with open('imdb_edges.tsv','rU') as tsvin:#, open('new.csv', 'wb') as csvout:
    tsvreader = csv.reader(tsvin, delimiter='\t')

    kevandneighbors = ['3257']

    #this if statement is used to first identify root node (Kevin Bacon)
    #and then find all of his first neighbors to create edge
    for row in tsvreader:
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

#distance function
    def node_distance(G, root_node):
        #an empty array
        queue=[]
        #an array that will hold the list of distances calculated
        list_distances=[]
        queue.append(root_node)
        #deleting the old keys
        if G.node[root_node].has_key('distance'):
            for n in G.nodes():
                del G.node[n]['distance']
        G.node[root_node]['distance']=0
        while len(queue):
            working_node=queue.pop(0)
            for n in G.neighbors(working_node):
                if len(G.node[n])==0:
                    G.node[n]["distance"]=G.node[working_node]["distance"]+1
                    queue.append(n)
        #append distances from root node to all other nodes and store in a list
        for n in G.nodes():
            list_distances.append(((root_node, n), G.node[n]["distance"]))
        return list_distances

    #closeness centrality calculation
    norm=0.0
    #dictionary that will hold the values of the distances
    diz_c={}
    l_values=[]
    for n in G.nodes():
        #calculates the distance from one node to all the other nodes
        #and then averages to calculate closeness centrality
        l=node_distance(G,n)
        ave_length=0
        for path in l:
            ave_length+=float(path[1])/(G.number_of_nodes()-1-0)
        norm+=1/ave_length
        diz_c[n]=1/ave_length
        l_values.append(diz_c[n])

    #generates dictionary of entries with top 20 values
    top20 = dict(sorted(diz_c.items(), key = lambda kv: kv[1], reverse = True))

    #top20 isn't sorted by values, so this list must be created to sort the dictionary
    top20_sorted = sorted(top20.items(), key = lambda kv: kv[1], reverse = True)
    #print top20_sorted
    #print len(top20_sorted)
    #print len(bc)

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