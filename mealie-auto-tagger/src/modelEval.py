import sys
from datasets import load_dataset
from services.embedding.embeddingService import __EmbeddingService
from model.mealie.shoppingListItem import MealieLabel

def LabelFromStr(name: str) -> MealieLabel:
    return MealieLabel(name=name, color="", groupId="", id="")
    

ds = load_dataset("Scuccorese/food-ingredients-dataset", split="train")
testSet = ds.shuffle(seed=42).select(range(100))


def main(modelName:str):
    embeddingService = __EmbeddingService()

    categories = set()
    for ingredient in testSet:
        categories.add(ingredient['category'])

    categories = [LabelFromStr(n) for n in categories]

    labelEmbeddings = embeddingService.computingLabelEmbeddings(list(categories), modelName=modelName)

    outputs = []
    for ingredient in testSet:
        outputs.append((ingredient, embeddingService.findClosest(ingredient['ingredient'], labelEmbeddings)))


    score = 0
    for gt, result in outputs:
        if gt['category'] == result.label.name:
            score += 1
    return score/len(outputs)


if __name__ == "__main__":
    modelName = sys.argv[1]
    score = main(modelName)
    print(f"|{modelName}|{score}|")