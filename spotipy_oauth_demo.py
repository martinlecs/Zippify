# https://github.com/plamere/spotipy/blob/master/spotipy/util.py
# http://www.acmesystems.it/python_httpd

from bottle import route, run, request
# from run import app
from flask import Flask, render_template
import spotipy
from spotipy import oauth2

PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID = '150244b7f272437fa52d365830d70012'
SPOTIPY_CLIENT_SECRET = '56d4b147fd024d399d276b74156448f7'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'

result = {}
app = Flask(__name__)
sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )

@app.route('/playlists')
def index():

    access_token = ""

    token_info = sp_oauth.get_cached_token()

    if token_info:
        print("Found cached token!")
        access_token = token_info['access_token']
    else:
        url = request.url
        code = sp_oauth.parse_response_code(url)
        if code:
            print("Found Spotify auth code in Request URL! Trying to get valid access token...")
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']

    if access_token:
        print("Access token available! Trying to get user information...")
        sp = spotipy.Spotify(access_token)
        user = sp.current_user()
        playlists = sp.user_playlists(user['id'])

        for playlist in playlists['items']:
            result[playlist['name']] = playlist['id']

        return render_template('app.html', result = result)
        # return result


    else:
        return htmlForLoginButton()

def htmlForLoginButton():
    auth_url = getSPOauthURI()
    htmlLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
    return htmlLoginButton

def getSPOauthURI():
    auth_url = sp_oauth.get_authorize_url()
    return auth_url

# run(host='', port=8080)

if __name__ == '__main__':
    app.run(debug = True)
