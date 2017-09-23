#Jack Slezak and Alex Bullock

import csv
import os
import networkx as nx
import operator


with open('imdb_edges.tsv','rU') as tsvin:
    tsvreader = csv.reader(tsvin, delimiter='\t')

    actors = {}
    tsvreader1 = csv.reader(tsvin, delimiter='\t')

    #creates key,value pair for each actorID and 1 or increments value if key already exists;
    #the value associated with the key represents the number of edges the node in the graph has
    for row in tsvreader1:
        if row[0] in actors:
        	actors[row[0]] += 1
        else:
        	actors[row[0]] = 1
     
    #generates dictionary of entries with top 20 values    
    top20 = dict(sorted(actors.items(), key = lambda kv: kv[1], reverse = True)[:20])

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
    for i in range(0,20):
    	key1 = int(top20_sorted[i][0])
    	print [names[key1] , top20_sorted[i][1]]
