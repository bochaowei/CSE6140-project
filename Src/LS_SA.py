import math
import time
import random
import networkx as nx

def SimulatedAnnealing(graph, cutoff_time, random_seed):
    random.seed(random_seed)
    vertices = graph.nodes
    cover = set()
    for i in vertices:
        cover.add(int(i))
    vertices = cover.copy()

    num_edge = graph.number_of_edges()
    best_f = graph.number_of_nodes()

    start_time = time.time()
    alpha = 0.99
    T0 = 200
    T = T0
    stop_point = 1e-14
    threshold = 1
    uncovered = set()
    trace = [str(round(time.time() - start_time, 2)) + ' ' + str(best_f)]

    f = 1.0 * len(cover) + 2.0 * len(uncovered)
    best_cover = cover.copy()
    best_f = f
    best_f2 = f
    initial_f = best_f2
    while (time.time() - start_time) < cutoff_time or T > stop_point:
        u = int(random.sample(vertices, 1)[0])
        neibneighbors = list(graph.adj[u])
        if u in cover:
            cover.remove(u)
            for i in neibneighbors:
                i = int(i)
                if i not in cover:
                    uncovered.add((u, i))
                    uncovered.add((i, u))
        else:
            cover.add(u)
            for i in neibneighbors:
                i = int(i)
                if i not in cover:
                    uncovered.remove((u, i))
                    uncovered.remove((i, u))


        deg_u = len(neibneighbors)/num_edge
        f1 = 1.0*len(cover)+2.0*len(uncovered)
        dE = max(0, f1 - f)
        if u in cover:
            P = math.exp(-(dE * (1 - deg_u)) / T)
        else:
            P = math.exp(-(dE * (1 + deg_u)) / T)

        T = T * alpha
        rand = random.uniform(0, 1)
        if rand < P:
            f = f1
        else:
            if u in cover:
                cover.remove(u)
                for i in neibneighbors:
                    i = int(i)
                    if i not in cover:
                        uncovered.add((u, i))
                        uncovered.add((i, u))
            else:
                cover.add(u)
                for i in neibneighbors:
                    i = int(i)
                    if i not in cover:
                        uncovered.remove((u, i))
                        uncovered.remove((i, u))

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