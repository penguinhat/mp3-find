import eyeD3

def get_artist(tag,query):
    return query.lower() in tag.getArtist().lower()

def get_title(tag,query):
    return query.lower() in tag.getTitle().lower() 

def get_album(tag,query):
    return query.lower() in tag.getAlbum().lower()
