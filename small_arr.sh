#Assignt4 - 4th problem

echo "Enter size of array"
a=()
read size

echo "Enter $size numbers in the array"
for (( i=0; i<size; i++ ))
do
	read num
	a+=($num)
done

min=${a[0]}
max=${a[0]}

for i in ${a[@]}
do
	if (( $i < min ))
	then
		min=$i
	fi
done

for j in ${a[@]}
do
	if(($j > max))
	then
		max=$j
	fi
done

echo "Smallest number is: $min"
echo "Largest number is: $max"
