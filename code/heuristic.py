import heapq
import time
import networkx as nx
def Degree_Greedy(graph):  ###maximum degree greedy algo
    t0=time.time() ###start time
    G=graph
    solution=[]
    trace=[]
    while G.edges:
        nodes=[(-d,n) for n,d in G.degree] 
        heapq.heapify(nodes) ######heapify the nodes according to their degree
        max_node=heapq.heappop(nodes)[1] ###find the node with highest degree
        G.remove_node(max_node) ###remove it from the graph
        solution.append(max_node) ###add to solution
    
    t1=time.time()
    trace.append(str(t1-t0)+', '+str(len(solution))) ###record the running time
    
    return solution,trace

def Two_Vertex(graph): #######approximate algo with approximation ratio of 2
    t0=time.time()
    G=graph
    solution=[]
    trace=[]
    while G.edges:
        e=list(G.edges)
        u,v=random.choice(e) ###randomly select an edge and remove both the nodes
        G.remove_node(u)
        G.remove_node(v)
        solution.append(u)
        solution.append(v)
    t1=time.time()
    trace.append(str(t1-t0)+', '+str(len(solution)))
    
    return solution,trace


