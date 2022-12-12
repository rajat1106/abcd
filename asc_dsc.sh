#Assignment4 - 3rd problem

declare -a array

echo "Enter the array of 5 numbers"

for (( i= 0; i<=4; i++ ))
do
	read array_ele
	array[$i]="$array_ele"

done
echo "This is your original array: ${array[@]}"
echo "-----------------------------------------"

echo "Descending order"

for (( i=0 ; i < ${#array[@]}; i++ ))
do
    for (( j=0 ; j < ${#array[@]}; j++ ))
    do
      if [[ ${array[$j]} -lt  ${array[$i]} ]]
      then
        tmp=${numbers[$i]}
        array[$i]=${array[$j]}
        array[$j]=${tmp}
      fi
    done
done

for n in "${array[@]}"
do
    echo "$n"
done


echo "Ascending order"
