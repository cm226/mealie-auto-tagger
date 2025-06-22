from model.mealie.shoppingListItem import MealieLabel
from pydantic import BaseModel, ConfigDict
from sentence_transformers import SentenceTransformer
from torch import Tensor


class MealieLabelEmbedding(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    label : MealieLabel
    embedding : Tensor

class MealieLabelEmbeddings(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    labels : list[MealieLabelEmbedding]
    model : SentenceTransformer

    def getLabelByID(self, id:str):
        return next(
            filter(
                lambda x: x.label.id == id, self.labels
            ))
