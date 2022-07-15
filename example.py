from dotenv import dotenv_values

from lyrics_translator import LyricsTranslator


if __name__ == "__main__":

    config = dotenv_values(".env")

    song = "Surfin' U.S.A."
    artist = "The Beach Boys"
    language = "de"

    lyrics = LyricsTranslator(song, artist, config, language)
    lyrics.get_song_translation()
    print(lyrics)
