import xml.etree.ElementTree  as ET

def tagging():
    tree = ET.parse('nlp.txt.xml')
    root = tree.getroot()

    with open('tag.txt', 'w') as fout:
        for token in root.iter('token'):
            word = token.find('word').text
            lemma = token.find('lemma').text
            pos = token.find('POS').text
            fout.write('\t'.join([word, lemma, pos]) + '\n')
