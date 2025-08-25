"""Model evaluation
Script to evaulate the performance of models
"""

import sys
from datasets import load_dataset
from mealie_auto_tagger.services.embedding.embeddingService import __EmbeddingService
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel

def label_from_str(name: str) -> MealieLabel:
    return MealieLabel(name=name, color="", groupId="", id="")

testSet = load_dataset("Scuccorese/food-ingredients-dataset", split="train")


def main(model_name:str):
    embedding_service = __EmbeddingService(model_name)

    categories = set()
    score = 0

    for ingredient in testSet:
        categories.add(ingredient['category'])

    categories = [label_from_str(n) for n in categories]

    label_embeddings = embedding_service.computingLabelEmbeddings(list(categories))

    for ingredient in testSet:
        output = embedding_service.findClosest(ingredient['ingredient'], label_embeddings)
        if ingredient['category'] == output.label.name:
            score += 1

    return score/len(testSet)


if __name__ == "__main__":
    modelName = sys.argv[1]
    score = main(modelName)
    print(f"|{modelName}|{score}|")
