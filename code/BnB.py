import argparse
from collections import deque, defaultdict
import os
from re import I
""" Our code """
#from LS1 import LocalSearch1
import networkx as nx
import copy
import sys
sys.setrecursionlimit(2^100000)
import time

def check(G, solution, dmax, upper):
    # check status of a partial solution
    if dmax == 0:
        if len(solution) < upper:
            return 1
        else:
            return -1
    else:
        NumEdges = len(list(G.edges))
        lower = len(solution) + NumEdges / dmax
    if lower >= upper:
        return -1       #not worth exploring
    elif NumEdges == 0:
        return 1       # all covered, complete solution
    return 0       # still valid partial solution, continue


def BestNode(G):
    # pick node with most degree
    dmax = 0
    best = None
    include = nx.get_node_attributes(G, "include")
    for node in list(G.nodes):
        if include[node] == -1:    # node already decided to exclude
            continue
        else:
            d = G.degree[node]
            if d > dmax:
                dmax = d
                best = node
    return best, dmax        # return best node and degree


def include(G, node, solution):
    # to include a node v in the solution
    solution.add(node)   # append the node to the solution set
    G.remove_node(node)   # remove node from the graph
    return G, solution

def exclude(G, node):
    # to exclude a node from the solution.
    nx.set_node_attributes(G, {node: -1}, name="include")    # -1 means exclude from current solution
    return G

def Backtrack(G, solution, best_solution, upper, parent_G, parent_solution, trace, cutoff_time, t0):
    # check current solution
    if (time.time() - t0) >= cutoff_time:
        return best_solution, upper, parent_G, parent_solution, trace
    v, dmax = BestNode(G)
    state = check(G, solution, dmax, upper)
    if state == -1:
        # not worthy exploring
        return best_solution, upper, parent_G, parent_solution, trace
    elif state == 1:
        # find a better solution
        best_solution = solution
        upper = len(best_solution)
        trace.append(str(time.time()-t0)+', '+str(len(best_solution))) ###record the running time
        return best_solution, upper, parent_G, parent_solution, trace
    elif state == 0:
        # make a copy of current state
        root_G = copy.deepcopy(G)
        root_solution = copy.deepcopy(solution)
        # if we include node v in solution
        G, solution = include(G, v, solution)
        best_solution, upper, G, solution, trace = Backtrack(G, solution, best_solution, upper, root_G, root_solution, trace, cutoff_time, t0)

        # if we do not include v in solution
        G = exclude(G, v)
        best_solution, upper, G, solution, trace = Backtrack(G, solution, best_solution, upper, root_G, root_solution, trace, cutoff_time, t0)
    return best_solution, upper, parent_G, parent_solution, trace


def BnB(graph, cutoff_time):
    t0 = time.time()
    num_edge = graph.number_of_edges()
    solution = set()
    best_solution = set()
    upper = float('inf')
    parent_G = graph
    parent_solution = set()
    best_f = graph.number_of_nodes()
    trace = [str(round(time.time() -  t0, 2)) + ' ' + str(best_f)]
    output = Backtrack(graph, solution, best_solution, upper, parent_G, parent_solution, trace, cutoff_time, t0)
    solution = output[0]
    trace = output[4]
    return solution, trace
