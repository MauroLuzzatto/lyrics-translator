# Lyrics Translator

[![pypi version](https://img.shields.io/pypi/v/lyrics-translator.svg)](https://pypi.python.org/pypi/lyrics-translator)
[![Supported versions](https://img.shields.io/pypi/pyversions/lyrics-translator.svg)](https://pypi.org/project/lyrics-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)


The `Lyrics Translator` downloads lyrics from genius and uses hugging face to translate the English lyrics into a target language.


## Install lyrics-translator

```
pip install lyrics-translator
```

## Setup
To use the `Lyrics Translator` you will have to create an API token from `genius`: https://docs.genius.com/#/getting-started-h1


add the API token to the `.env` file:
```txt
GENIUS_ACCESS_TOKEN=M8Mx-chHJKKUEJLSOEI893793KJQu3_
```


## Usage
<!--
📚 A comprehensive example of the `explainy` API can be found in this ![Jupyter Notebook](https://github.com/MauroLuzzatto/explainy/blob/main/examples/01-explainy-intro.ipynb)

📖 Or in the [example section](https://explainy.readthedocs.io/en/latest/examples/01-explainy-intro.html) of the documentation -->





```python
from dotenv import dotenv_values
from lyrics_translator import LyricsTranslator, create_folder, get_base_path


config = dotenv_values(".env")

song = "Surfin' U.S.A."
artist = "The Beach Boys"
language = "de"

lyrics = LyricsTranslator(song, artist, config, language)
lyrics.get_song_translation()
print(lyrics)
```


## Author
**Mauro Luzzatto** - [Maurol](https://github.com/MauroLuzzatto)
