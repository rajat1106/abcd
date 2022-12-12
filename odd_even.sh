#Assignment4 - 2nd problem

declare -a array
declare -a array_p
declare -a array_n
echo "Enter the array of 5 numbers"

for (( i= 0; i<=4; i++ ))
do
	read array_ele
	array[$i]="$array_ele"

done

echo "This is your original array: ${array[@]}"
j=0
k=0
c=0
echo "--------------------------------------------"
while ((c<=4))
do
	if (( ${array[c]}%2==0 ))
	then
		echo "The $c th number i.e ${array[$c]} is Even"
		array_p[$j]="${array[c]}"
		j=$((j+1))
	else
		echo "The $c th number i.e ${array[$c]} is Odd"
		array_n[$k]="${array[c]}"
		k=$((k+1))
	fi
	((c++))
done
echo "----------------------------------------------"
echo "Even numbers: ${array_p[@]}"
echo "Odd numbers: ${array_n[@]}"
