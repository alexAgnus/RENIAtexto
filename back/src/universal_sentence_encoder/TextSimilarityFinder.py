from src.universal_sentence_encoder.TextEncoder import TextEncoder
from sklearn.metrics.pairwise import cosine_similarity


class TextSimilarityFinder:
    def __init__(self, *, text_encoder: TextEncoder):
        self.text_encoder = text_encoder

    def execute(self, reference_text: str, text_list: [str]):
        encoded_reference = self.text_encoder.encode([reference_text])
        encoded_texts = self.text_encoder.encode(text_list)
        similarities = cosine_similarity(encoded_reference, encoded_texts)
        return similarities[0]
