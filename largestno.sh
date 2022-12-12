echo "Enter the no. to be compared"
read var1
read var2
read var3

if [ $var1 -gt $var2 ] && [ $var1 -gt $var3 ]
then
	echo "the first no. entered is largest"
elif [ $var2 -gt $var3 ] && [ $var2 -gt $var3 ]
then
	echo "the second no. is laregest "
else
	echo "The thirs entered is largest"
fi
