import warnings
from pathlib import Path

import lyricsgenius
from docx import Document
from dotenv import dotenv_values

from lyrics_translator.translator import Translator
from lyrics_translator.saver import Saver

config = dotenv_values(".env")
genius = lyricsgenius.Genius(config["GENIUS_ACCESS_TOKEN"])


class LyricsTranslator(object):
    def __init__(
        self,
        song: str,
        artist: str,
        language: str,
        origin_language="en",
        testing: bool = False,
    ):
        self.song = song
        self.artist = artist
        self.language = language
        self.origin_language = origin_language
        self.testing = testing
        self.text = None
        self.translation = None

        self.translator = Translator(
            language=self.language, origin_language=self.origin_language
        )
        self.translator.get_translator_pipeline()

    def get_song_translations(self) -> None:
        """download the song lyrics from the API and translate the lyrics"""
        self.download_lyrics()
        self.translate()

    def download_lyrics(self, get_full_info: bool = False) -> str:
        """Download the lyrics of the song using the `genius` API

        Args:
            get_full_info (bool, optional): _description_. Defaults to False.

        Returns:
            str: _description_
        """
        try:
            if self.testing:
                genius_song = None
            else:
                genius_song = genius.search_song(
                    self.song, self.artist, get_full_info=get_full_info
                )
        except KeyError:
            pass

        if not genius_song:
            message = f"not found - song: {self.song}, artist: {self.artist}"
            warnings.warn(message)
            self.text = ""
        else:
            self.text = genius_song.lyrics
        return self.text

    def translate(self) -> str:
        """Translate the lyrics into the target language

        Returns:
            str: _description_
        """
        if self.testing:
            self.translation = "some test text"
        else:
            self.translation = self.translator.translate(self.text)

    def save(self, folder: Path, kind: str = "txt") -> None:
        """_summary_

        Args:
            folder (Path): _description_
            kind (str, optional): _description_. Defaults to "txt".
        """
        saver = Saver(
            song=self.song,
            artist=self.artist,
            translation=self.translation,
            language=self.language,
        )
        saver.save(folder=folder, kind=kind)

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        seperator = "----" * 10
        string = [self.text, seperator, self.translation]
        return "\n".join(string)
