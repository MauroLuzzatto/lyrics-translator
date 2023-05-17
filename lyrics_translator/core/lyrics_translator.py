import lyricsgenius
from dotenv import dotenv_values

from lyrics_translator.core.lyrics import Lyrics
from lyrics_translator.core.translator import Translator

MANDATORY_ENV_VARS = ["GENIUS_ACCESS_TOKEN"]


class LyricsTranslator(object):
    def __init__(
        self,
        language: str = "de",
        origin_language="en",
        config: dict = None,
        model_name: str = None,
    ) -> None:
        """LyricsTranslator main class, which uses the Lyrics class to fetch
        lyrics and translates them into the target language.

        Args:
            language (str): target language that the lyrics should be transalted into. Defaults to "de".
            origin_language (str, optional): set optional current language of the lyrics for more advanced traslations. Defaults to "en".
            config (dict): config file to pass in environment variables
            model_name (str, optional): model name to use for the translation. Defaults to None (uses the default model for the language pair)

        Raises:
            EnvironmentError: _description_
        """
        self.language = language
        self.origin_language = origin_language

        if config is None:
            self.config = dotenv_values(".env")
        else:
            self.config = config

        for env_var in MANDATORY_ENV_VARS:
            if env_var not in self.config:
                message = (
                    f"Failed because the envrionment variable '{env_var}' is not set."
                    f" Add '{env_var}' to the '.env' file and try it again!"
                )
                raise EnvironmentError(message)

        if not model_name:
            model_name = self.config.get("MODEL_NAME", None)

        self.translator = Translator(
            language=self.language,
            origin_language=self.origin_language,
            model_name=model_name,
        )
        self.translator.get_translator_pipeline()

        self.genius = lyricsgenius.Genius(
            self.config["GENIUS_ACCESS_TOKEN"], timeout=10, retries=3
        )

    def get_song_lyrics(self, song, artist, testing: bool = False):
        """retrun only the lyrics of the song"""
        lyrics = Lyrics(genius=self.genius, song=song, artist=artist, testing=testing)
        text = lyrics.get_lyrics_text()
        return text

    def get_song_translation(self, song, artist, testing: bool = False) -> None:
        """Download the song lyrics from the API and translate them using the Lyrics class."""
        lyrics = Lyrics(genius=self.genius, song=song, artist=artist, testing=testing)
        translation = lyrics.get_translation(
            translator=self.translator, language=self.language
        )
        return translation

    def __repr__(self) -> str:
        """LyricsTranslator representation

        Returns:
            str: returns the string to create the same instance
        """
        return (
            "LyricsTranslator("
            f" language={self.language}, origin_language={self.origin_language})"
        )
