import pytest
from lyrics_translator import LyricsTranslator


song = "Surfin' U.S.A."
artist = "The Beach Boys"
language = "de"


@pytest.fixture
def translator():
    return LyricsTranslator(language="de")


def test_get_song_translation(translator):
    translation = translator.get_song_translation(song, artist)

    output = translation[:100]
    expected = """63 ContributorsSurfin’ USA Lyrics[Verse 1]
    Wenn jeder einen Ozean hätte
    In den USA
    Dann wären alle s"""
    assert output.strip() == expected.strip()


def test_get_song_lyrics(translator):
    lyrics = translator.get_song_lyrics(song, artist)

    output = lyrics[:100]
    expected = """63 ContributorsSurfin’ USA Lyrics[Verse 1]
    If everybody had an ocean
    Across the U.S.A
    Then everybody"""
    assert output.strip() == expected.strip()
