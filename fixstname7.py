import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "samplek100.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

# ignore expected case
expected = ["Street", "Avenue", "Alley", "Bay", "Boulevard", "Drive", "Center", "Court", "Place", "Plaza" "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "Real", "Way", "Broadway", "Terrace", "Loop"]


'''mapping = { "St": "Street",
            "st": "Street",
            "St.": "Street", 
            "St":  "Street",
            "Ave.": "Avenue",
            "Ave": "Avenue", 
            "AVE": "Avenue",
            "ave": "Avenue,
            "Blvd.": Boulevard
            
            "Rd.": "Road"
            }'''


def audit_street_type(street_types, street_name):
    #finds the last word of the street name and assigns to var m
    m = street_type_re.search(street_name)
    if m:
        #sets var street_type equal to a single word. 
        street_type = m.group()
        #execute only if not in expected list
        if street_type not in expected:
            #adds word to dictionary if not in 'expected'
            street_types[street_type].add(street_name)

#helper function.  identifies tags where street name is listed and returns value
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    #opens the file
    osm_file = open(osmfile, "r")
    #sets street_types equal to default dictionary listed
    street_types = defaultdict(set)
    #iterate through osm file and define each as 'elem'
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        #look for the tag= to 'node' or 'way' as its known that's where street is
        if elem.tag == "node" or elem.tag == "way":
            #iterate over the tag itself
            for tag in elem.iter("tag"):
                #if there is a value in the helper function
                if is_street_name(tag):
                    #conduct function to add to dictionary IF not in expected list
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name, mapping):
    #assign var to regular expression and pull out last word
    last_word = street_type_re.search(name)
    #i dont fully understand this command but I got it from the forums
    #it takes the regular expression and translates it
    last_word = last_word.group()
    for e in mapping:
        if last_word == e:
            print name[:-len(last_word)], '7777'
            name = name[:-len(last_word)] + mapping[e]
            
    return name
# updates street names
audit(OSMFILE)