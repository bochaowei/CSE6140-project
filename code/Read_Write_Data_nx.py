import argparse
import os
""" Our code """
from LS_SA import SimulatedAnnealing
import networkx as nx
from heuristic import Degree_Greedy
from BnB import BnB

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
    return graph


def WriteFile(dictName, filename, num_of_best_solution, trace):
    sol_filename = dictName + filename + '.sol'
    trace_filename = dictName + filename + '.trace'
    with open(sol_filename, 'w') as file:
        file.write(str(len(num_of_best_solution)) + '\n')
        #file.write(str(num_of_best_solution)[1:-1])
        for v in num_of_best_solution:
            file.write(str(v))
            file.write(',')
        file.seek(0, 2)  # end of file
        size = file.tell()  # the size...
        file.truncate(size - 1)  # truncate at that size - how ever many characters
    file.close()
    with open(trace_filename, 'w') as file:
        for i in trace:
            file.write(i + '\n')
    file.close()
    print("DONE")


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
    graph = ReadFile(args)

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
    dictName = os.getcwd()
    if dictName.split('/')[-1] == 'code':
        dictName = '../output/'
    else:
        dictName = dictName + '/output/'
    dictName = dictName.replace('\\', '/')
    """ For my own test"""
    #dictName = 'D:/Desktop/CSE6140Project/solution/'

    """
    choose algorithm based on -alg
    """
    if args.algorithm == "BnB":
        num_best_solution, trace = BnB(graph, args.time)
        WriteFile(dictName, filename, num_best_solution, trace)
    elif args.algorithm == "Approx":
        num_best_solution, trace =Degree_Greedy(graph)
        WriteFile(dictName, filename, num_best_solution, trace)
    elif args.algorithm == "LS1":
        filename += '_' + str(args.seed)
        num_best_solution, trace = SimulatedAnnealing(graph, args.time, args.seed)
        WriteFile(dictName, filename, num_best_solution, trace)
    elif args.algorithm == "LS2":
        filename += '_' + str(args.seed)
        pass
    else:
        raise NameError("Please input correct algorithm name!")
