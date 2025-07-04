import sys
from datasets import load_dataset
from mealie_auto_tagger.services.embedding.embeddingService import __EmbeddingService
from mealie_auto_tagger.model.mealie.shoppingListItem import MealieLabel

def LabelFromStr(name: str) -> MealieLabel:
    return MealieLabel(name=name, color="", groupId="", id="")
    

testSet = load_dataset("Scuccorese/food-ingredients-dataset", split="train")


def main(modelName:str):
    embeddingService = __EmbeddingService(modelName)

    categories = set()
    score = 0

    for ingredient in testSet:
        categories.add(ingredient['category'])

    categories = [LabelFromStr(n) for n in categories]

    labelEmbeddings = embeddingService.computingLabelEmbeddings(list(categories))

    for ingredient in testSet:
        output = embeddingService.findClosest(ingredient['ingredient'], labelEmbeddings)
        if ingredient['category'] == output.label.name:
            score += 1

    return score/len(testSet)


if __name__ == "__main__":
    modelName = sys.argv[1]
    score = main(modelName)
    print(f"|{modelName}|{score}|")