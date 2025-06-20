from model.mealie.shoppingListItem import Label
from model.mealieLableEmbeddings import MealieLabelEmbedding, MealieLabelEmbeddings
from sentence_transformers import SentenceTransformer, util

class EmbeddingService:

    def computingLabelEmbeddings(self, labels: list[Label], modelName : str = "sentence-transformers/all-MiniLM-L12-v2") -> MealieLabelEmbeddings:
        labelEmbeddings = []
        
        model = SentenceTransformer(modelName)
        for label in labels:
            labelEmbeddings.append(
                MealieLabelEmbedding(
                    label=label,
                    embedding=model.encode(label.name, convert_to_tensor=True)
                )
            )
        
        return MealieLabelEmbeddings(labels=labelEmbeddings, model=model)


    def findClosest(self, term : str, embeddings: MealieLabelEmbeddings):

        termEmbedding = embeddings.model.encode(term, convert_to_tensor=True)
        distancePool = [(util.cos_sim(termEmbedding, d.embedding).item(),d) for d in embeddings.labels]

        
        closest = max(distancePool, key=lambda score: score[0])
        return closest[1]



