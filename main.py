from pathlib import Path

import torch

from lyrics_translator import LyricsTranslator
from lyrics_translator.utils import create_folder, get_base_path

torch.multiprocessing.freeze_support()


if __name__ == "__main__":

    base_path = get_base_path()
    save_folder = create_folder(Path(base_path / "lyrics"))
    save = True

    songs = [
        ("Surfin' U.S.A.", "The Beach Boys", "de"),
        ("Surfin' U.S.A.", "The Beach Boys", "sv"),
        # ("We are your friends", "Justice"),
        # ("Why'd You only call me when you're high?", "Arctic Monkeys"),
        # ("Can't Stop", "Red Hot Chili Peppers"),
        # ("À cause des garçons", "Yelle"),
        # ("Walking on a dream", "Empire of the Sun"),
        # ("Last Nite", "The Strokes"),
        # ("Hello", "Martin Solveig"),
    ]

    for index, (song, artist, language) in enumerate(songs):
        lyrics = LyricsTranslator(song, artist, language, testing=True)
        lyrics.get_song_translations()
        lyrics.save(save_folder)
        print(index, lyrics)
