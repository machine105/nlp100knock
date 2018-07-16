from Chunk_41 import read_cabocha
import codecs

def extract_verb_patterns():
    text = read_cabocha('neko.txt.cabocha')
    fout = codecs.open('patterns.txt', 'w', 'utf-8')
    for sentence in text:
        for chunk in sentence:
            verb = chunk.first_verb()
            if verb:
                line = verb + '\t'
                cases = []
                for src in chunk.srcs:
                    case = sentence[src].case()
                    if case:
                        cases.append(case)
                if cases:
                    line = line + u' '.join(sorted(cases))
                    fout.write(line + '\n')
    fout.close()
