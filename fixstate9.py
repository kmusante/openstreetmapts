import xml.etree.cElementTree as ET
import pprint

OSMFILE = 'samplek100.osm'

def process_state(filename):
    users = {}
    for _, element in ET.iterparse(filename):
        for child in element:
            if child.tag == 'way':
                for tag in child.iter("tag"):
                    if tag.attrib['k']=='addr:state':
                        if tag.attrib['v'] not in users: # and x!=None:
                            users[tag.attrib['v']]=1
                        else:
                            users[tag.attrib['v']]=users[tag.attrib['v']]+1
    return users
# return dictionary and frequency number of times each state format listed


def update_state(state):
    if state=='california' or state=='California' or state=='ca' or zip=='Ca':
        state='CA'
    else:
        return state
    
    return state


# updates state

def update_states():
    state_ab=process_state(OSMFILE)
    #formats dictionary
    pprint.pprint(dict(state_ab))
    #state_ab=process_state(OSMFILE)
    #formats dictionary
    #pprint.pprint(dict(users))

    for state_ab, ways in state_ab.iteritems():
        
        better_state = update_state(state_ab)
        #print better_state, '&&&&'
        
# truncates  states name to 'CA' OR returns all non identified entries 

#update_states()
