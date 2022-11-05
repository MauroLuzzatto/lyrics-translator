from lyrics_translator import LyricsTranslator

if __name__ == "__main__":

    song = "Surfin' U.S.A."
    artist = "The Beach Boys"
    language = "de"

    translator = LyricsTranslator(language)
    lyrics = translator.get_song_translation(song, artist)
    print(lyrics)

    lyrics.save()
