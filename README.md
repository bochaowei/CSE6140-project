This is for CSE6140 project: Minimum vertex cover. Each of our group members is in charge of implementing one of the four methods and write the corresponding parts in the report. 'BnB.py','heuristic.py', 'LS_HC' and 'LS-SA' are the modules for the four methods.
The 'Read_Write_Data_nx.py' imported four modules, read the graph data and after running all functions, write the results to output.

requirements:
networkx

How to compile our codes:
1. All codes are included in "code" folder
2. Using executable shell "runTest.sh" by command line ./runTest.sh
	variables in runTest.sh:
		1. time (you can edit this variable to set cutoff time)
		2. seed (random seed for local search)
runTest.sh will traversal all graph file from folder DATA and pass graph to each algorithm (BnB, Approx, LS1, LS2)
