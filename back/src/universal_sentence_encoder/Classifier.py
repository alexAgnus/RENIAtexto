from src.pfsi.pfsi_case import PfsiCase
from src.shared.DatasetListMapper import DatasetListMapper
from src.universal_sentence_encoder.LoadTensorflowModel import LoadTensorflowModel
from src.universal_sentence_encoder.TextEncoder import TextEncoder
from src.universal_sentence_encoder.TextSimilarityFinder import TextSimilarityFinder

USE_MODEL_URL = "https://tfhub.dev/google/universal-sentence-encoder/4"


class Classifier:
    @staticmethod
    def run(reference_text: str):
        use_model = LoadTensorflowModel().load_model(model_url=USE_MODEL_URL)
        text_encoder = TextEncoder(use_model=use_model)
        dataset_list_mapper = DatasetListMapper()
        text_list = dataset_list_mapper.execute(
            filepath="assets/dataset-pfsi.csv"
        )

        text_similarity_finder = TextSimilarityFinder(
            text_encoder=text_encoder
        )
        similarities = text_similarity_finder.execute(
            reference_text=reference_text, text_list=text_list
        )

        text_list_with_similarities: [PfsiCase] = []
        for i, similarity in enumerate(similarities):
            text_list_with_similarities.append(PfsiCase(description=text_list[i], id=i, similarity=similarity))
            # print(f"Similarity with text {text_list[i]} is {similarity}")

        text_list_with_similarities.sort(key=lambda x: x.similarity, reverse=True)
        # Print the first 10
        # for i in range(10):
        #     print(
        #         f"🧨 Similarity with text {text_list_with_similarities[i][0]} is {text_list_with_similarities[i][1]}"
        #     )
        return text_list_with_similarities[:100]
