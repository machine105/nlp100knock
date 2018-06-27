cut -f 1 $1 | sort | uniq -c | sort -r -n -k 1,1
