from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import torch

torch.multiprocessing.freeze_support()


cache = {}


class Translator(object):
    def __init__(self, language: str):
        self.language = language

    def get_translator_pipeline(self) -> None:
        """[summary]

        Args:
            language (str): [description]

        Raises:
            ValueError: [description]

        Returns:
            pipeline: [description]
        """

        if self.language == "de":
            model_name = "t5-large"
        elif self.language in ["fr", "sv"]:
            model_name = f"Helsinki-NLP/opus-mt-en-{self.language}"
        else:
            raise ValueError(f'"{self.language}" is not supported!')

        print(
            f"Setup translator_pipeline for language {self.language}, using {model_name}!"
        )

        if model_name in cache:
            self.translator = cache[model_name]
        else:

            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
            self.translator = pipeline(
                f"translation_en_to_{self.language}", model=model, tokenizer=tokenizer
            )
            cache[model_name] = self.translator

    def translate(self, text: str, max_lines: int = 20) -> str:
        """[summary]

        Args:
            text (str): [description]
            translator (pipeline): [description]

        Returns:
            str: [description]
        """
        print("Song is being translated, this can take a while...")
        text = text.strip().split("\n")[:max_lines]
        return "\n".join(
            [output["translation_text"] for output in self.translator(text)]
        )


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

    translator = get_translator_pipeline(language)
    translation = get_translation(long_text, translator)
    print("----" * 10)
    print(translation)
