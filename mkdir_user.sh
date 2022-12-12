echo "Enter the name of the first directory:"
read dir1

echo "Enter the name of the second directory:"
read dir2

mkdir -p -- ./$dir1
mkdir -p -- ./$dir2
echo "The two new directories created are $dir1 and $dir2"
