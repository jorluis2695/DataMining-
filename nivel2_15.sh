#!/bin/bash
a=5
indice=0
var2=10
bool=true
echo "" > fileF.txt 
for i in {1..5}
	do
		for j in {2..15}
		do
			if [ $j -lt $var2 ]
			then
				indice="0""$j"
			else
				indice="$j"
			fi

			
			if [ "$bool" = true ]
			then
				cat fileN$indice"".txt | cut -d"," -f $a > fileVar$a"".txt
				bool=`echo false`
			else	
				cat fileN$indice"".txt | cut -d"," -f $a  > temp.txt
				paste -d"," fileVar$a"".txt temp.txt > temp2.txt 
				mv temp2.txt fileVar$a"".txt
				
			fi


		done
		echo "fileVar$a"".txt"
		paste -d"," fileF.txt fileVar$a"".txt > temp3.txt
		mv temp3.txt fileF.txt
		bool=`echo true`
		a=$[$a +1]	


	done
	cut -d"," -f 1-3 fileN02.txt  > newFile.txt
	paste newFile.txt fileF.txt | sed -e 's/\s/,/g' | tr -s ',' > temp4.txt
	mv temp4.txt newFile.txt	

		