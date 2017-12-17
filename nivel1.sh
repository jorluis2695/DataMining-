#!/bin/bash
var1=0
var2=10
for i in {8..15}
	do
		echo "Welcome $i times"
			
		if [ $i -lt $var2 ]
		then
			var1="0""$i"
		else
			var1="$i"
		
	fi
		echo "soda_sa_n$var1""_t1.txt"
		paste soda_sa_n$var1""_t1.txt soda_tp_n$var1""_t1.txt soda_u_n$var1""_t1.txt soda_v_n$var1""_t1.txt soda_w_n$var1""_t1.txt | cut -f 1-5,10,15,20,25 | sed -e 's/\s/,/g' | tr -s ',' >> fileN$var1"".txt
		paste soda_sa_n$var1""_t2.txt soda_tp_n$var1""_t2.txt soda_u_n$var1""_t2.txt soda_v_n$var1""_t2.txt soda_w_n$var1""_t2.txt | cut -f 1-5,10,15,20,25 | sed -e 's/\s/,/g' | tr -s ',' >> fileN$var1"".txt
		paste soda_sa_n$var1""_t3.txt soda_tp_n$var1""_t3.txt soda_u_n$var1""_t3.txt soda_v_n$var1""_t3.txt soda_w_n$var1""_t3.txt | cut -f 1-5,10,15,20,25 | sed -e 's/\s/,/g' | tr -s ',' >> fileN$var1"".txt

	done