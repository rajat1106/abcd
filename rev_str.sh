echo "Enter the string to be reserved:"
read s
len=${#s}
for (( i = $len-1; i>= 0; i-- ))
do
	new=$new${s:$i:1}
done
echo "The reserved string would be: $new"
