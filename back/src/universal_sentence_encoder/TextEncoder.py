class TextEncoder:
    def __init__(self, use_model):
        self.use_model = use_model

    def encode(self, text_list: [str]):
        embeddings = self.use_model(text_list)
        return embeddings
