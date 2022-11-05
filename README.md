# Lyrics Translator

[![pypi version](https://img.shields.io/pypi/v/lyrics-translator.svg)](https://pypi.python.org/pypi/lyrics-translator)
[![Supported versions](https://img.shields.io/pypi/pyversions/lyrics-translator.svg)](https://pypi.org/project/lyrics-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)


The `LyricsTranslator` downloads lyrics from [genius](https://genius.com/) and uses 🤗[hugging face](https://genius.com/) to translate the lyrics into a target language.


## Install

```
pip install lyrics-translator
```

## Setup
To use the `LyricsTranslator` you will have to [get an API token](https://docs.genius.com/#/getting-started-h1) from `genius` add the API token to the `.env` file:

```txt
GENIUS_ACCESS_TOKEN=<replace-me-with-your-genius-api-token>
```

## Usage
<!--
📚 A comprehensive example of the `explainy` API can be found in this ![Jupyter Notebook](https://github.com/MauroLuzzatto/explainy/blob/main/examples/01-explainy-intro.ipynb)

📖 Or in the [example section](https://explainy.readthedocs.io/en/latest/examples/01-explainy-intro.html) of the documentation -->


```python
from lyrics_translator import LyricsTranslator

song = "Surfin' U.S.A."
artist = "The Beach Boys"
language = "de"

translator = LyricsTranslator(language)
lyrics = translator.get_song_translation(song, artist)
print(lyrics)
```
Output:
```
Surfin’ USA Lyrics[Verse 1]
Wenn jeder einen Ozean hätte
Überall in den USA
Dann würde jeder surfen
Wie Californi-a
Sie würden ihre Taschen tragen.
Auch Huarache Sandalen
Ein stumpfes stumpfes blond Haar
Surfin' U.S.A

[Korus]
Sie würden sie surfen in Del Mar
(Innen, Außen, USA)
Ventura County Line
(Innen, Außen, USA)
Santa Cruz und Trestles
(Innen, Außen, USA)
Australiens Narrabeen
(Innen, Außen, USA)
Überall in Manhattan
(Innen, Außen, USA)
Und den Doheny Way hinunter
(Innen, Außen)
[Anschlag]
Jeder ist surfin'
Surfin' U.S.A

[Zwischenruf 2]
Wir werden alle diese Route planen.
Wir werden wirklich bald
Wir wischen unsere Surfbretter ab
Wir können auf Juni nicht warten
Wir werden alle für den Sommer weg sein
Wir sind auf surfari zu bleiben
Sagen Sie dem Lehrer, wir surfen
Surfin' U.S.A

[Korus]
Haggerties und Swamis
(Innen, Außen, USA)
Palisaden im Pazifik
(Innen, Außen, USA)
San Onofre und der Sonnenuntergang
(Innen, Außen, USA)
Redondo Beach LA
(Innen, Außen, USA)
Ganz La Jolla
(Innen, Außen, USA)
In der Bucht von Wa'imea
(Innen, Außen)
[Anschlag]
Jeder ist surfin'
Surfin' U.S.A

[Instrumental Interlude]

[Outro]
Jeder ist surfin'
Surfin' U.S.A

Jeder ist surfin'
Surfin' U.S.A

Jeder ist surfin'
Surfin' U.S.A

Jeder ist surfin'
Surfin' U.S.A
```
