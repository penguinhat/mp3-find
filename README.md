mpfind
======

Command line tool like find but works on mp3 metadata

Examples
========

mpfind
Print all mp3 files in current directory and subdirecories to stdout

mpfind --artist kesha -0 | xargs -0 cp '{}' -t ~/foo/
Use mpfind to get a null seperated list of all songs by Kesha in current working directory or sub directories, then pipe this list into xargs and copy to ~/foo directory

TODO
====

Give nicer error if eyeD3 doesn't exist
Look into using another library to parse mp3 tags?
    Need one that is simple for users to install
    Need one that is simple to use
Add -r argument for recurisve directory traversal instead of having this be the default
Add more filters 
