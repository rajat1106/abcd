#Assignment4 - 5th probelm

echo "Enter a number to be reversed"
read n
rev=0
sd=0
while (($n > 0 ))
do
	sd=$(( $n %10 ))
	rev=$(( $rev*10 + $sd ))
	n=$(( $n/10 ))
done

echo "Reverse of the number is $rev"
