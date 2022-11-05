try:
    from importlib.metadata import version, PackageNotFoundError  # type: ignore
except ImportError:  # pragma: no cover
    from importlib_metadata import version, PackageNotFoundError  # type: ignore

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

from lyrics_translator.core.lyrics_translator import LyricsTranslator
from lyrics_translator.core.utils import create_folder, get_base_path, read_songs
