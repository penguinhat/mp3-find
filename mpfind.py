#!/usr/bin/env python

import eyeD3
import filters
import sys, os

#Take in args
# mpfind [expressions]

path = os.getcwd()

#TODO: Tidy up
#TODO: Add --help
#TODO: Validate input (use a proper library for this)

filter_map = {
    '-artist':filters.get_artist,
    '-title':filters.get_title,
    '-album':filters.get_album,
    #TODO: Add more filters 
}

filters = [] #List of (function,argument) tuples to filter argument by

func = None
for arg in sys.argv[1:]:
    if func:
        filters.append( (func,arg) )
        func = None
    else:
        func = filter_map[arg]

def run_filters(mp3):
    """Takes in a path to an mp3 files and runs all the filters
    on it.
    
    Returns True if all filters are true or no filers
    else returns False"""

    if not filters:
        return True

    mp3_tag = eyeD3.Tag()
    mp3_tag.link(mp3)

    for func, arg in filters:
        if not func(mp3_tag,arg):
            return False

    return True

for dirpath, dirnames, files in os.walk(os.getcwd()):

    join_path = lambda file:os.path.join(dirpath,file)

    mp3s = filter(eyeD3.isMp3File,map(join_path,files))

    if filters:
        mp3s = filter(run_filters,mp3s)

    #Render out paths
    def render_path(mp3):
        return os.path.join(dirpath,mp3)

    files = map(render_path,mp3s)
    for f in files:
        print f
