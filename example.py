
from lyrics_translator import LyricsTranslator

if __name__ == "__main__":


    song = "Surfin' U.S.A."
    artist = "The Beach Boys"
    language = "de"

    lyrics = LyricsTranslator(song, artist, language)
    lyrics.get_song_translation()
    print(lyrics)
