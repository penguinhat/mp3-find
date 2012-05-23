import eyeD3

def get_artist(tag,query):
    return query in tag.getArtist() 

def get_title(tag,query):
    return query in tag.getTitle() 

def get_album(tag,query):
    return query in tag.getAlbum()
