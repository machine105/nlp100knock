import xml.etree.ElementTree as ET

def extract_nnp():
    tree = ET.parse('nlp.txt.xml')
    root = tree.getroot()

    with open('nnp.txt', 'w') as fout:
        for token in root.iter('token'):
            if token.find('POS').text == 'NNP':
                fout.write(token.find('word').text + '\n')
