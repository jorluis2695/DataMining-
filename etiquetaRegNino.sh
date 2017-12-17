file="fileN01_filt.txt"
a=31021
b=31060
c=31180
d=31240
e=31260
acum=0
total=32000
bool=false
echo "region_nino" > fileF.txt 
cat $file | tail -n +2 | while read line; do
	#echo "$line"
	col2=$(echo $line | awk -F',' ' { print $3 }')
    #echo "$col2"
    for i in {1..30}
    do
    	
    	acum=$[1000 *$i]
    	total=$[31000 +acum]
    	#echo "$total"
		total=$(echo $total-$col2 | bc)
    	#echo "$total"
    	if [[ $total -ge 0 ]]; then
    		#echo "continue"

    		if [[ $i -lt  11 ]]; then
				if [[ $col2 -ge $a && $col2 -le $b ]]; then
					echo "Nino 3" >> fileF.txt 
					#echo "Nino 3"
				elif [[ $col2 -gt	 $b && $col2 -le $c ]]; then
					echo "Nino 3.4" >> fileF.txt 
					#echo "Nino 3.4"
				elif [[ $col2 -gt $c && $col2 -le $d ]]; then
					echo "Nino 4" >> fileF.txt 
					#echo "Nino 4"
				else
					echo "NONE" >> fileF.txt 
					#echo "NONE"
				fi
				break
			elif [[ $i -ge  11 && $i -le 20 ]]; then
				if [[ $col2 -ge $a && $col2 -le $b ]]; then
					echo "Nino 3" >> fileF.txt 
					#echo "Nino 3"
				elif [[ $col2 -gt $b && $col2 -le $c ]]; then
					echo "Nino 3.4" >> fileF.txt 
					#echo "Nino 3.4"
				elif [[ $col2 -gt $c && $col2 -le $d ]]; then
					echo "Nino 4" >> fileF.txt 
					#echo "Nino 4"
				elif [[ $col2 -gt $d && $col2 -le $e ]]; then
					echo "Nino 1-2" >> fileF.txt 
					#echo "Nino 1-2"
				else
					echo "NONE" >> fileF.txt 
					#echo "NONE"
				fi
				break
			else
				if [[ $col2 -gt $d && $col2 -le $e ]]; then
					echo "Nino 1-2" >> fileF.txt
					#echo "Nino 1-2" 
				else
					echo "NONE" >> fileF.txt 
					#echo "NONE"
				fi
				break

			fi

		else
			if [[ $total -lt -30000 ]]; then
				echo "NONE" >> fileF.txt 
				#echo "NONE sobrep" 
				break
			else
				a=$[$a +1000]
				b=$[$b +1000]	
				c=$[$c +1000]	
				d=$[$d +1000]
				e=$[$e +1000]
			fi
		fi
		
	done
	a=31021
	b=31060
	c=31180
	d=31240
	e=31260	
   
done
paste -d, fileprueba.txt fileF.txt > temp4.txt
mv temp4.txt fileF.txt	
