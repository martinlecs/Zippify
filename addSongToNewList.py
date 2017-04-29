import sys
import spotipy
import spotipy.util as util
import json

scope = 'playlist-modify-public'

if len(sys.argv) > 3:
    #note username is actually the userid
    username = sys.argv[1]
    playlist_name = sys.argv[2]

    i = 3
    track_ids = []
    while(i < len(sys.argv)):
        track_ids.append(sys.argv[i])
        i += 1
else:
    print("Usage: %s username playlist_name track_id ..." % (sys.argv[0],))
    sys.exit()


token = util.prompt_for_user_token(username, scope)

if token:

    #userid = sp.me()['uri'] someone's user id must be processed before this function
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    # # #create a new playlist for yourself
    playlists = sp.user_playlist_create(username, playlist_name, public=True)

    # get playlist id
    plid = playlists['id']

    # # Add songs
    #track = [track_ids]
    results = sp.user_playlist_add_tracks(username, plid, track_ids)
    print(results)


else:
    print("Can't get token for", username)