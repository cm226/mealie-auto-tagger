from sentence_transformers import SentenceTransformer, util
from datasets import load_dataset

import time

from setup import ds, model

def compare(w1, w2):
    start_time = time.time()
    embedding1 = model.encode(w1, convert_to_tensor=True)
    embedding2 = model.encode(w2, convert_to_tensor=True)
    print("--- %s seconds ---" % (time.time() - start_time))
    return util.cos_sim(embedding1, embedding2)



#categorys = ["vegetable", "meat", "dairy", "fish", "bread", "sauce", "oil", "pasta"]

#examples = ["carrot", "beef", "peas", "milk", "chicken", "black beans", "pork", "pak-choi"]
testSet = ds.shuffle(seed=42).select(range(100))

categorys = set()

for ingredient in testSet:
    categorys.add(ingredient['category'])

overall = 0
for ingredient in testSet:
    scores = []
    for category in categorys:
        scores.append({'example':ingredient['ingredient'],
            'category': category,
            'score': compare(ingredient['ingredient'], category)[0][0].item()
        })

    most = max(scores, key=lambda s: s['score'])
    if most['category'] == ingredient['category']:
        overall += 1
    else:
        print("incorrect: " + most['category'] + " != " + ingredient['category'] + " - " + ingredient['ingredient'])

print(overall / len(testSet))

#examples = ["500 g (1 lb 2 oz) regular minced (ground) beef",
#"½ cup (30 g) panko breadcrumbs",
#"1 egg",
#"1 tbsp Worcestershire sauce",
#"2 tbsp olive oil",
#"4 brioche rolls, halved and toasted",
#"2 tomatoes, finely sliced",
#"1 red onion, finely sliced",
#"4 teaspoons whole-egg mayonnaise",
#"Sweet potatoes"]


#for example in examples:
    #scores = []
    #for category in categorys:
        #scores.append({'example':example,
                        #'category': category,
                         #'score': compare(example, category)[0][0].item()
                        #})

    #most = max(scores, key=lambda s: s['score'])
    #print(most['example'] + ' = ' + most['category'])



