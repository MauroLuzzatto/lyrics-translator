import warnings
from pathlib import Path
from typing import List, Tuple

import lyricsgenius
import torch
from dotenv import dotenv_values

from lyrics_translator.song_instance import SongInstance
from lyrics_translator.translation import (get_translation,
                                           get_translator_pipeline)
from lyrics_translator.utils import create_folder, get_base_path

torch.multiprocessing.freeze_support()


base_path = get_base_path()
save_folder = create_folder(Path(base_path / "lyrics"))


config = dotenv_values(".env")
genius = lyricsgenius.Genius(config["GENIUS_ACCESS_TOKEN"])


def get_song_translations(
    song_list: List[Tuple[str, str]], language: str, save: bool = True
):
    """_summary_

    Args:
        song_list (List[Tuple[str, str]]): _description_
        language (str): _description_
        save (bool, optional): _description_. Defaults to True.
    """
    translator = get_translator_pipeline(language)
    for index, (song, artist) in enumerate(song_list):

        song_instance = SongInstance(song, artist, language)
        try:
            # download the lyrics
            genius_song = genius.search_song(song, artist, get_full_info=False)
        except KeyError:
            continue

        if not genius_song:
            message = f"not found - song: {song}, artist: {artist}"
            warnings.warn(message)
            continue

        text = genius_song.lyrics
        song_instance.set_text(text)

        translation = get_translation(text, translator)
        song_instance.set_translation(translation)

        if save:
            song_instance.save(save_folder)

        print(song_instance)


if __name__ == "__main__":

    song_list = [
        ("Surfin' U.S.A.", "The Beach Boys"),
        # ("We are your friends", "Justice"),
        # ("Why'd You only call me when you're high?", "Arctic Monkeys"),
        # ("Can't Stop", "Red Hot Chili Peppers"),
        # ("À cause des garçons", "Yelle"),
        # ("Walking on a dream", "Empire of the Sun"),
        # ("Last Nite", "The Strokes"),
        # ("Hello", "Martin Solveig"),
    ]

    get_song_translations(song_list, language="de")
    get_song_translations(song_list, language="sv")
