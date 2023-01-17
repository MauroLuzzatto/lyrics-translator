import pytest

from lyrics_translator.core.translator import Translator

short_text = "Hello my friends! How are you doing today?"
expected_short = "Hallo meine Freunde, wie machen Sie heute?"

long_text = """Importing AutoTokenizer and AutoModelForSeq2SeqLM from transformers."""
expected_long = """Importieren von AutoTokenizer und AutoModelForSeq2SeqLM aus Transformatoren."""


lyrics = """[Verse 2]
We'll all be planning that route
We're gonna take real soon
We're waxing down our surfboards
We can't wait for June
We'll all be gone for the summer
We're on surfari to stay
Tell the teacher we're surfin'
Surfin' U.S.A"""

expected_lyrics = """[Version 2]
Wir alle planen diesen Weg
Wir werden bald wirklich nehmen
Wir wuchsen unsere Surfboards ab.
Wir können nicht auf Juni warten
Wir werden alle für den Sommer weg sein
Wir sind auf surfari zu bleiben
Sagen Sie dem Lehrer, wir surfen!
Surfen in den USA"""


@pytest.fixture
def translator():
    return Translator(language="de")

def test_get_model_name(translator):
    assert "t5-small" == translator.get_model_name()


@pytest.mark.parametrize("language, lyrics, expected", [
    ("de", short_text, expected_short),
    ("de", long_text, expected_long),
    ("de", lyrics, expected_lyrics),
])
def test_translate(language, lyrics, expected):

    translator = Translator(language)
    translator.get_translator_pipeline()
    translation = translator.translate(lyrics)
    assert translation.strip() == expected.strip()