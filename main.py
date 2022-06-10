from pathlib import Path

import torch

from lyrics_translator import LyricsTranslator
from lyrics_translator import create_folder, get_base_path

torch.multiprocessing.freeze_support()


if __name__ == "__main__":

    base_path = get_base_path()
    resources_path = Path(base_path / "resources")
    folder = create_folder(Path(base_path / "lyrics"))

    songs = [
        ("Surfin' U.S.A.", "The Beach Boys", "de"),
        ("Surfin' U.S.A.", "The Beach Boys", "sv"),
    ]

    for index, (song, artist, language) in enumerate(songs):
        print(language)
        lyrics = LyricsTranslator(song, artist, language, testing=True)
        lyrics.get_song_translations()
        lyrics.save(folder)
        print(index, lyrics)
