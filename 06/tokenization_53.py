import xml.etree.ElementTree as ET

def tokenize():
    tree = ET.parse('nlp.txt.xml')
    root = tree.getroot()

    with open('tokenization.txt', 'w') as fout:
        for word in root.iter('word'):
            fout.write(word.text + '\n')
    
        
