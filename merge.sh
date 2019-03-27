#!/bin/bash

# https://stackoverflow.com/a/8880633

# delete before declaring to prevent recursion
[ -e grades-merged.csv ] && rm grades-merged.csv
declare -a arr=(grades-*.csv)
# put headers
# https://stackoverflow.com/a/2439587
head -n 1 "${arr[0]}" > grades-merged.csv

## now loop through the above array
for i in "${arr[@]}"
do
   sed 1d "$i" >> grades-merged.csv
   # https://stackoverflow.com/a/5876058
done
