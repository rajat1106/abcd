#Assignment 4 - 6th problem

echo "Enter the last inded of fibonacci to be printed"
read n
a=0
b=1

echo "The fibonacci series is: "
echo -n "$a, "
echo -n "$b, "

for (( i=0; i<n-2; i++ ))
do
	fn=$((a+b))
	echo -n "$fn, "
	a=$b
	b=$fn
done
echo " "
