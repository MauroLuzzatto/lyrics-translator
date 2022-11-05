from pathlib import Path
from typing import Optional

from lyrics_translator.core.saver import Saver
from lyrics_translator.core.utils import MockGeniusSong


class Lyrics(object):
    def __init__(self, song:str, artist:str, testing:bool=None) -> None:
        self.song = song
        self.artist = artist
        self.testing = testing

        self.text: str = None
        self.translation:str = None
        self.language:str = None

    def download_lyrics(self, genius, get_full_info: Optional[bool] = False) -> None:
        """Download the lyrics of the song using the `genius` API.

        Args:
            get_full_info (bool): _description_. Defaults to False.

        Returns:
            str: _description_
        """
        if self.testing:
            genius_song = MockGeniusSong(lyrics="<test lyrics>")
        else:
            genius_song = genius.search_song(
                self.song, self.artist, get_full_info=get_full_info
            )

        if not genius_song:
            message = f"not found - song: {self.song}, artist: {self.artist}"
            raise ValueError(message)

        self.text = genius_song.lyrics

    def translate(self, translator, language:str, short:bool=False) -> None:
        """Translate the lyrics into the target language.

        Returns:
            str: _description_
        """
        self.language = language

        if self.testing:
            self.translation = "<test translation>"
        else:
            self.translation = translator.translate(self.text, short)

    def get_translation(self, translator, language) -> str:
        self.translate(translator, language)
        return self.translation

    def get_lyrics(self, genius) -> str:
        self.download_lyrics(genius)
        return self.lyrics

    def save(self, folder: Path = None, kind: str = "txt") -> None:
        """Save the translated lyrics to a file.

        Args:
            folder (Path): _description_
            kind (str, optional): _description_. Defaults to "txt".
        """

        if folder is None:
            folder = Path().resolve()

        saver = Saver(
            song=self.song,
            artist=self.artist,
            translation=self.translation,
            language=self.language,
        )
        saver.save(folder=folder, kind=kind)

    def __str__(self) -> str:
        """string version of the Lyrics instance, returns the translated lyrics

        Returns:
            str: _description_
        """
        return self.translation

    def __repr__(self) -> str:
        """Lyrics representation

        Returns:
            str: returns the string to create the same instance
        """
        return f"Lyrics(song={self.song}, artist={self.artist})"
