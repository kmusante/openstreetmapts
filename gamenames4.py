import xml.etree.cElementTree as ET

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        for child in element:
            if child.tag == 'tag':
                if child.attrib['k'].lower() == 'name':
                    #print users
                    users.add(child.attrib['v'].lower())
    

    return users
# returns a list of names of location
# file can be much larger as use iterparse
# gets name of location
name = process_map('samplek100.osm')
print name