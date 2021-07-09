#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-09
#-------------------------------------------------------------------------------

import random
import networkx as nx
import matplotlib.pyplot as plt


def mark_node( P ) :
    nx.draw(G, pos=pos, nodelist=P, node_size=900, node_color='lightgreen'  )

def reset_node( P ) :
    nx.draw(G, pos=pos, nodelist=P, node_size=900, node_color='tomato'  )

fig = plt.figure(figsize=(10,8)) # 8인치 by 8인치

N = 14
M = 10
G=nx.grid_2d_graph(N,M)

for w in range(M) :
    G.add_edge( (0,w),(N-1,w) )

pos = dict( (n, n) for n in G.nodes() ) # pos=(위치, node 이름)
# vlabels = dict( ((i, j), i * 10 + j) for i, j in G.nodes() ) # 사용안함.
vlabels = dict( ((i, j), str(i)+","+str(j) ) for i, j in G.nodes() )

nx.draw_networkx(G, pos=pos, node_size=900,  labels=vlabels,node_color='tan', edge_color='r', font_size = 10)
nx.draw_networkx_edges (G, pos,  width=2, edge_color='tan' )

nx.draw(G, pos=pos, nodelist=[(0,0), (1,1)], \
                  node_size=900, node_color='yellow'  )

plt.title("Solid Graph Drawing")

##labels = {}
##for node in G.nodes():
##    if random.randrange(100)%3 == 0 :
##        labels[node] = node
##
###nx.draw(G, pos, with_labels=False)
###Now only add labels to the nodes you require (the hubs in my case)
##nx.draw_networkx_labels(G,pos,labels,font_size=10,font_color='w')


for w in list( G.nodes ) :
    print( f' w={w} >> {list( G.neighbors( w ))}' )

my=[ (4,3), (8,6), (5,6) ]
mark_node( my )
reset_node( [(0,0)] )


plt.axis('off')
plt.show()