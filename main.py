from pathlib import Path
from typing import List, Tuple

import torch

from lyrics_translator import SongTranslator
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
        song_instance = SongTranslator(song, artist, language)
        song_instance.get_song_translations()
        song_instance.save(save_folder)
        print(index, song_instance)
