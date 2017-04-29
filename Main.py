import sys
import spotipy
import spotipy.util as util
import json
import re
import os

from read_a_playlist import getTracks
from merge import merge
from user_playlists import getPlaylists

scope = 'playlist-modify-public'

#Initial Call Main.py Userid 
#Receives a userid, will return a hash of h{songName} = songId
def findPlayLists(username = None):
    if username is not None:
        #note username is actually the userid
        playlist_options = getPlaylists(username)
        #print playlist_options
        return playlist_options
    else:
        print("Usage: %s username ..." % (sys.argv[0],))
        sys.exit()
        return

def makePlaylist(username, playlist_options, playlist_name, playlist_url):
    #Display options -> Front end   
    keys = playlist_options.keys()
    r = re.compile(".*"+playlist_name+".*")
    playlist_id = filter(r.match, keys)
    playlist_id = playlist_options[playlist_id[0]]
    #Track 1 = Playlist id -> need to use id to get list of tracks
    track1 = getTracks(name=username, playlist_input=playlist_id) 
    #Track 2 = url -> need to use url to get list of tracks
    track2 = getTracks(name=playlist_url)

    #merge playlists
    # get a list of songs that will be added into the new playlist
    track_ids = merge(track1, track2)
    token = util.prompt_for_user_token(username, scope)
    os.remove(".cache-" + username)
    if token:
    #userid = sp.me()['uri'] someone's user id must be processed before this function
        sp = spotipy.Spotify(auth=token)
        sp.trace = False

    # # #create a new playlist for yourself
        playlists = sp.user_playlist_create(username, playlist_name, public=True)
    # get playlist id
        plid = playlists['id']

    # # Add songs
        if (os.path.exists(".cache-" + username)):
            print "file deleted"
            os.remove(".cache-" + username)
        results = sp.user_playlist_add_tracks(username, plid, track_ids)
        print(results)
        return results

    else:
        print("Can't get token for", username)

makePlaylist(username='12186663114', playlist_options=findPlayLists(username='12186663114'),playlist_name='test2',playlist_url='https://open.spotify.com/user/12186663114/playlist/5iBkCrMuq3XB6ti9ZfjhuX')
