from fastapi import FastAPI
from src.shared.GetPfsiCases import GetPfsiCases
from src.universal_sentence_encoder.Classifier import Classifier
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/check-health")
def check_health():
    return {"status": "ok"}


@app.get("/api/get-pfsi-cases")
def get_pfsi_cases():
    text_list_result = GetPfsiCases().execute(filepath="assets/dataset-pfsi.csv")
    return {"status": "ok", "data": [x.to_dict() for x in text_list_result]}


@app.get("/api/get-similar-texts-with-universal-sentence-encoder")
def get_similar_texts_with_universal_sentence_encoder(description: str):
    text_list_result = Classifier.run(reference_text=description)
    return {"status": "ok", "data": [x.to_dict() for x in text_list_result]}
