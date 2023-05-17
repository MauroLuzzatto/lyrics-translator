
<!-- <p align="center">
<img src="https://github.com/MauroLuzzatto/lyrics-translator/blob/main/docs/img/logo.jpg" width="200" height="200"/>
</p> -->

<h1 align="center">🎵 LyricsTranslator - automated lyrics translation</h1>



<p align="center">

<a href="https://pypi.python.org/pypi/lyrics-translator" target="_blank">
    <img src="https://img.shields.io/pypi/v/lyrics-translator.svg" alt="pypi version">
</a>

<a href="https://pypi.org/project/lyrics-translator" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/lyrics-translator.svg" alt="Supported versions">
</a>

<a href="https://github.com/ambv/black" target="_blank">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square" alt="Code style: black">
</a>


<a href="https://pycqa.github.io/isort/" target="_blank">
    <img src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336" alt="Imports: isort">
</a>


<a href="https://github.com/MauroLuzzatto/lyrics-translator/actions?workflow=Tests" target="_blank">
    <img src="https://github.com/MauroLuzzatto/lyrics-translator/workflows/Tests/badge.svg" alt="Tests">
</a>

</p>


---

**Documentation**: <a href="https://mauroluzzatto.github.io/lyrics-translator" target="_blank">https://mauroluzzatto.github.io/lyrics-translator</a>

**Source Code**: <a href="https://github.com/MauroLuzzatto/lyrics-translator" target="_blank">https://github.com/MauroLuzzatto/lyrics-translator</a>

---


`LyricsTranslator` is a Python module that allows you to download lyrics from the popular music lyrics website [genius](https://genius.com/) and translate them into a target language of your choice. The module uses the powerful 🤗[hugging face](https://huggingface.co/) library for translation, which provides state-of-the-art performance in natural language processing tasks.

With `LyricsTranslator`, you can easily translate the lyrics of your favorite songs into different languages, allowing you to appreciate the beauty and meaning of the lyrics in a language that you're comfortable with. This can be particularly helpful if you're learning a new language or if you want to explore the cultural nuances of a different language.

The module supports all languages that are available on the [OPUS-MT](https://github.com/Helsinki-NLP/Opus-MT) platform, which includes languages from all around the world. Whether you're interested in German, Spanish, Chinese, Japanese, or any other language, LyricsTranslator has got you covered. The full list of list of languages can be found on 🤗[hugging face](https://huggingface.co/models?other=marian).


All languages that are supported by [OPUS-MT](https://github.com/Helsinki-NLP/Opus-MT) are available for translation.

- German: `de`
- Swedish: `sv`
- French: `fr`
- Spanish: `es` 
- Chinese: `zh`
- Japanese: `ja`
- Portuguese: `pt`
- Arabic: `ar`
- Italian: `it`

and many more ...





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
