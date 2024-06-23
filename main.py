
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import pyperclip
class Spotify:
    def __init__(self,clientId,clientSecret,redirectUri,scope) -> None:
        self._clientID = clientId
        self._clientSecret = clientSecret 
        self._redirectUri = redirectUri
        self._scope = scope
        self._sp = None

    
    def oAuth(self):
        
        self._sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id = self._clientID,
            client_secret = self._clientSecret,
            redirect_uri = self._redirectUri,
            scope = self._scope
        ))
        return self._sp
    
    def playlists(self, uId):
        playlists = self._sp.user_playlists(uId)
        return playlists

    def playlists_tracks(self, uId, playlistId):
        #tracks = self._sp.user_playlist_tracks(uId, playlistId) # copied as is
        #return tracks
        tracks = []
        results = self._sp.user_playlist_tracks(uId, playlistId)
        tracks.extend(results['items'])
        while results['next']: # to handle pagination
            results = self._sp.next(results)
            tracks.extend(results['items'])
        return tracks


spo = Spotify(clientId,clientSecret,redirectUri,scope) # enter your own information
spo.oAuth()  # Authenticate and initialize the Spotify client
user_id = <<<insert info>>>
owner_id = <<<insert info>>>
playlists = spo.playlists(owner_id) # switch it to see new KP Playlst

for k,v in enumerate(playlists['items']):
    #if v['owner']['id'] == owner_id: # owner_id
    oinfo = v['name']
    plylstID = v['id']
    ownerId = v['owner']['id']
    print(k, oinfo, plylstID,ownerId,"--->",v['tracks']['total'])
    
    a  = spo.playlists_tracks(owner_id,plylstID)

    for x in range(len(a)): # to handle pagination
    
        print("\t\t\t\t--->", x, a[x]['track']['name']) # to handle pagination
