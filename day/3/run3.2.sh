set -v

# Right 1, down 1
python day3.py $1 --x 1 --y 1 -v

# Right 3, down 1 (default)
python day3.py $1 -v

# Right 5, down 1
python day3.py $1 --x 5 --y 1 -v

# Right 7, down 1
python day3.py $1 --x 7 --y 1 -v

# Right 1, down 2 
python day3.py $1 --x 1 --y 2 -v