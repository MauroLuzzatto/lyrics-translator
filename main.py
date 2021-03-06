from pathlib import Path

from dotenv import dotenv_values

from lyrics_translator import LyricsTranslator, create_folder, get_base_path

if __name__ == "__main__":

    base_path = get_base_path()
    resources_path = Path(base_path / "resources")
    folder = create_folder(Path(base_path / "lyrics"))

    config = dotenv_values(".env")

    songs = [
        ("Surfin' U.S.A.", "The Beach Boys", "de"),
        ("Surfin' U.S.A.", "The Beach Boys", "sv"),
    ]

    for index, (song, artist, language) in enumerate(songs):
        lyrics = LyricsTranslator(song, artist, config, language, testing=False)
        lyrics.get_song_translation()
        lyrics.save(folder)
        print(index, lyrics)
