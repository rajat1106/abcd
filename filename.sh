
echo "Enter the name of first file"
read file1

echo "Enter the name of second file"
read file2

touch $file1 && touch $file2
echo "Files $file1 and $file2  are created"
