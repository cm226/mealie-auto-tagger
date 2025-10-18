from mealie_auto_tagger.services.embedding.embeddingService import embeddingService
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel
from mealie_auto_tagger.model.mealie_label_embeddings import MealieLabelEmbedding


class _EmbeddingCache:
    _embeddings: dict[str, MealieLabelEmbedding] = {}

    def get_label_embedding(self, label: MealieLabel):
        embedding = self._embeddings.get(label.name)
        if embedding is None:
            embedding = embeddingService.computeLabelEmbedding(label)
            self._embeddings[label.name] = embedding
        return embedding


embedding_cache = _EmbeddingCache()
