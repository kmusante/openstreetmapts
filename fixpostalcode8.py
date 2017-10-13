import xml.etree.cElementTree as ET

OSMFILE="samplek100.osm"

def process_postcode(filename):
    users = {}
    for _, element in ET.iterparse(filename):
        for child in element:
            for tag in child.iter("tag"):
                if tag.attrib['k']=='addr:postcode':
                    if tag.attrib['v'] not in users:
                        users[tag.attrib['v']]=1
                    else:
                        users[tag.attrib['v'].lower()]=users[tag.attrib['v']]+1
                            
                    
    return users

def update_zip(zip):
    if len(zip)==9 and zip.isdigit():
        zip=zip[0:4]
    else:
        return zip
    return zip


# updates street names

def update_street():
    post_code=process_postcode(OSMFILE)
    #formats dictionary
    pprint.pprint(dict(users))

    for post_code, ways in post_code.iteritems():
        for zip in ways:
            better_zip = update_zip(zip)
            
# truncates 9 digit post codes to 5
# returns all non digit entries and entries not equal to either 9 or 5 digits

process_postcode(OSMFILE)
