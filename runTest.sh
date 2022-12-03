#!/bin/bash
graphFiles=`ls ./data/ | grep .graph`
time=20
seed=5
for graph in ${graphFiles}
do
	filename=`echo ${graph} | cut -d'.' -f1`
	echo ${graph}
	python ./code/Read_Write_Data_nx.py -inst ./DATA/${graph} -alg LS1 -time ${time} -seed ${seed}
	python ./code/Read_Write_Data_nx.py -inst ./DATA/${graph} -alg LS2 -time ${time} -seed ${seed}
	python ./code/Read_Write_Data_nx.py -inst ./DATA/${graph} -alg BnB -time ${time} -seed ${seed}
	python ./code/Read_Write_Data_nx.py -inst ./DATA/${graph} -alg Approx -time ${time} -seed ${seed}
done
