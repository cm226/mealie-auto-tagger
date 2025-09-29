from mealie_auto_tagger.services.embedding.labelEmbeddingsService import labelEmbeddingsService


class LabelEmbeddingsCache:

    label_embeddings = None

    def update(self):
        self.label_embeddings = labelEmbeddingsService.computeLabelEmbeddings()

    def get(self):
        if self.label_embeddings is None:
            self.update()
        return self.label_embeddings
