# BASIC CASE - two playlists with even length and no duplicates

# playlist A
# playlist B
# zipped playlist

# shuffle A
# shuffle B

# go through playlists and add to zipped playlist


# shows a user's playlists (need to be authenticated via oauth)

import sys
import os
import spotipy
import spotipy.util as util

class spotipy.oauth2.SpotifyClientCredentials(client_id='14d31a3e6b944b4d80f3a277e4ea50a2', client_secret='58fe8fcaaadc4799b22ba77c98f843aa', proxies=None)

def show_tracks(results):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists_contents.py [username]")
        sys.exit()

    token = util.prompt_for_user_token(username)

    if token:
        top = 40
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print()
                print(playlist['name'])
                print('  total tracks', playlist['tracks']['total'])
                results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print("Can't get token for", username)
