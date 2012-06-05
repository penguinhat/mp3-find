#!/usr/bin/env python

import sys, os
import argparse

try:
    import eyeD3 
except ImportError:
    print "Sorry, I can't find the eyeD3 package I need to read mp3 tags."
    print "\nHave you installed eyeD3? If not, you should be able to do this using\nsudo apt-get install eyeD3.\n"
    print "If you are still having problems after trying that, then try visiting the eyeD3 website at http://eyed3.nicfit.net/"

    sys.exit(1)
    #TODO: Write better copy for this error message.

import filters

path = os.getcwd()

#TODO: Tidy up

parser = argparse.ArgumentParser(description='search for mp3 files using filters based on mp3 metadata')

parser.add_argument('--artist',help='Filter by artist name, will return *<artist>*')
parser.add_argument('--title',help='Filter by title name, will return *<title>*')
parser.add_argument('--album',help='Filter by album name, will return *<album>*')
parser.add_argument('-0','--print0',action='store_true',help='Split output by null character instead of by newline (useful if you pipe into xargs -0)')
#TODO: Add positition dir argument?
#TODO: Add -r argument

args = parser.parse_args()

filter_map = {
    'artist':filters.get_artist,
    'title':filters.get_title,
    'album':filters.get_album,
    #TODO: Add more filters 
}


filters = [] #List of (function,argument) tuples to filter argument by

for key, func in filter_map.iteritems():
    value = getattr(args,key)
    if value:
        filters.append( (func,value) )

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
        if args.print0:
            sys.stdout.write('%s\x00' % f) #Seperate with null character
        else:
            print f
