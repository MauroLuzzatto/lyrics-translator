from pathlib import Path
from typing import Optional

from lyrics_translator.core.saver import Saver
from lyrics_translator.core.utils import MockGeniusSong


class Lyrics(object):
    def __init__(self, genius, song: str, artist: str, testing: bool = None) -> None:
        """_summary_

        Args:
            genius (_type_): _description_
            song (str): _description_
            artist (str): _description_
            testing (bool, optional): _description_. Defaults to None.
        """
        self.song = song
        self.artist = artist
        self.testing = testing
        self.genius = genius

        self.text: str = None
        self.translation: str = None
        self.language: str = None

    def get_lyrics_text(self, get_full_info: Optional[bool] = False) -> str:
        """Download the lyrics of the song using the `genius` API.

        Args:
            get_full_info (bool): _description_. Defaults to False.

        Returns:
            str: _description_
        """
        if self.testing:
            genius_song = MockGeniusSong(lyrics="<test lyrics>")
        else:
            genius_song = self.genius.search_song(
                self.song, self.artist, get_full_info=get_full_info
            )

        if not genius_song:
            message = f"not found - song: {self.song}, artist: {self.artist}"
            raise ValueError(message)

        self.text = genius_song.lyrics
        return self.text

    def get_translation(self, translator, language: str) -> str:
        """Translate the lyrics into the target language.

        Returns:
            str: _description_
        """
        if not self.text:
            self.text = self.get_lyrics_text()

        self.language = language

        if self.testing:
            self.translation = "<test translation>"
        else:
            self.translation = translator.translate(self.text)

        return self.translation

    def save(self, folder: str = "lyrics", kind: str = "txt") -> None:
        """Save the translated lyrics to a file.

        Args:
            folder (Path): _description_
            kind (str, optional): _description_. Defaults to "txt".
        """

        if not folder:
            folder_path = Path().resolve()
        else:
            folder_path = Path(folder).resolve()
            folder_path.mkdir(parents=True, exist_ok=True)

        saver = Saver(
            song=self.song,
            artist=self.artist,
            translation=self.translation,
            language=self.language,
        )
        saver.save(folder=folder_path, kind=kind)

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
