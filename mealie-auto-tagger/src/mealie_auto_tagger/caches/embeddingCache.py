from mealie_auto_tagger.services.embedding.embeddingService import embeddingService
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel
from mealie_auto_tagger.model.mealieLableEmbeddings import MealieLabelEmbedding

class __EmbeddingCache:
    _embeddings:dict[str,MealieLabelEmbedding] = {}

    def getLabelEmbedding(self, label:MealieLabel ):
        embedding = self._embeddings.get(label.name)
        if embedding == None:
            embedding = embeddingService.computeLabelEmbedding(label)
            self._embeddings[label.name] = embedding
        return embedding
    
embeddingCache = __EmbeddingCache()