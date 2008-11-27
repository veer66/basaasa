from xml.dom import pulldom

from simplejson import dumps


def get_headword(node):
    headword_nodes = node.getElementsByTagName("headword")
    assert len(headword_nodes) == 1
    headword_node0 = headword_nodes[0]
    headword = headword_node0.firstChild.nodeValue
    return headword

def get_pos(node):
    pos_nodes = node.getElementsByTagName("pos")
    assert len(pos_nodes) <= 1
    if len(pos_nodes) < 1:
        return None
    else:
        pos_node0 = pos_nodes[0]
        return pos_node0.firstChild.nodeValue

def get_translation(node):
    translation_nodes = node.getElementsByTagName("translation")
    assert len(translation_nodes) == 1
    translation_node0 = translation_nodes[0]
    lang = translation_node0.getAttribute("lang") 
    return translation_node0.firstChild.nodeValue, lang 
      
class TeiGen:
    def __init__(self):
        self.headword_entry_map = {}
        
    def add(self, entry):
        self.headword_entry_map.setdefault(entry['headword'], []).append(entry)
      
def main():
    import sys  
    reload(sys)  
    sys.setdefaultencoding('utf-8')
    
    tei_gen = TeiGen()
    events = pulldom.parse("yaitron.xml")
    for (event, node) in events:
        if event == "START_ELEMENT" and node.tagName == "entry":
            events.expandNode(node)
            lang = node.getAttribute("lang")
            headword = get_headword(node)
            pos = get_pos(node)
            translation, trans_lang = get_translation(node)
            
            # headword -> sense
            
            entry = {"headword": headword,
                     "lang": lang,
                     "pos": pos,
                     "translation": {"lang": lang, "text": translation}}      
          
          
            tei_gen.add(entry)  
            #print node.toprettyxml(newl="", indent="")
            #print
            #print
            # print dumps(entry)  
    
if __name__ == '__main__':
    main()
