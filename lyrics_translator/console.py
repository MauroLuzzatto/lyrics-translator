import click

from lyrics_translator import LyricsTranslator

from . import __version__


@click.command()
@click.option(
    "--song", default="Surfin' U.S.A.", help="Name of the song to be translated."
)
@click.option("--artist", default="The Beach Boys", help="Name of the artist.")
@click.option(
    "--language", default="de", help="Language to song lyrics to translate to."
)
@click.option(
    "--testing",
    default=False,
    help='Mode of developement, if testing is set to "True" only dummy data is used',
)
@click.version_option(version=__version__)
def main(song, artist, language, testing):
    translator = LyricsTranslator(language)
    lyrics = translator.get_song_translation(song, artist, testing)
    title = f"'{song}' by '{artist}' translated into '{language}'"

    click.secho(title, fg="green")
    click.echo(lyrics)
