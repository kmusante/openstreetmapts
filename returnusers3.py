import xml.etree.cElementTree as ET
import pprint
import re

def get_user(element):
    #can return any element such as k, v, lat, lon, uid, id, user, etc
    return element.get('user')

# counts number of times field is in database
def process_map(filename):
    users = {}#set()
    for _, element in ET.iterparse(filename):
        x=get_user(element)
        if x not in users:# and x!=None:
            users[x]=1
        else:
            users[x]=users[x]+1
        
    #print users
    return users
# returns user name and how many entries made
# do not do on entire file as file is too large
process_map('samplek100.osm')
