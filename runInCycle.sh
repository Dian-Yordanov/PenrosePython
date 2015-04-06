#!/bin/bash
clear
max=10
for i in `seq 2 $max`
do
python pythonPenroseServer.py 
sleep 5
done

