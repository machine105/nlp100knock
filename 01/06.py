import prob05

str1 = "paraparaparadise"
str2 = "paragraph"

X = prob05.n_gram(2, str1)
Y = prob05.n_gram(2, str2)

XandY = []
XorY = X
XminusY = []
print(X)
print(Y)

for elem in X:
    if elem in Y:
        XandY.append(elem)
print(XandY)

for elem in Y:
    if not elem in X:
        XorY.append(elem)
print(XorY)

for elem in X:
    if not elem in Y:
        XminusY.append(elem)
print(XminusY)
