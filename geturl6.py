import xml.etree.cElementTree as ET

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        for child in element:
            if child.tag == 'tag':
                if child.attrib['k'].lower()=='website':
                    users.add(child.attrib['v'].lower())
                    

    return users
#provides list of websites
website = process_map('samplek100.osm')
print website