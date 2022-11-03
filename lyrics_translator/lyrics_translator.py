from pathlib import Path
from typing import Optional

import lyricsgenius

from dotenv import dotenv_values


from lyrics_translator.saver import Saver
from lyrics_translator.translator import Translator
from lyrics_translator.utils import MockGeniusSong

MANDATORY_ENV_VARS = ["GENIUS_ACCESS_TOKEN"]


class LyricsTranslator(object):
    def __init__(
        self,
        song: str,
        artist: str,
        language: str,
        config: dict = None,
        origin_language="en",
        testing: bool = False,
    ):
        """LyricsTranslator main class, which fetches the lyrics and translates them into
        the desired language.

        Args:
            song (str): _description_
            artist (str): _description_
            config (dict): _description_
            language (str): _description_
            origin_language (str, optional): _description_. Defaults to "en".
            testing (bool, optional): _description_. Defaults to False.

        Raises:
            EnvironmentError: _description_
        """
        self.song = song
        self.artist = artist

        for env_var in MANDATORY_ENV_VARS:
            if env_var not in config:
                message = (
                    f"Failed because the envrionment variable '{env_var}' is not set."
                    f" Add '{env_var}' to the '.env' file and try it again!"
                )
                raise EnvironmentError(message)

        if config is None:
            self.config = dotenv_values(".env")
        else:
            self.config = config

        self.language = language
        self.origin_language = origin_language
        self.testing = testing

        self.text = None
        self.translation = None

        self.translator = Translator(
            language=self.language, origin_language=self.origin_language
        )
        self.translator.get_translator_pipeline()

    def get_song_translation(self) -> None:
        """Download the song lyrics from the API and translate the lyrics."""
        self.download_lyrics()
        self.translate()

    def download_lyrics(self, get_full_info: Optional[bool] = False) -> str:
        """Download the lyrics of the song using the `genius` API.

        Args:
            get_full_info (bool): _description_. Defaults to False.

        Returns:
            str: _description_
        """
        if self.testing:
            genius_song = MockGeniusSong(lyrics="test text")
        else:
            genius = lyricsgenius.Genius(
                self.config["GENIUS_ACCESS_TOKEN"], timeout=10, retries=3
            )
            genius_song = genius.search_song(
                self.song, self.artist, get_full_info=get_full_info
            )

        if not genius_song:
            message = f"not found - song: {self.song}, artist: {self.artist}"
            raise ValueError(message)
        self.text = genius_song.lyrics
        return self.text

    def translate(self):
        """Translate the lyrics into the target language.

        Returns:
            str: _description_
        """
        if self.testing:
            self.translation = "test translation"
        else:
            self.translation = self.translator.translate(self.text)

    def save(self, folder: Path, kind: str = "txt") -> None:
        """Save the translated lyrics to a file.

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
        """string version of the LyricsTranslator instance, returns the translated lyrics

        Returns:
            str: _description_
        """
        return self.translation

    def __repr__(self) -> str:
        """LyricsTranslator representation

        Returns:
            str: returns the string to create the same instance
        """
        return (
            f"LyricsTranslator(song={self.song}, artist={self.artist},"
            f" language={self.language}, origin_language={self.origin_language},"
            f" testing={self.testing})"
        )
