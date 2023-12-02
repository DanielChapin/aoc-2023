#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $ ./new_day.sh <day>"
    exit
fi

mkdir "$1"
cd "$1"
touch example.txt
touch input0.txt
cp ../template.py part1.py