import xml.etree.ElementTree as ET

def coref():
    with open('nlp.txt') as fin:
        text = fin.read()

    tree = ET.parse('nlp.txt.xml')
    root = tree.getroot().find('document')
    offsets = [] # (index, offset) index in original text

    coref_root = root.find('coreference')
    assert coref_root
    for coref in coref_root.iter('coreference'):
        rprm = ''
        test = []
        for mention in coref.iter('mention'):
            if mention.get('representative'):
                # representative mention
                rprm = mention.findtext('text')
                test = []
                for sentence in root.iter('sentence'):
                    if sentence.get('id') != mention.findtext('sentence'):
                        continue
                    for token in sentence.iter('token'):
                        if int(token.get('id')) < int(mention.findtext('start')):
                            continue
                        if int(token.get('id')) >= int(mention.findtext('end')):
                            assert ' '.join(test) == rprm, ' '.join(test) + ' != ' + rprm
                            break
                        test.append(token.findtext('word'))
            else:
                # mention
                continue
                            
                
