from functools import lru_cache

import torch
from tqdm import tqdm
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
            model_name = "t5-large"
        elif self.language in ["fr", "sv"]:
            model_name = f"Helsinki-NLP/opus-mt-{self.origin_language}-{self.language}"
        else:
            print("trying to find a model....")
            model_name = f"Helsinki-NLP/opus-mt-{self.origin_language}-{self.language}"

        if model_name in cache:
            self.translator = cache[model_name]
        else:
            try:
                tokenizer = AutoTokenizer.from_pretrained(
                    model_name, model_max_length=512
                )
            except OSError as err:
                message = f'{err} -- language "{self.language}" is not supported!'
                raise ValueError(message)

            model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

            self.translator = pipeline(
                f"translation_en_to_{self.language}", model=model, tokenizer=tokenizer
            )
            cache[model_name] = self.translator

        print(
            f'Setup translator_pipeline to translate from "{self.origin_language}" to'
            f' "{self.language}" using {model_name}!'
        )

    def translate(self, text: str, short: bool = False) -> str:
        """[summary]

        Args:
            text (str): [description]
            translator (pipeline): [description]

        Returns:
            str: [description]
        """
        print("Song is being translated, this can take a while...")
        batch_size = 20
        list_of_text = [entry.strip() for entry in text.strip().split("\n")]
        number_of_lines = len(list_of_text)

        if short:
            numbers_of_paragraphs = 1
        else:
            numbers_of_paragraphs = int(number_of_lines / batch_size) + 1

        output = []

        for paragraph in tqdm(range(numbers_of_paragraphs)):
            start = paragraph * batch_size
            end = min((paragraph + 1) * batch_size, number_of_lines)

            print(f"Translation line {start} to {end} out of {number_of_lines}")

            translation = self.translator(list_of_text[start:end])

            output.extend(
                [output_text["translation_text"] for output_text in translation]
            )
        return "\n".join(output)

    def load_config():
        """to be implemented"""
        pass


if __name__ == "__main__":

    language = "de"
    short_text = "Hello my friends! How are you doing today?"

    long_text = """
        Importing AutoTokenizer and AutoModelForSeq2SeqLM from transformers. Note that you need to import TFAutoModelForSeq2SeqLM if you want the TensorFlow equivalent.
        Initializing the Tokenizer. We’ll be using the Helsinki-NLP pretrained/finetuned OpusMT English to Dutch model for initializing the tokenizer. Using a tokenizer, we can convert textual inputs into tokens.
        Initializing the model. Using the same pretrained/finetuned model, we can generate translations.
        We then tokenize the input text in a Seq2Seq fashion as if we convert a batch of one sentence (hence wrapping everything inside a Python list).
        We then generate a translation for all the elements in the batch, decode the batch, and take the first element.
        Which is the translated text that we then print on screen.
    """
    translator = Translator(language)
    translator.get_translator_pipeline()
    translation = translator.translate(long_text)
    print("----" * 10)
    print(translation)
