import random

def Typoglycemia(str):
    ret = ""
    words = str.split()
    for word in words:
        if len(word) <= 4:
            ret = ret + word + " "
            continue
        new_word = word[0]
        word = word[1:]
        while len(word) > 1:
            i = random.randrange(len(word) - 1)
            new_word = new_word + word[i]
            word = word[0:i] + word[i + 1:]
        new_word = new_word + word[0]
        ret = ret + new_word + " "
    return ret

print(Typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
