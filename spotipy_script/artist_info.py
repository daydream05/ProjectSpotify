import sys
import spotipy
import spotipy.util



client_id ='4dc6c4e1ad194273bf4370d78a1e4c0f'
client_secret = '77f6d3ef1ee84673907c5a2763c9b999'
redirect_uri = 'http://example.com/callback/'




if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Need your username!")
        print('usage: python userplay_lists.py [username]')

    username = 'warknight'
    token = spotipy.util.prompt_for_user_token(username,
                                               client_id = client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri)

    if token:
        url = 'https://open.spotify.com/track/1ds2QsfhAAfRiaFMGDzrdb'
        sp = spotipy.Spotify(auth=token)
        features = sp.audio_features(url)
        print(features)

    else:
        print("Can't get token for ", username)