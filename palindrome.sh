echo "Enter the string"
read s

len=${#s}

for (( i = $len-1; i>= 0; i-- ))
do
	new=$new${s:$i:1}
done
echo "The reserve of it would be:$new"

if [ $s == $new ]
then
 	echo "Its a palindrome"
else
	echo "Not a palindrome"
fi
