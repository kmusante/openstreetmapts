import csv
import os

DATADIR = ""
DATAFILE ="nodes.csv"
DATAFILE1="nodes_tags.csv"
DATAFILE2="ways.csv"
DATAFILE3="ways_nodes.csv"
DATAFILE4="ways_tags.csv"

def parse_file(datafile):
    name = ""
    data = []
    with open(datafile,'rb') as f:
        freader = csv.reader(f)
        name= freader.next()[1]
        next(freader)
        for x in freader:
            data.append(x)
        print len(data)
        #print name, data
        pass
    # Do not change the line below
    return (name, data)
#examine data
parse_file(DATAFILE)