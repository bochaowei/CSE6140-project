import math
import time
import random
import networkx as nx

def SimulatedAnnealing(graph, cutoff_time, random_seed):
    random.seed(random_seed)
    vertices = graph.nodes
    # create a set to record all covered vertex
    cover = set()
    for i in vertices:
        cover.add(int(i))
    vertices = cover.copy()

    num_edge = graph.number_of_edges()
    best_f = graph.number_of_nodes()

    start_time = time.time()
    # temperature per loop decrease rate
    alpha = 0.99
    # initial temperature
    T0 = 200
    T = T0
    # the lowest temperature
    stop_point = 1e-14
    # a constant number, set 1 here
    threshold = 1
    # a set to record all unconnected vertexes
    uncovered = set()
    trace = [str(round(time.time() - start_time, 2)) + ' ' + str(best_f)]

    # objective function
    f = 1.0 * len(cover) + 2.0 * len(uncovered)
    best_cover = cover.copy()
    best_f = f
    best_f2 = f
    initial_f = best_f2
    # the loop will end when reached cutoff time or temperature is lowest
    while (time.time() - start_time) < cutoff_time or T > stop_point:
        # pick a random vertices
        u = int(random.sample(vertices, 1)[0])
        # find the neighbor of this vertex
        neighbors = list(graph.adj[u])
        # when vertex already be covered, remove it from cover set and check its neighbor
        cover, uncovered = processSet(cover, uncovered, neighbors, u)

        # use mathematical function to calculate probability
        deg_u = len(neighbors) / num_edge
        f1 = 1.0*len(cover)+2.0*len(uncovered)
        dE = max(0, f1 - f)
        if u in cover:
            P = math.exp(-(dE * (1 - deg_u)) / T)
        else:
            P = math.exp(-(dE * (1 + deg_u)) / T)

        # temperature decreased
        T = T * alpha
        rand = random.uniform(0, 1)
        # decide whether accept new result based on probability
        if rand < P:
            f = f1
        else:
            cover, uncovered = processSet(cover, uncovered, neighbors, u)

        if f < best_f2 and len(uncovered) == 0:
            best_f2 = f
            best_cover2 = cover.copy()
            if best_f2 < best_f:
                best_f = best_f2
                trace.append(str(round(time.time() - start_time, 2)) + ' ' + str(best_f))
                best_cover = best_cover2.copy()
            if threshold < (initial_f-best_f2):
                initial_f = best_f2
                T = T0

    return best_cover, trace

def processSet(cover, uncovered, neighbors, u):
    if u in cover:
        cover.remove(u)
        for i in neighbors:
            i = int(i)
            if i not in cover:
                uncovered.add((u, i))
                uncovered.add((i, u))
    else:
        cover.add(u)
        for i in neighbors:
            i = int(i)
            if i not in cover:
                uncovered.remove((u, i))
                uncovered.remove((i, u))

    return cover, uncovered
