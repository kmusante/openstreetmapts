import xml.etree.cElementTree as ET

def process_map(filename):
    users ={}
    for _, element in ET.iterparse(filename):
        for child in element:
            if child.tag == 'tag':
                if child.attrib['k'].lower()=='cuisine':
                    if child.attrib['v'] not in users:# and x!=None:
                                    
                        users[child.attrib['v'].lower()]=1
                    else:
                        users[child.attrib['v'].lower()]=users[child.attrib['v'].lower()]+1
                    

    return users
# get dictionary of different types of restaurants
rest_type = process_map('samplek100.osm')
print rest_type