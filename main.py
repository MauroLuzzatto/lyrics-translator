from pathlib import Path

from lyrics_translator import LyricsTranslator, create_folder, get_base_path

if __name__ == "__main__":

    base_path = get_base_path()
    resources_path = Path(base_path / "resources")
    folder = create_folder(Path(base_path / "lyrics"))

    songs = [
        ("Surfin' U.S.A.", "The Beach Boys", "de"),
        ("Surfin' U.S.A.", "The Beach Boys", "sv"),
    ]

    for index, (song, artist, language) in enumerate(songs):
        translator = LyricsTranslator(language)
        lyrics = translator.get_song_translation(song, artist)
        print(index, lyrics)
        lyrics.save(folder)
