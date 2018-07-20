cut -f 1 mining.txt | sort | uniq -c | sort -r | less
cut -f 1,2 mining.txt | sort | uniq -c | sort -r | less
