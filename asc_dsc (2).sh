#Assignment4 - 3rd problem

echo "Enter the size of the array"
read n

echo "Enter $n numbers in the array:"

i=0
while (($i < $n ))
do
	read a[$i]
	((i++))
done

flag=1
for (( i=0; i<$n-1; i++ ))
do
	flag=0;
	for ((j =0; j<$n-1-$i; j++ ))
	do
		if [[ ${a[$j]} -gt ${a[$j+1]} ]]
		then
			temp=${a[$j]}
			a[$j]=${a[$j+1]}
			a[$j+1]=$temp
			flag=1
		fi
	done
	if [[ $flag -eq 0 ]]
	then
		break
	fi
done
echo "---------------------------"
echo "Ascending order: ${a[@]}"
echo "-------------------------"

flag1=1
for (( i=0;i<$n-1;i++))
do
	flag1=0
	for (( j=0; j<$n-1-$i; j++ ))
	do
		if [[ ${a[$j]} -lt ${a[$j+1]} ]]
		then
			temp1=${a[$j]}
			a[$j]=${a[$j+1]}
			a[$j+1]=$temp1
			flag1=1
		fi
	done
	if [[ $flag1 -eq 0 ]]
	then
		break
	fi
done
echo "Descending order: ${a[@]}"
