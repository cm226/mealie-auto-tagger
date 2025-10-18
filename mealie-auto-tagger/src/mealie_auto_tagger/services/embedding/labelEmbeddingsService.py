from mealie_auto_tagger.db.init import SessionLocal
from mealie_auto_tagger.db.repos.all_repositories import get_repositories
from mealie_auto_tagger.services.mealie_labels import mealieLabels
from mealie_auto_tagger.caches.embedding_cache import embedding_cache
from mealie_auto_tagger.model.mealie_label_embeddings import MealieLabelEmbeddings


class __LabelEmbeddingsService():
    def computeLabelEmbeddings(self):
        labels = mealieLabels.get_all_labels()

        with SessionLocal() as session:
            get_repositories(session)\
                .labelRepo\
                .storeAllMealieLabels(labels)

        labels = [embedding_cache.get_label_embedding(
            label) for label in labels]
        return MealieLabelEmbeddings(
            labels=labels,
            model=labels[0].model
        )


labelEmbeddingsService = __LabelEmbeddingsService()
