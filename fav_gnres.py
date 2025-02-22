"""
Given a map Map<String, List> userSongs with user names as keys and a list of all the songs that the user has listened to as values.

Also given a map Map<String, List> songGenres, with song genre as keys and a list of all the songs within that genre as values. The song can only belong to only one genre.

The task is to return a map Map<String, List>, where the key is a user name and the value is a list of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.

Example 1:

Input:

userSongs = {

"David": ["song1", "song2", "song3", "song4", "song8"],

"Emma": ["song5", "song6", "song7"]

},

songGenres = {

"Rock": ["song1", "song3"],

"Dubstep": ["song7"],

"Techno": ["song2", "song4"],

"Pop": ["song5", "song6"],

"Jazz": ["song8", "song9"]

}

Output: {

"David": ["Rock", "Techno"],

"Emma": ["Pop"]

}
"""
from typing import Dict, List
from collections import defaultdict, Counter
def fav_gnres(userSongs: Dict[str, List[str]],songGenres: Dict[str, List[str]]) ->  Dict[str, List[str]]:
    song_to_Gnre_map = {}
    for k, v in songGenres.items():
        for song in v:
            song_to_Gnre_map[song] = k
    user_gnre_map = defaultdict(Counter)
    for u, songs in userSongs.items():
        user_gnre_map[u] = Counter()
        for s in songs:
            gnre = song_to_Gnre_map[s]
            user_gnre_map[u][gnre]+=1
    result = {}
    for u, gnre in user_gnre_map.items():
        fav_gnres = []
        max_f = 0
        for g, f in gnre.items():
            if f > max_f:
                max_f = f
                fav_gnres = [g]
            elif f == max_f:
                fav_gnres.append(g)
        result[u] = fav_gnres
    return result
        
    
           
userSongs = {

"David": ["song1", "song2", "song3", "song4", "song8"],

"Emma": ["song5", "song6", "song7"]

}

songGenres = {

"Rock": ["song1", "song3"],

"Dubstep": ["song7"],

"Techno": ["song2", "song4"],

"Pop": ["song5", "song6"],

"Jazz": ["song8", "song9"]

}

print(fav_gnres(userSongs, songGenres))