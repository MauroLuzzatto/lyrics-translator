import json
from pathlib import Path


def split_lyrics(text):
    return text.replace("[", "\n----\n[").split("\n")


def get_base_path():
    return Path(__file__).parent.parent.absolute()


def create_folder(path):
    """
    create folder, if it doesn't already exist
    """
    Path(path).mkdir(parents=True, exist_ok=True)
    return path


def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def read_songs(folder: Path, file: str = "songs.txt"):
    with open(Path(folder / file), encoding="utf-8") as f:
        songs = f.read()
    return [song.split(",") for song in songs.split("\n")]


class MockGeniusSong:
    def __init__(self, lyrics):
        self.lyrics = lyrics
