def n_gram(n, seq):
    ngram = []
    for i in range(len(seq) - n + 1):
        if not seq[i:i + n] in ngram:
            ngram.append(seq[i:i + n])
    return ngram

str = "I am NLPer."
print(n_gram(2, str))
splited = str.replace(".", " ").split()
print(n_gram(2, splited))
