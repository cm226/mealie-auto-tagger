from model.mealie.shoppingListItem import Label
from pydantic import BaseModel, ConfigDict
from sentence_transformers import SentenceTransformer
from torch import Tensor


class MealieLabelEmbedding(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    label : Label
    embedding : Tensor

class MealieLabelEmbeddings(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    labels : list[MealieLabelEmbedding]
    model : SentenceTransformer
