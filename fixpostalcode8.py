import xml.etree.cElementTree as ET

def process_postcode(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        for child in element:
            for tag in child.iter("tag"):
                if tag.attrib['k']=='addr:postcode':
                    if len(tag.attrib['v'])==9 and tag.attrib['v'].isdigit():
                        tag.attrib['v']=tag.attrib['v'][0:4]
                        
                    if tag.attrib['v'].isdigit()==False:
                        users.add(tag.attrib['v'])
                    if tag.attrib['v']==5 or tag.attrib['v']==9:
                        users.add(tag.attrib['v'])
    return users

# truncates 9 digit post codes to 5
# returns all non digit entries and entries not equal to either 9 or 5 digits

print(process_postcode('samplek100.osm'))
