import tensorflow as tf
import tensorflow_hub as hub

class LoadTensorflowModel:

    def load_model(self, *, model_url: str):
        print(f"✅ Loading model from {model_url}")
        model = hub.load(model_url)
        print("✅ Model loaded")
        return model