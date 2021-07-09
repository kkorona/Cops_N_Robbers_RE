#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-06-09
#-------------------------------------------------------------------------------

import random
import networkx as nx
import matplotlib.pyplot as plt

ncolor="gainsboro"
ccolor="limegreen"
rcolor="tomato"
ecolor='gray'

def mark_rob( P ) :
    nx.draw(G, pos=pos, nodelist=P, node_size=900, node_color= rcolor, edge_color=ecolor )
    return

def mark_cop( P ) :
    nx.draw(G, pos=pos, nodelist=P, node_size=900, node_color= ccolor, edge_color=ecolor )
    return

def reset_rob( P ) :
    nx.draw(G, pos=pos, nodelist=P, node_size=900, node_color= ncolor, edge_color=ecolor )
    return

def reset_cop( P ) :
    nx.draw(G, pos=pos, nodelist=P, node_size=900, node_color= ncolor, edge_color=ecolor )
    return

fig = plt.figure(figsize=(9,7)) # 8인치 by 8인치

N = 12
M = 9
G=nx.grid_2d_graph(N,M)

for w in range(M) :   # circular cylind edge 추가하기
    G.add_edge( (0,w),(N-1,w) )

pos = dict( (n, n) for n in G.nodes() ) # pos=(위치, node 이름)
# vlabels = dict( ((i, j), i * 10 + j) for i, j in G.nodes() ) # 사용안함.
vlabels = dict( ((i, j), str(i)+","+str(j) ) for i, j in G.nodes() )

nx.draw_networkx(G, pos, node_size=900, node_color= ncolor ,
                 font_size=10, labels=vlabels)
nx.draw_networkx_edges(G, pos=pos,width=2, edge_color= ecolor )

plt.title(" Cops and Robbers in Cylinder Model")

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

my=[ (4,3), (8,6), (0,0) ]
mark_cop( my )
mark_rob( [ (4,2) ] )
##reset_cop( [(0,0)] )


plt.axis('off')
plt.show()