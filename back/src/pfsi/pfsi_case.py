from pydantic import BaseModel

class PfsiCase(BaseModel):
    description: str
    id: int
    similarity: float

    def to_dict(self):
        return {
            "description": self.description,
            "id": self.id,
            "similarity": self.similarity
        }