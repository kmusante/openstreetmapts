# print tags in sample file
# Counts number of each type of tag

import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict
import re

def count_tags(filename):
    tags={}
    for event, elem in ET.iterparse(filename):
        #print elem.tag, '**'#tag names
        #print elem.attrib, '&&'#dictionary
        for child in elem:
            if elem.tag in tags.keys():
                tags[elem.tag]=tags[elem.tag]+1
            else:
                tags[elem.tag]=1
    #print tags
    return tags

# do not do this for smaller files as takes too long
# gives an idea of the total # of tags in entire file
count_tags('samplek100.osm')
