from pydantic import BaseModel, ConfigDict, model_validator
from sentence_transformers import SentenceTransformer
from torch import Tensor
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel


class MealieLabelEmbedding(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    label: MealieLabel
    embedding: Tensor
    model: SentenceTransformer


class MealieLabelEmbeddings(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    labels: list[MealieLabelEmbedding]
    model: SentenceTransformer

    @model_validator(mode='after')
    def validate_models(self) -> 'MealieLabelEmbeddings':
        if not self.labels:
            raise ValueError("Labels list cannot be empty")

        first_model = self.labels[0].model
        for label in self.labels:
            if label.model != first_model:
                raise ValueError("All labels must use the same model")

        object.__setattr__(self, 'model', first_model)
        return self

    def get_label_by_id(self, label_id: str):
        return next(
            filter(
                lambda x: x.label.id == label_id, self.labels
            ), None)
