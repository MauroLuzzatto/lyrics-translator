import json

import requests
from dotenv import dotenv_values


class SpotifyAPI(object):
    def __init__(self, USER_ID, CLIENT_ID, CLIENT_SECRET):

        self.USER_ID = USER_ID

        grant_type = "client_credentials"
        body_params = {"grant_type": grant_type}

        url = "https://accounts.spotify.com/api/token"
        response = requests.post(url, data=body_params, auth=(CLIENT_ID, CLIENT_SECRET))

        token_raw = json.loads(response.text)
        token = token_raw["access_token"]
        self.headers = {"Authorization": "Bearer {}".format(token)}

    def get_playlists(self, limit=20, offset=1):
        # Second step – make a request tox any of the playlists endpoint. Make sure to set a valid value for <spotify_user>.

        r = requests.get(
            url=f"https://api.spotify.com/v1/users/{self.USER_ID}/playlists?limit={limit}&offset={offset}",
            headers=self.headers,
        )

        if r.status_code != 200:
            print(r.status_code)
            exit()

        return (
            json.loads(r.text),
            {item["name"]: item["id"] for item in r.json()["items"]},
        )

    def get_playlist_items(self, playlist_id, limit=100, offset=1):

        r = requests.get(
            url=f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?limit={limit}&offset={offset}",
            headers=self.headers,
        )
        if r.status_code != 200:
            print(r.status_code)
            exit()

        return json.loads(r.text)

    def get_track_info(self, track, artist, limit=4):

        r = requests.get(
            url=f"https://api.spotify.com/v1/search?q=track:{track}%20artist:{artist}&limit={limit}&type=track",
            headers=self.headers,
        )
        return json.loads(r.text)

    def get_artist_info(self, id):

        r = requests.get(
            url=f"https://api.spotify.com/v1/artists/{id}", headers=self.headers
        )
        return json.loads(r.text)

    def get_audio_features(self, id):
        r = requests.get(
            url=f"https://api.spotify.com/v1/audio-features/{id}", headers=self.headers
        )
        return json.loads(r.text)

    def get_audio_analysis(self, id):
        r = requests.get(
            url=f"https://api.spotify.com/v1/audio-analysis/{id}", headers=self.headers
        )
        return json.loads(r.text)

    def post_url(self, url):
        r = requests.get(url=url, headers=self.headers)
        return json.loads(r.text)


track = "one more time"
artist = "daft punk"


if __name__ == "__main__":

    config = dotenv_values(".env")
    user_id = 1157239771
    playlist_id = "3VQvmc9cjrVj7HcjxwN5Jg"

    spotifAPI = SpotifyAPI(
        user_id, config["SPOTIFY_CLIENT_ID"], config["SPOTIFY_CLIENT_SECRET"]
    )
    # playlists, playlist_dict = spotifAPI.get_playlists()

    playlist = spotifAPI.get_playlist_items(playlist_id=playlist_id)

    songs = []
    language = "sv"

    for track in playlist["items"]:
        artist = ", ".join([artist["name"] for artist in track["track"]["artists"]])
        songs.append((track["track"]["name"], artist, language))

    print(songs)
