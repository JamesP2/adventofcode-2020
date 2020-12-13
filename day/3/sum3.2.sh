#!/bin/bash
set -v

product=1

# Right 1, down 1
let "product*=$(python day3.py $1 --x 1 --y 1)"

# Right 3, down 1 (default)
let "product*=$(python day3.py $1)"

# Right 5, down 1
let "product*=$(python day3.py $1 --x 5 --y 1)"

# Right 7, down 1
let "product*=$(python day3.py $1 --x 7 --y 1)"

# Right 1, down 2 
let "product*=$(python day3.py $1 --x 1 --y 2)"

echo $product