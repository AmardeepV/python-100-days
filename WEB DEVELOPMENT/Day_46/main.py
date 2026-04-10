import requests
from typing import List
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json


URL = "https://ukf.com/read/let-it-rolls-top-100-dnb-full-results/"
OUTPUT_FILE = "songs.json"


def fetch_page(url: str) -> str:
    # fetch the html content from the website
    responce = requests.get(URL)
    responce.raise_for_status()
    return responce.text


def parse_songs_title(html: str) -> List[str]:
    # scrape the songs from the html content and output as a list
    soup = BeautifulSoup(html, "html.parser")
    elements = soup.find_all('strong')
    list_of_songs = []
    for each in elements:
        try:
            number, album = each.get_text().split('. ', 1)
            composer, song = album.split(' – ', 1)
        except ValueError:
            print(
                f"Data is not in the correct format, skipping it {number, album}")
        list_of_songs.append((song, composer))
    return list_of_songs


def write_to_file(songs: List[tuple], filename: str) -> None:

    # write the list of songs in a txt file
    data = json.dumps(songs, indent=4)
    with open(filename, 'w') as file:
        file.write(data)


def main() -> None:
    # html_content = fetch_page(URL)
    # songs_list = parse_songs_title(html_content)
    # write_to_file(songs_list, OUTPUT_FILE)
    album = read_song_artist(OUTPUT_FILE)
    spotify_auth(album)


def spotify_auth(album: list) -> None:
    client_id = os.environ.get("SPOTIFY_CLIENT_ID")
    client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private playlist-modify-public user-read-private",
            redirect_uri="https://example.com",
            client_id=client_id,
            client_secret=client_secret,
            show_dialog=True,
            cache_path="token.txt"
        )
    )

    song_uris = []
    for data in album:
        result = sp.search(q=f"track:{data[0]} artist:{data[1]}",
                           type="track", market="AT")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{data[0]} does not exist")
    user = sp.current_user()
    print("USER ID:", user["id"])
    print("DISPLAY NAME:", user["display_name"])
    playlist = sp.user_playlist_create(
        user=sp.current_user()["id"],
        name="Top DNB Songs",
        public=False
    )
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


def read_song_artist(filepath: str) -> list:
    with open(filepath) as file:
        data = json.load(file)

    return data


if __name__ == '__main__':
    main()
