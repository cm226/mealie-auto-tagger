from mealie_auto_tagger.db.init import SessionLocal
from mealie_auto_tagger.db.repos.all_repositories import get_repositories
from mealie_auto_tagger.services.mealieLabels import mealieLabels
from mealie_auto_tagger.caches.embeddingCache import embeddingCache
from mealie_auto_tagger.model.mealieLableEmbeddings import MealieLabelEmbeddings

class __LabelEmbeddingsService():
    def computeLabelEmbeddings(self):
        labels = mealieLabels.getAllLabels()

        with SessionLocal() as session:
            get_repositories(session)\
                .labelRepo\
                .storeAllMealieLabels(labels)

        labels=[embeddingCache.getLabelEmbedding(label) for label in labels]
        return MealieLabelEmbeddings(      
            labels=labels,
            model=labels[0].model
        )

labelEmbeddingsService = __LabelEmbeddingsService()