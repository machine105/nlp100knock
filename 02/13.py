f = open('col1.txt')
col1 = f.read().split('\n')
f.close()

f = open('col2.txt')
col2 = f.read().split('\n')
f.close()

f = open('merged.txt', 'w')
for cols in zip(col1, col2):
    f.write('\t'.join(cols))
    f.write('\n')
f.close()
