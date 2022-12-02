#!/bin/bash
cut_off_time=20
random_seed=5
python Read_Write_Data_nx.py -inst D:/Desktop/CSE6140Project/DATA/dummy1.graph -alg LS1 -time ${cut_off_time} -seed 5
python Read_Write_Data_nx.py -inst D:/Desktop/CSE6140Project/DATA/dummy2.graph -alg LS1 -time ${cut_off_time} -seed 5
python Read_Write_Data_nx.py -inst D:/Desktop/CSE6140Project/DATA/jazz.graph -alg LS1 -time ${cut_off_time} -seed 5
python Read_Write_Data_nx.py -inst D:/Desktop/CSE6140Project/DATA/email.graph -alg LS1 -time ${cut_off_time} -seed 5
python Read_Write_Data_nx.py -inst D:/Desktop/CSE6140Project/DATA/netscience.graph -alg LS1 -time ${cut_off_time} -seed 5
python Read_Write_Data_nx.py -inst D:/Desktop/CSE6140Project/DATA/star.graph -alg LS1 -time ${cut_off_time} -seed 5
python Read_Write_Data_nx.py -inst D:/Desktop/CSE6140Project/DATA/star2.graph -alg LS1 -time ${cut_off_time} -seed 5
python Read_Write_Data_nx.py -inst D:/Desktop/CSE6140Project/DATA/power.graph -alg LS1 -time ${cut_off_time} -seed 5
python Read_Write_Data_nx.py -inst D:/Desktop/CSE6140Project/DATA/karate.graph -alg LS1 -time ${cut_off_time} -seed 5
python Read_Write_Data_nx.py -inst D:/Desktop/CSE6140Project/DATA/football.graph -alg LS1 -time ${cut_off_time} -seed 5
python Read_Write_Data_nx.py -inst D:/Desktop/CSE6140Project/DATA/hep-th.graph -alg LS1 -time ${cut_off_time} -seed 5
python Read_Write_Data_nx.py -inst D:/Desktop/CSE6140Project/DATA/as-22july06.graph -alg LS1 -time ${cut_off_time} -seed 5
python Read_Write_Data_nx.py -inst D:/Desktop/CSE6140Project/DATA/delaunay_n10.graph -alg LS1 -time ${cut_off_time} -seed 5
