from functools import lru_cache

import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

torch.multiprocessing.freeze_support()


cache = {}


class Translator(object):
    def __init__(self, language: str, origin_language: str = "en"):
        self.language = language
        self.origin_language = origin_language

    @lru_cache(maxsize=5)
    def get_translator_pipeline(self) -> None:
        """[summary]

        Raises:
            ValueError: [description]

        """
        if self.language == "de" and self.origin_language == "en":
            model_name = "t5-small"
        else:
            print("trying to find the model....")
            model_name = f"Helsinki-NLP/opus-mt-{self.origin_language}-{self.language}"

        if model_name in cache:
            self.translator = cache[model_name]
        else:
            try:
                tokenizer = AutoTokenizer.from_pretrained(
                    model_name, model_max_length=512, skip_special_tokens=True
                )
                model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

            except OSError as err:
                message = f'{err} -- language "{self.language}" is not supported!'
                raise ValueError(message)

            self.translator = pipeline(
                f"translation_{self.origin_language}_to_{self.language}",
                model=model,
                tokenizer=tokenizer,
            )
            cache[model_name] = self.translator

        print(
            f'Setup translator_pipeline to translate from "{self.origin_language}" to'
            f' "{self.language}" using "{model_name}"!'
        )

    def translate(self, text: str) -> str:
        """[summary]

        Args:
            text (str): [description]

        Returns:
            str: [description]
        """
        print("Song is being translated, this can take a while...")

        skip_token = "_11111111_"

        sentences = [
            sentence.strip() if sentence.strip() != "" else skip_token
            for sentence in text.strip().split("\n")
        ]
        output = []
        for translation in self.translator(sentences, batch_size=8):
            output.append(translation["translation_text"])

        output_sentences = "\n".join(output)
        return output_sentences.replace(skip_token, "\n")

    def load_config():
        """to be implemented"""
        pass


if __name__ == "__main__":

    language = "de"  # "de"
    short_text = "Hello my friends! How are you doing today?"

    long_text = """
        Importing AutoTokenizer and AutoModelForSeq2SeqLM from transformers. Note that you need to import TFAutoModelForSeq2SeqLM if you want the TensorFlow equivalent.
        Initializing the Tokenizer. We’ll be using the Helsinki-NLP pretrained/finetuned OpusMT English to Dutch model for initializing the tokenizer. Using a tokenizer, we can convert textual inputs into tokens.
        Initializing the model. Using the same pretrained/finetuned model, we can generate translations.
        We then tokenize the input text in a Seq2Seq fashion as if we convert a batch of one sentence (hence wrapping everything inside a Python list).
        We then generate a translation for all the elements in the batch, decode the batch, and take the first element.
        Which is the translated text that we then print on screen.
    """

    lyrics = """
        Surfin’ USA Lyrics[Verse 1]
        If everybody had an ocean
        Across the U.S.A
        Then everybody'd be surfin'
        Like Californi-a
        You'd see them wearing their baggies
        Huarache sandals too
        A bushy bushy blond hairdo
        Surfin' U.S.A

        [Chorus]
        You'd catch 'em surfin' at Del Mar
        (Inside, outside, U.S.A.)
        Ventura County line
        (Inside, outside, U.S.A.)
        Santa Cruz and Trestles
        (Inside, outside, U.S.A.)
        Australia's Narrabeen
        (Inside, outside, U.S.A.)
        All over Manhattan
        (Inside, outside, U.S.A.)
        And down Doheny Way
        (Inside, outside)
        [Hook]
        Everybody's gone surfin'
        Surfin' U.S.A

        [Verse 2]
        We'll all be planning that route
        We're gonna take real soon
        We're waxing down our surfboards
        We can't wait for June
        We'll all be gone for the summer
        We're on surfari to stay
        Tell the teacher we're surfin'
        Surfin' U.S.A

        [Chorus]
        Haggerties and Swamis
        (Inside, outside, U.S.A.)
        Pacific Palisades
        (Inside, outside, U.S.A.)
        San Onofre and Sunset
        (Inside, outside, U.S.A.)
        Redondo Beach LA
        (Inside, outside, U.S.A.)
        All over La Jolla
        (Inside, outside, U.S.A.)
        At Wa'imea Bay
        (Inside, outside)
        You might also like[Hook]
        Everybody's gone surfin'
        Surfin' U.S.A

        [Instrumental Interlude]

        [Outro]
        Everybody's gone surfin'
        Surfin' U.S.A

        Everybody's gone surfin'
        Surfin' U.S.A

        Yeah everybody's gone surfin'
        Surfin' U.S.A

        Yeah everybody's gone surfin'
        Surfin' U.S.A12Embed
        """
    translator = Translator(language)
    translator.get_translator_pipeline()
    # translation = translator.translate(long_text)
    translation = translator.translate_fast(lyrics)

    print("----" * 10)
    print(translation)
