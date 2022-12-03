import argparse
from collections import deque, defaultdict
import os
from re import I
""" Our code """
#from LS1 import LocalSearch1
import networkx as nx
import numpy as np
import copy

def ReadFile(args):
    with open(args.filename, 'r') as file:
        first_line = file.readline()
        num_node = int(first_line.split(" ")[0])
        graph = nx.Graph()
        for node in range(num_node):
            graph.add_node(node+1)
        node1 = 1
        for line in file:
            l = line.split(" ")
            for i in l:
                if i != '\n':
                    if '\n' in i:
                        i = i.replace('\n', '')
                    graph.add_edge(node1, int(i))
            node1 += 1
        nx.set_node_attributes(graph, 0, "include")
    print(graph.nodes, graph.edges)
    print(graph)
    return graph


def WriteFile(dictName, filename, num_of_best_solution, trace):
    sol_filename = dictName + filename + '.sol'
    trace_filename = dictName + filename + '.trace'
    # print(sol_filename)
    with open(sol_filename, 'w') as file:
        file.write(str(len(num_of_best_solution)) + '\n')
        file.write(str(num_of_best_solution)[1:-1])
    file.close()
    with open(trace_filename, 'w') as file:
        for i in trace:
            file.write(i + '\n')
    file.close()


# for BnB
def check(G, solution, dmax, upper):
    # check status of a partial solution
    NumEdges = len(list(G.edges))
    lower = len(solution) + NumEdges / dmax
    if lower >= upper:
        return -1      #not worth exploring
    elif NumEdges == 0:
        return 1        # all covered, complete solution
    return 0        # still valid partial solution, continue


def BestNode(G):
    # pick node with most degree
    dmax = 0.00001
    best = None
    for node in list(G.nodes):
        if G.nodes[node]["include"] == -1:    # node already decided to exclude
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
    print(f"include node {node}")
    return G, solution

def exclude(G, node):
    # to exclude a node from the solution.
    nx.set_node_attributes(G, {node: -1}, name="include")    # -1 means exclude from current solution
    print(f"exclude node {node}")
    return G

def Backtrack(G, solution, best_solution, upper, parent_G, parent_solution):
    # check current solution
    v, dmax = BestNode(G)
    state = check(G, solution, dmax, upper)
    if state == -1:
        # not worthy
        return best_solution, upper, parent_G, parent_solution
    elif state == 1:
        # find a better solution
        best_solution = solution
        upper = len(best_solution)
        print(f"find a better solution: {best_solution}, with {upper} edges")
        breakpoint()
        return best_solution, upper, parent_G, parent_solution
    elif state == 0:
        # make a copy of current state
        root_G = copy.deepcopy(G)
        root_solution = copy.deepcopy(solution)
        # if we include node v in solution
        G, solution = include(G, v, solution)
        best_solution, upper, G, solution = Backtrack(G, solution, best_solution, upper, root_G, root_solution)            # trace back

        # if we do not include v in solution
        #breakpoint()
        G = exclude(G, v)
        best_solution, upper, G, solution = Backtrack(G, solution, best_solution, upper, root_G, root_solution)
    return best_solution, upper, parent_G, parent_solution



if __name__ == "__main__":
    """
    command line format: python <filename>.py -inst <filename> -alg [BnB|Approx|LS1|LS2] -time <cutoff in seconds> -seed <random seed>
    For my own test:
        python Read_Write_Data.py -inst D:/Desktop/CSE6140Project/DATA/dummy1.graph -alg LS1 -time 600 -seed 5
    """
    parser = argparse.ArgumentParser(description='Local Search for MVC')
    parser.add_argument('-inst', type=str, help='Test file name', dest='filename')
    parser.add_argument('-alg', type=str, action='store', help='Algorithm name', dest='algorithm')
    parser.add_argument('-time', type=int, action='store', help='Cutoff time in second', dest='time')
    parser.add_argument('-seed', type=int, action='store', help='Random seed', dest='seed')
    args = parser.parse_args()

    """
    extract data from provided file
    """
    G = ReadFile(args)

    """
    output filename
    File name: < instance > < method > < cutoff > < randSeed > ∗.sol, e.g. jazz BnB 600.sol
    File name: < instance > < method > < cutoff > < randSeed > ∗.trace, e.g. jazz BnB 600.trace, jazz LS1 600 4.trace.
    """
    filename = args.filename.split('/')[-1]
    filename = filename.split('.')[0]
    filename = filename + '_' + args.algorithm + '_' + str(args.time)   # Only local search need random seed
                                                                        # + '_' + str(args.seed)
    #### Not work on windows
    # dicts = os.getcwd()
    # if dicts.split('/')[-1] == 'src':
    #     dictName = '../solution/'
    # else:
    #     dictName = dictName + '/solution/'
    """ For my own test"""
    dictName = '/Users/zfan43/Documents/6140/CSE6140-project/Src/'

    """
    choose algorithm based on -alg
    """
    if args.algorithm == "BnB":
        pass
    else:
        raise NameError("Please input correct algorithm name!")

    Backtrack(G, set(), set(), float('inf'), G, set())
