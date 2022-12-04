import math
import time
import random
import networkx as nx
from random import choice
import heapq

def HillClimbing(graph, cutoff_time, random_seed):
    random.seed(random_seed)
    vertices = graph.nodes
    
    list_reduce = list(vertices)
    #print(list_reduce)
    
    #record current best sol, number of v in mvc, initially number of all vertex
    solution_best_list = vertices
    solution_best_length = len(vertices)
    

    t0 = time.time()

    trace=[]
    while (time.time() - t0) < cutoff_time and len(list_reduce) > 0:
        G = graph.copy()
        #random initial point
        node = choice(list_reduce)
        #print(node)
        list_reduce.remove(node)
        #print(list_reduce)
        #print(G.nodes)
        #print(graph.nodes)
        G.remove_node(node)
        solution=[]
        solution.append(node)
        while G.edges:
            nodes=[(-d,n) for n,d in G.degree] 
            heapq.heapify(nodes) ######heapify the nodes according to their degree
            max_node=heapq.heappop(nodes)[1] ###find the node with highest degree
            #print(max_node)
            G.remove_node(max_node) ###remove it from the graph
            solution.append(max_node) ###add to solution
        
        if len(solution) < solution_best_length:
            t1=time.time()
            solution_best_length = len(solution)
            solution_best_list = solution
            trace.append(str(t1-t0)+', '+str(solution_best_length))
            #print(t1)
            #print(solution_best_length)
            #print(trace)
    
    #trace.append(str(t1-t0)+', '+str(len(solution_best_list)))
    return solution_best_list,trace
    

