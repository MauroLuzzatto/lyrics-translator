from lyrics_translator import LyricsTranslator

if __name__ == "__main__":

    song = "Surfin' U.S.A."
    artist = "The Beach Boys"

    for language in ["de", "sv"]:

        translator = LyricsTranslator(language)
        lyrics = translator.get_song_translation(song, artist)
        lyrics.save()
        print(lyrics)
