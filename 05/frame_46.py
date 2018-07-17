from Chunk_41 import read_cabocha
import codecs

def extract_verb_frames():
    text = read_cabocha('neko.txt.cabocha')
    fout = codecs.open('frames.txt', 'w', 'utf-8')
    for sentence in text:
        for chunk in sentence:
            verb = chunk.first_verb()
            if verb:
                line = verb + '\t'
                cases = []
                surfaces = []
                for src in chunk.srcs:
                    case = sentence[src].case()
                    if case:
                        cases.append(case)
                        surfaces.append(sentence[src].surface())
                if cases:
                    line = line + u' '.join(sorted(cases)) + '\t' + u' '.join(sorted(surfaces))
                    fout.write(line + '\n')
    fout.close()
