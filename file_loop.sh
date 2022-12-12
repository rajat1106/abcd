echo "enter the name of 3 files "
read file1
read file2
read file3

for x in $file1 $file2 $file3
do
	touch $x
	echo "$x file created successfully"
done
