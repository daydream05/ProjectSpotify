import sys
import spotipy
import spotipy.util
import pandas as pd
import os


client_id ='4dc6c4e1ad194273bf4370d78a1e4c0f'
client_secret = '77f6d3ef1ee84673907c5a2763c9b999'
redirect_uri = 'http://example.com/callback/'


def get_track_artists(dataframe):
    '''Get all the artists the collaborated in a track. '''

    # We will use this empty to join our dataframes into one csv file.
    # It has the same columns as the generated ones.
    frames = []

    url_list = dataframe['URL'].tolist()
    # TODO Max number of tracks to search for is 50 per call. Create a loop so that we can loop every 50 and call a new request each time

    url_list = url_list[:49]

    # This is a dictionary with one key, 'tracks'
    tracks_dictionary = sp.tracks(url_list)
    # The outer for loop will only loop once because we only have one key.
    for key, tracks in tracks_dictionary.items():
        for index, track in enumerate(tracks):
            # We enumrate each track so we can call on the url_list
            # So we can tag each artist with the url used to call them in the first place.
            track_url = url_list[index]

            # THIS IS WHAT HOLDS OUR ARTIST INFORMATION
            artists = track['artists']
            for artist in artists:
                data = pd.DataFrame.from_dict(artist)
                data['track_url'] = track_url
                frames.append(data)

    result = pd.concat(frames)
    result.to_csv("all_artists.csv")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Need your username!")
        print('usage: python userplay_lists.py [username]')
        print('using custom username warknight')

    username = 'warknight'
    token = spotipy.util.prompt_for_user_token(username,
                                               client_id = client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri)

    if token:
        sp = spotipy.Spotify(auth=token)
        dir_path = os.getcwd()
        project_dir = os.path.abspath(os.path.join(dir_path, os.pardir))

        unique_tracks_df = pd.read_csv(project_dir+"\\top200\\top200_combined\\unique_tracks.csv")
        get_track_artists(unique_tracks_df)

    else:
        print("Can't get token for ", username)

