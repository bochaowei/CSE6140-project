import heapq
import time
def minimum_vertex_cover_greedy(graph):
    t0=time.time()
    G=graph
    nodes=[(d,n) for n,d in G.degree]
    heapq.heapify(nodes)
    solution=[]
    while G.edges:
        max_node=heapq.heappop(nodes)[1]
        G.remove_node(max_node)
        solution.append(max_node)
    t1=time.time()

    return (solution,t1-t0)


