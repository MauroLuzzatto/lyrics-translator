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


class MockGeniusSong:
    def __init__(self, lyrics):
        self.lyrics = lyrics
